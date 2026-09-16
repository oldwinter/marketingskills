import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONTRIBUTING = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
ISSUE_CONFIG = (ROOT / ".github/ISSUE_TEMPLATE/config.yml").read_text(encoding="utf-8")
FORK = "https://github.com/oldwinter/marketingskills"
UPSTREAM_HOST = "https://github.com/coreyhaines31/marketingskills"
PR_TEMPLATES = ("new-skill.md", "skill-update.md", "documentation.md")


class ContributingLinkTests(unittest.TestCase):
    def test_skill_request_opens_this_fork(self):
        self.assertIn(
            f"{FORK}/issues/new?template=skill-request.yml",
            CONTRIBUTING,
        )
        self.assertNotIn(f"{UPSTREAM_HOST}/issues/new", CONTRIBUTING)

    def test_open_issue_has_this_fork_url(self):
        self.assertIn(f"[Open an issue]({FORK}/issues)", CONTRIBUTING)

    def test_pr_templates_use_compare_quick_pull(self):
        self.assertNotRegex(CONTRIBUTING, r"\]\(\?template=")
        for name in PR_TEMPLATES:
            self.assertIn(
                f"{FORK}/compare?quick_pull=1&template={name}",
                CONTRIBUTING,
            )
            self.assertTrue(
                (ROOT / ".github/PULL_REQUEST_TEMPLATE" / name).is_file(),
                f"missing PR template {name}",
            )

    def test_new_issue_contact_stays_on_this_fork(self):
        self.assertIn(f"{FORK}/blob/main/CONTRIBUTING.md", ISSUE_CONFIG)
        self.assertNotIn(UPSTREAM_HOST, ISSUE_CONFIG)
        self.assertTrue((ROOT / ".github/ISSUE_TEMPLATE/skill-request.yml").is_file())
        self.assertTrue((ROOT / "CONTRIBUTING.md").is_file())

    def test_contributing_does_not_send_people_upstream(self):
        self.assertIsNone(re.search(r"coreyhaines31/marketingskills", CONTRIBUTING))


if __name__ == "__main__":
    unittest.main()
