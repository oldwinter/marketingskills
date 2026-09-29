import json
import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class RepositoryContractTests(unittest.TestCase):
    def test_agent_operations_use_this_fork(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

        self.assertIn("/plugin marketplace add oldwinter/marketingskills", agents)
        self.assertIn(
            "raw.githubusercontent.com/oldwinter/marketingskills/main/VERSIONS.md",
            agents,
        )
        self.assertNotIn("/plugin marketplace add coreyhaines31/marketingskills", agents)
        self.assertNotIn(
            "raw.githubusercontent.com/coreyhaines31/marketingskills/main/VERSIONS.md",
            agents,
        )
        self.assertIn("**Upstream**: [coreyhaines31/marketingskills]", agents)

    def test_agent_overview_does_not_hard_code_cli_count(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

        self.assertIsNone(re.search(r"clis/.*\(\d+ tools\)", agents))

    def test_current_release_has_notes_and_no_fallback(self):
        version = json.loads(
            (ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
        )["version"]
        versions = (ROOT / "VERSIONS.md").read_text(encoding="utf-8")
        workflow = (ROOT / ".github" / "workflows" / "release.yml").read_text(
            encoding="utf-8"
        )

        self.assertRegex(versions, rf"(?m)^### {re.escape(version)} \(")
        self.assertIn(".github/scripts/release-notes.py", workflow)
        self.assertNotIn("blocks.get", workflow)

    def test_skill_versions_match_versions_table(self):
        versions = (ROOT / "VERSIONS.md").read_text(encoding="utf-8")
        table = dict(
            re.findall(r"(?m)^\| ([a-z0-9-]+) \| ([0-9]+\.[0-9]+\.[0-9]+) \|", versions)
        )
        skill_dirs = sorted(path.name for path in (ROOT / "skills").iterdir() if path.is_dir())

        self.assertEqual(set(table), set(skill_dirs))
        for skill_name in skill_dirs:
            content = (ROOT / "skills" / skill_name / "SKILL.md").read_text(
                encoding="utf-8"
            )
            frontmatter = content.split("---", 2)[1]
            match = re.search(r"(?m)^  version: (\S+)$", frontmatter)
            self.assertIsNotNone(match, f"missing metadata.version for {skill_name}")
            self.assertEqual(table[skill_name], match.group(1), skill_name)


if __name__ == "__main__":
    unittest.main()
