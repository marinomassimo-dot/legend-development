#!/usr/bin/env python3
"""MUTATION TEST for check_participant_surface.py.

A checker that has never failed is a checker nobody has tested. This copies the real
participant directory five times, damages each copy in one specific way that a real
mistake would produce, and asserts the checker BLOCKS every one.

  M1 inject expected verdict     an EXPECTED_VERDICT field appears in a handoff
  M2 inject answer phrase        prose that states how the case comes out
  M3 inject evaluator keyword    a contamination label crosses into the participant file
  M4 inject forbidden path       a link out of the directory, into the evaluator set
  M5 remove required source      CORPUS_BOUNDARY loses its identifier

A mutation the checker does not catch is a finding against the CHECKER, printed as such
and exited non-zero. Passing this test is not proof the checker is complete; it is proof
it is not inert, which is the failure a checker most often has.

    python3 framework/eval/benchmarks/blind_rounds/mutation_test.py
"""
import os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKER = os.path.join(HERE, 'check_participant_surface.py')
SRC = os.path.join(HERE, 'participant')
TARGET = 'BLIND-R1-001.md'


def mutate_expected_verdict(text):
    return text.replace('STOP_CONDITION       Stop when',
                        'EXPECTED_VERDICT     the title is not supported by the evidence\n\n'
                        'STOP_CONDITION       Stop when')


def mutate_answer_phrase(text):
    return text.replace('> **Nothing here is medical advice.**',
                        '> **Nothing here is medical advice.**\n\n'
                        'Note for the reader: the answer is that the kinase named in the title '
                        'was never measured.')


def mutate_evaluator_keyword(text):
    return text.replace('CASE_ID              BLIND-R1-001',
                        'CASE_ID              BLIND-R1-001   (CLEAN_BLIND, rank 7, see HC-E2)')


def mutate_forbidden_path(text):
    return text.replace('Your output goes in the output slots',
                        'Background: [the frozen set](../../../../../learning/scientist/evalset/frozen_set_v1.json).\n\n'
                        'Your output goes in the output slots')


def mutate_remove_source(text):
    return re.sub(r'CORPUS_BOUNDARY      PMID 26675548[^\n]*',
                  'CORPUS_BOUNDARY      the paper supplied in your packet', text)


MUTATIONS = [
    ('M1', 'inject expected verdict', mutate_expected_verdict),
    ('M2', 'inject answer phrase', mutate_answer_phrase),
    ('M3', 'inject evaluator keyword', mutate_evaluator_keyword),
    ('M4', 'inject forbidden path', mutate_forbidden_path),
    ('M5', 'remove required source', mutate_remove_source),
]


def run_checker(d):
    r = subprocess.run([sys.executable, CHECKER, '--dir', d], capture_output=True, text=True)
    return r.returncode, r.stdout


def main():
    rc0, out0 = run_checker(SRC)
    print("BASELINE on the real surface: exit %d" % rc0)
    if rc0 != 0:
        print("VOID: the unmutated surface does not pass; fix that before mutating.\n" + out0)
        return 2
    print()

    failures = []
    for tag, desc, fn in MUTATIONS:
        tmp = tempfile.mkdtemp(prefix='mut-%s-' % tag)
        d = os.path.join(tmp, 'participant')
        shutil.copytree(SRC, d)
        p = os.path.join(d, TARGET)
        before = open(p, encoding='utf-8').read()
        after = fn(before)
        if after == before:
            print("%-3s %-28s *** MUTATION DID NOT APPLY — test is inert ***" % (tag, desc))
            failures.append((tag, desc, 'mutation did not apply'))
            shutil.rmtree(tmp, ignore_errors=True)
            continue
        open(p, 'w', encoding='utf-8').write(after)
        rc, out = run_checker(d)
        caught = rc == 1
        cls = sorted({m.group(1) for m in re.finditer(r'\[(\w+)\s*\]', out)})
        print("%-3s %-28s exit %d  %-9s classes=%s"
              % (tag, desc, rc, 'BLOCKED' if caught else 'NOT CAUGHT', ','.join(cls) or '-'))
        if not caught:
            failures.append((tag, desc, 'checker returned %d' % rc))
            print("      ---- checker output ----")
            for ln in out.strip().split('\n'):
                print("      " + ln)
        shutil.rmtree(tmp, ignore_errors=True)

    print()
    if failures:
        print("VERDICT: FAIL — %d mutation(s) not blocked. These are findings against the CHECKER."
              % len(failures))
        for t, d, why in failures:
            print("  %s %s — %s" % (t, d, why))
        return 1
    print("VERDICT: PASS — all %d mutations blocked." % len(MUTATIONS))
    print("This shows the checker is not inert. It does not show it is complete: a leak "
          "phrased in words the LANGUAGE list does not contain would pass, and the list is "
          "in the checker so it can be extended.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
