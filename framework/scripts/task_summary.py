#!/usr/bin/env python3
"""Derive task display fields from every structured queue; never decide runtime release.

No second queue. --write preserves previous display values in STATE_SUMMARY_HISTORY.
Writers must use their own task checkout; this does not lock other manual editors.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile


def derive(data):
    queues = [(k, v) for k, v in data.items() if k.startswith('AUTHORISED_QUEUE')]
    if not queues:
        raise ValueError('no structured queue')
    states, steps = [], []
    for key, queue in queues:
        if not isinstance(queue, dict) or queue.get('MANDATE_STATE') not in ('OPEN', 'COMPLETE', 'PAUSED', 'CANCELLED'):
            raise ValueError(f'{key}: missing or invalid MANDATE_STATE')
        states.append(queue['MANDATE_STATE'])
        local = []
        for name, objective in queue.items():
            if not name.startswith('OBJ_'):
                continue
            if not isinstance(objective, dict) or not isinstance(objective.get('steps'), list) or not objective['steps']:
                raise ValueError(f'{key}.{name}: missing steps')
            for step in objective['steps']:
                if not isinstance(step, dict) or step.get('status') not in ('TODO', 'IN_PROGRESS', 'DONE', 'BLOCKED'):
                    raise ValueError(f'{key}.{name}: invalid step')
                if step['status'] == 'DONE' and not step.get('evidence'):
                    raise ValueError('DONE without evidence')
                if step['status'] == 'BLOCKED' and not step.get('blocker'):
                    raise ValueError('BLOCKED without blocker')
                local.append(step)
        if not local or (queue['MANDATE_STATE'] == 'COMPLETE' and any(s['status'] != 'DONE' for s in local)):
            raise ValueError(f'{key}: completion contradicts steps or queue is empty')
        steps.extend(local)
    state = ('OPEN' if 'OPEN' in states else 'PAUSED' if 'PAUSED' in states else
             'COMPLETE' if all(s == 'COMPLETE' for s in states) else 'CANCELLED')
    done = sum(s['status'] == 'DONE' for s in steps)
    return {'CURRENT_STATE': f'{state} — {done}/{len(steps)} steps DONE (derived from all structured queues)',
            'OUTCOME': state}


def sync(path, write=False):
    before = path.read_bytes()
    data = json.loads(before)
    expected = derive(data)
    changed = any(data.get(k) != v for k, v in expected.items())
    if changed and write:
        data.setdefault('STATE_SUMMARY_HISTORY', []).append({
            'source_sha256': hashlib.sha256(before).hexdigest(),
            'previous': {k: data.get(k) for k in expected}})
        data.update(expected)
        if path.read_bytes() != before:
            raise ValueError('task changed while deriving summary')
        fd, name = tempfile.mkstemp(dir=path.parent, prefix='.summary-')
        try:
            with os.fdopen(fd, 'w') as out:
                json.dump(data, out, ensure_ascii=False, indent=2)
                out.write('\n')
            os.replace(name, path)
        finally:
            if os.path.exists(name):
                os.unlink(name)
    return changed, expected


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--record', type=Path, required=True)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    try:
        changed, expected = sync(args.record, args.write)
    except (OSError, ValueError) as error:
        print(f'UNRESOLVED: {error}')
        return 2
    print(json.dumps(expected, ensure_ascii=False))
    return 1 if changed and not args.write else 0

if __name__ == '__main__':
    raise SystemExit(main())
