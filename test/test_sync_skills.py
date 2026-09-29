import json
import pathlib
import subprocess
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".github" / "scripts" / "sync-skills.js"


def run_sync(skill_bytes: bytes, readme: str) -> tuple[subprocess.CompletedProcess[str], str]:
    with tempfile.TemporaryDirectory(dir=ROOT / "test") as tmpdir:
        fixture = pathlib.Path(tmpdir)
        (fixture / "skills" / "fixture").mkdir(parents=True)
        (fixture / ".claude-plugin").mkdir()
        (fixture / "skills" / "fixture" / "SKILL.md").write_bytes(skill_bytes)
        (fixture / "README.md").write_text(readme, encoding="utf-8")
        (fixture / ".claude-plugin" / "marketplace.json").write_text(
            json.dumps(
                {
                    "metadata": {"version": "1.0.0"},
                    "plugins": [{"description": "1 marketing skills"}],
                }
            ),
            encoding="utf-8",
        )
        (fixture / ".claude-plugin" / "plugin.json").write_text(
            json.dumps({"version": "1.0.0"}), encoding="utf-8"
        )
        result = subprocess.run(
            ["node", str(SCRIPT)],
            cwd=fixture,
            text=True,
            capture_output=True,
            check=False,
        )
        return result, (fixture / "README.md").read_text(encoding="utf-8")


class SyncSkillsTests(unittest.TestCase):
    def test_parses_crlf_frontmatter(self):
        result, readme = run_sync(
            b"---\r\nname: crlf-name\r\ndescription: CRLF description survives generation.\r\n---\r\n",
            "<!-- SKILLS:START -->\nold\n<!-- SKILLS:END -->\n",
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("[crlf-name](skills/fixture/)", readme)
        self.assertIn("CRLF description survives generation.", readme)

    def test_missing_readme_markers_is_an_error(self):
        result, _ = run_sync(
            b"---\nname: fixture\ndescription: Marker fixture.\n---\n",
            "# README without generated markers\n",
        )

        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Could not find skill markers", result.stderr)

    def test_valid_unchanged_markers_are_a_successful_noop(self):
        result, _ = run_sync(
            b"---\nname: fixture\ndescription: Marker fixture.\n---\n",
            "<!-- SKILLS:START -->\n| Skill | Description |\n|-------|-------------|\n| [fixture](skills/fixture/) | Marker fixture. |\n<!-- SKILLS:END -->\n",
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Everything is already in sync", result.stdout)


if __name__ == "__main__":
    unittest.main()
