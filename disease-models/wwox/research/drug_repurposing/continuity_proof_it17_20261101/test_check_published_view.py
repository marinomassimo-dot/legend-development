#!/usr/bin/env python3
"""Offline tests of check_published_view.py against a local http.server on 127.0.0.1 (no external network).

  python3 -B test_check_published_view.py        # runs all cases; --help prints this text and does nothing else

A copy of the package is served under the prefix /legend-development/. The positive case must pass; each negative fixture
(one byte altered, one file missing, robots tag removed, NOTICE 404, wrong prefix, footer name dropped, anchor dropped,
external script, root-absolute href, wrong manifest entry) must fail with its expected condition line, and the
production-URL 404 must report NOT_YET_PUBLISHED (exit 3), never a pass.
"""
import contextlib
import functools
import http.server
import io
import re
import shutil
import sys
import tempfile
import threading
import unittest
from pathlib import Path

if "-h" in sys.argv or "--help" in sys.argv:
    print(__doc__)
    sys.exit(0)

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_published_view as cpv  # noqa: E402

PKG = HERE.parent / "view" / "shareable_package"
DEPLOY = HERE.parent / "view" / "DEPLOY.md"
PREFIX = "/legend-development/"


class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


@contextlib.contextmanager
def serve(root):
    """Serve `root` under PREFIX only (anything else is 404)."""
    class H(_Quiet):
        def translate_path(self, path):
            if not path.startswith(PREFIX):
                return str(Path(root) / "__no_such_path__")
            return super().translate_path("/" + path[len(PREFIX):])
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(H, directory=str(root)))
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    try:
        yield "http://127.0.0.1:%d" % srv.server_address[1]
    finally:
        srv.shutdown()
        srv.server_close()


def check(base, deploy=DEPLOY):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = cpv.main([base, "--deploy-md", str(deploy)])
    return code, buf.getvalue()


class T(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="cpv_"))
        self.root = self.tmp / "site"
        shutil.copytree(PKG, self.root)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_case(self, base_suffix=PREFIX):
        with serve(self.root) as base:
            return check(base + base_suffix)

    def edit_page(self, fn):
        p = self.root / "index.html"
        p.write_text(fn(p.read_text(encoding="utf-8")), encoding="utf-8")

    def assert_fail(self, code, out, cond, needle):
        self.assertEqual(code, 1, out)
        self.assertTrue(any(l.startswith("FAIL [%s]" % cond) and needle in l for l in out.splitlines()), out)

    def test_positive(self):
        code, out = self.run_case()
        self.assertEqual(code, 0, out)
        self.assertIn("RESULT: PASS", out)
        self.assertNotIn("FAIL", out)

    def test_one_file_altered(self):
        p = self.root / "NOTICE.md"
        p.write_bytes(p.read_bytes() + b" ")
        code, out = self.run_case()
        self.assert_fail(code, out, "b", "NOTICE.md differs from the table")

    def test_one_file_missing(self):
        (self.root / "LICENSES" / "CC0-1.0.txt").unlink()
        code, out = self.run_case()
        self.assert_fail(code, out, "b", "LICENSES/CC0-1.0.txt answers 404")

    def test_notice_404(self):
        (self.root / "NOTICE.md").unlink()
        code, out = self.run_case()
        self.assert_fail(code, out, "d", "NOTICE.md answers 404")

    def test_credit_missing(self):
        (self.root / "class_b" / "chembl_cc-by-sa-3.0" / "CREDIT.txt").unlink()
        code, out = self.run_case()
        self.assert_fail(code, out, "d", "CREDIT.txt answers 404")

    def test_robots_removed(self):
        self.edit_page(lambda h: re.sub(r'<meta name="robots"[^>]*>', "", h))
        code, out = self.run_case()
        self.assert_fail(code, out, "c", "robots meta tags found: []")

    def test_robots_twice(self):
        self.edit_page(lambda h: h.replace('<meta name="robots" content="noindex,nofollow">', '<meta name="robots" content="noindex,nofollow"><meta name="robots" content="noindex,nofollow">'))
        code, out = self.run_case()
        self.assert_fail(code, out, "c", "robots meta tags found")

    def test_wrong_prefix(self):
        code, out = self.run_case("/")
        self.assert_fail(code, out, "a", "index.html answers 404")
        self.assertIn("FAIL [c-f]", out)

    def test_footer_name_dropped(self):
        self.edit_page(lambda h: h.replace("DoCM (via DGIdb)", "Docm"))
        code, out = self.run_case()
        self.assert_fail(code, out, "e", "DoCM (via DGIdb)")

    def test_anchor_dropped(self):
        self.edit_page(lambda h: h.replace('id="deepened-cases"', 'id="x-deepened"'))
        code, out = self.run_case()
        self.assert_fail(code, out, "f", "#deepened-cases MISSING")

    def test_external_script(self):
        self.edit_page(lambda h: h.replace("</head>", '<script src="https://cdn.example.org/x.js"></script></head>', 1))
        code, out = self.run_case()
        self.assert_fail(code, out, "f", "another host")

    def test_root_absolute_reference(self):
        self.edit_page(lambda h: h.replace("</head>", '<link rel="stylesheet" href="/style.css"></head>', 1))
        code, out = self.run_case()
        self.assert_fail(code, out, "f", "root-absolute")

    def test_manifest_disagrees(self):
        p = self.root / "manifest.json"
        t = p.read_text(encoding="utf-8")
        a = '"COMPARISON.md": {"bytes": 6772'
        # same digests but one entry lies: rewrite via json to stay valid, then re-serve (digest of manifest.json changes too)
        import json
        d = json.loads(t)
        d["files"]["COMPARISON.md"]["sha256"] = "0" * 64
        p.write_text(json.dumps(d), encoding="utf-8")
        code, out = self.run_case()
        self.assertEqual(code, 1, out)
        self.assertIn("served manifest.json disagrees with the table on COMPARISON.md", out)

    def test_production_404_is_not_a_pass(self):
        with serve(self.tmp / "empty_does_not_exist") as base:
            old = cpv.PRODUCTION_URL
            cpv.PRODUCTION_URL = base + PREFIX
            try:
                code, out = check(base + PREFIX)
            finally:
                cpv.PRODUCTION_URL = old
        self.assertEqual(code, 3, out)
        self.assertIn("NOT_YET_PUBLISHED", out)
        self.assertNotIn("PASS", out.replace("This is not a pass", ""))

    def test_no_default_url(self):
        with self.assertRaises(SystemExit) as cm, contextlib.redirect_stderr(io.StringIO()):
            cpv.main([])
        self.assertEqual(cm.exception.code, 2)
        self.assertEqual(cpv.main(["ftp://x/"]), 2)

    def test_cross_host_redirect_refused(self):
        class R(_Quiet):
            def do_GET(self):
                self.send_response(302)
                self.send_header("Location", "http://localhost:1/x")
                self.end_headers()
        srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), R)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        try:
            st, _ = cpv.get("http://127.0.0.1:%d/a" % srv.server_address[1])
        finally:
            srv.shutdown()
            srv.server_close()
        self.assertEqual(st, 302)


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]], verbosity=1)
