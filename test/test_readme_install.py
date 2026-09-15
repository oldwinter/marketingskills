import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")


class ReadmeInstallTests(unittest.TestCase):
    def test_english_install_uses_this_fork(self):
        install = README.split("## Installation", 1)[1].split("## Upgrading from v1.x to v2.0", 1)[0]
        self.assertIn("npx skills add oldwinter/marketingskills", install)
        self.assertIn("/plugin marketplace add oldwinter/marketingskills", install)
        self.assertIn("https://github.com/oldwinter/marketingskills.git", install)
        self.assertNotIn("npx skills add coreyhaines31/marketingskills", install)
        self.assertNotIn("/plugin marketplace add coreyhaines31/marketingskills", install)
        self.assertNotIn("npx skillkit install coreyhaines31/marketingskills", install)

    def test_open_issue_points_at_this_fork(self):
        self.assertIn("https://github.com/oldwinter/marketingskills/issues", README)
        self.assertNotIn("https://github.com/coreyhaines31/marketingskills/issues", README)

    def test_upstream_stays_attribution(self):
        self.assertTrue(re.search(r"coreyhaines31/marketingskills", README))


if __name__ == "__main__":
    unittest.main()
