"""Run a headless browser for a test and leave nothing behind (ADV-299, HE, 2026-11-28).

Measured 2026-11-28: ~/legend_browser_tmp held 247 `tmp*` folders (each a Chromium profile `p` and the page `v.html`) from
`test_repurposing_view.py`, class `Browser`: the class-level `tempfile.TemporaryDirectory()` is removed by `tearDownClass`, which fails
("Directory not empty") when a browser child process still writes into the profile, and is not run at all when the suite is
killed; `subprocess.run(..., timeout=120)` kills only the parent browser process, never its children. Two helpers close both:

  run_browser(cmd, timeout)  start the browser in its own process group, and kill the whole group when it finishes, times out or
                             raises, so no child outlives the call.
  remove_tree(path)          stop any process still holding `path` as its profile, then remove the tree, retrying, and report
                             whether the folder is gone. Register it with `addClassCleanup` / `addCleanup` BEFORE the browser starts.
"""
from __future__ import annotations

import os
import shutil
import signal
import subprocess
import time


def run_browser(cmd: list[str], timeout: float) -> subprocess.CompletedProcess:
    """Output goes to temporary files, not pipes: a browser child that outlives its parent holds a pipe open and would block
    `communicate` until the timeout."""
    import tempfile
    with tempfile.TemporaryFile("w+") as out, tempfile.TemporaryFile("w+") as err:
        process = subprocess.Popen(cmd, stdout=out, stderr=err, text=True, start_new_session=True)
        try:
            process.wait(timeout=timeout)
        finally:
            _kill_group(process.pid)
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                pass
        out.seek(0)
        err.seek(0)
        return subprocess.CompletedProcess(cmd, process.returncode, out.read(), err.read())


def _kill_group(pid: int) -> None:
    try:
        os.killpg(pid, signal.SIGKILL)
    except (ProcessLookupError, PermissionError):
        pass


def _holders(path: str) -> list[int]:
    """pids whose command line names `path` (a browser started with --user-data-dir under it)."""
    found = []
    for entry in os.listdir("/proc"):
        if entry.isdigit() and int(entry) != os.getpid():
            try:
                with open(f"/proc/{entry}/cmdline", "rb") as handle:
                    if path.encode() in handle.read():
                        found.append(int(entry))
            except OSError:
                continue
    return found


def remove_tree(path: str, attempts: int = 8, pause: float = 0.25) -> bool:
    path = os.path.realpath(path)
    for _ in range(attempts):
        for pid in _holders(path):
            try:
                os.kill(pid, signal.SIGKILL)
            except (ProcessLookupError, PermissionError):
                pass
        shutil.rmtree(path, ignore_errors=True)
        if not os.path.exists(path):
            return True
        time.sleep(pause)
    return not os.path.exists(path)
