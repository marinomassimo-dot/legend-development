"""Tests for dream_pass.py on synthetic repositories (declared synthetic, no real record)."""
import os
import subprocess
import sys
import tempfile
import unittest

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dream_pass.py")
ROOT = "mod/research"


def run(cwd, *args):
    return subprocess.run([sys.executable, SCRIPT, *args, "--root", ROOT], cwd=cwd, capture_output=True, text=True)


def git(cwd, *args):
    subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@example.invalid", *args], cwd=cwd, check=True, capture_output=True)


class Repo(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.d = self.tmp.name
        git(self.d, "init", "-q")

    def tearDown(self):
        self.tmp.cleanup()

    def put(self, rel, text):
        p = os.path.join(self.d, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(text)

    def commit(self, msg="c"):
        git(self.d, "add", "-A")
        git(self.d, "commit", "-q", "-m", msg)


class Controls(Repo):
    def test_co_occurrence_carries_no_sign(self):
        """Misleading association: two genes co-named in many files, one file denying the link."""
        for i in range(5):
            self.put(f"{ROOT}/n{i}.md", "GENEA and GENEB are discussed together.\n")
        self.put(f"{ROOT}/neg.md", "GENEA effect on GENEB was not shown in any neural cell.\n")
        self.commit()
        out = run(self.d, "pairs", "GENEA", "GENEB").stdout
        self.assertIn("carries no sign", out)
        self.assertIn("not shown in any neural cell", out)
        for word in ("consistent", "opposed", "activates", "inhibits", "up-regulates"):
            self.assertNotIn(word, out.replace("carries no sign", ""))

    def test_qualifier_columns_stay_attached(self):
        """Lost qualifier: the context and status columns of a table row reach the reader."""
        self.put(f"{ROOT}/b.tsv", "gene_a\trelation\tgene_b\tstatus\tcontext\nGENEA\tlowers\tGENEB\tobserved_other_context\tmuscle cells, knockdown only\n")
        self.commit()
        out = run(self.d, "pairs", "GENEA", "GENEB").stdout
        self.assertIn("header: gene_a\trelation\tgene_b\tstatus\tcontext", out)
        self.assertIn("observed_other_context\tmuscle cells, knockdown only", out)

    def test_consumed_result_reported_as_consumed(self):
        """Repeated work: a folder already cited from outside is shown as cited, an orphan as not."""
        self.put(f"{ROOT}/drug_repurposing/pkg_used/README.md", "result\n")
        self.put(f"{ROOT}/drug_repurposing/pkg_orphan/README.md", "result\n")
        self.put(f"{ROOT}/needs.md", "see pkg_used for the measurement\n")
        self.put(f"{ROOT}/drug_repurposing/x.txt", "x\n")
        self.commit()
        out = run(self.d, "consumers", "--since", "2000-01-01").stdout.splitlines()
        rows = {r.split("\t")[0].rsplit("/", 1)[-1]: r.split("\t") for r in out[1:] if "\t" in r}
        self.assertGreaterEqual(int(rows["pkg_used"][2]), 1)
        self.assertEqual(int(rows["pkg_orphan"][2]), 0)

    def test_removed_folder_is_not_listed(self):
        self.put(f"{ROOT}/drug_repurposing/gone/a.md", "x\n")
        self.commit("add")
        git(self.d, "rm", "-rq", f"{ROOT}/drug_repurposing/gone")
        self.commit("remove")
        out = run(self.d, "consumers", "--since", "2000-01-01").stdout
        self.assertNotIn("gone", out)


class Pointers(Repo):
    def test_draft_without_route_is_reported(self):
        self.put(f"{ROOT}/drug_repurposing/req_E-MTAB-1_draft.md", "# Draft: ask about E-MTAB-1 - NOT SENT\n\nbody E-MTAB-1\n")
        self.put(f"{ROOT}/log.md", "E-MTAB-1 returned 403.\n")
        self.put(f"{ROOT}/linked.md", "E-MTAB-1 403, see req_E-MTAB-1_draft.md\n")
        self.commit()
        out = run(self.d, "pointers").stdout
        self.assertIn("req_E-MTAB-1_draft.md\tE-MTAB-1\t", out)
        self.assertIn(f"{ROOT}/log.md", out)
        self.assertNotIn(f"{ROOT}/linked.md", out)

    def test_quiet_when_nothing_changed(self):
        self.put("other/a.md", "x\n")
        self.commit()
        out = run(self.d, "quiet", "--since", "HEAD").stdout
        self.assertTrue(out.startswith("quiet:"), out)


if __name__ == "__main__":
    unittest.main()
