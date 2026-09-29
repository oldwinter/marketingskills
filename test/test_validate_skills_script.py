import pathlib
import subprocess
import tempfile
import textwrap
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "validate-skills.sh"


def run_validator(skill_name: str) -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory() as tmpdir:
        worktree = pathlib.Path(tmpdir)
        skill_dir = worktree / "skills" / skill_name
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            textwrap.dedent(
                f"""\
                ---
                name: {skill_name}
                description: Use when auditing a page; for signup flows, see signup.
                ---

                # Fixture
                """
            ),
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


if __name__ == "__main__":
    unittest.main()
