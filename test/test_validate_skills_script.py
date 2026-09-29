import pathlib
import subprocess
import tempfile
import textwrap
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "validate-skills.sh"


def run_validator(
    skill_name: str, content: str | None = None
) -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory(dir=ROOT / "test") as tmpdir:
        worktree = pathlib.Path(tmpdir)
        skill_dir = worktree / "skills" / skill_name
        skill_dir.mkdir(parents=True)
        if content is None:
            content = textwrap.dedent(
                f"""\
                ---
                name: {skill_name}
                description: Use when auditing a page; for signup flows, see signup.
                ---

                # Fixture
                """
            )
        (skill_dir / "SKILL.md").write_text(
            content,
            encoding="utf-8",
        )
        return subprocess.run(
            ["bash", str(VALIDATOR)],
            cwd=worktree,
            text=True,
            capture_output=True,
            check=False,
        )


class ValidateSkillsNameTests(unittest.TestCase):
    def test_rejects_consecutive_hyphens(self):
        result = run_validator("page--cro")

        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("consecutive hyphens", result.stdout)

    def test_accepts_single_hyphen(self):
        result = run_validator("page-cro")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rejects_preamble_before_frontmatter(self):
        result = run_validator(
            "preamble",
            "intro\n---\nname: preamble\ndescription: Use when auditing; for signup, see signup.\n---\n",
        )

        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("malformed YAML frontmatter", result.stdout)

    def test_rejects_unterminated_frontmatter(self):
        result = run_validator(
            "unterminated",
            "---\nname: unterminated\ndescription: Use when auditing; for signup, see signup.\n",
        )

        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("malformed YAML frontmatter", result.stdout)

    def test_rejects_top_level_version(self):
        result = run_validator(
            "top-version",
            "---\nname: top-version\ndescription: Use when auditing; for signup, see signup.\nversion: 1.0.0\n---\n",
        )

        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("'version' is top-level", result.stdout)

    def test_accepts_metadata_version(self):
        result = run_validator(
            "nested-version",
            "---\nname: nested-version\ndescription: Use when auditing; for signup, see signup.\nmetadata:\n  version: 1.0.0\n---\n",
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
