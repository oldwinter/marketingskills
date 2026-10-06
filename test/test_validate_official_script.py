import os
import pathlib
import subprocess
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "validate-skills-official.sh"


class OfficialValidatorTests(unittest.TestCase):
    def test_nonzero_exit_is_failure_even_if_output_says_valid(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "test") as tmpdir:
            fixture = pathlib.Path(tmpdir)
            skill_dir = fixture / "skills" / "sample"
            ref_dir = fixture / "skills-ref"
            bin_dir = fixture / "bin"
            skill_dir.mkdir(parents=True)
            (ref_dir / ".venv" / "bin").mkdir(parents=True)
            bin_dir.mkdir()
            (skill_dir / "SKILL.md").write_text("---\nname: sample\n---\n", encoding="utf-8")
            (ref_dir / ".venv" / "bin" / "activate").write_text(
                f'export PATH="{bin_dir}:$PATH"\n', encoding="utf-8"
            )
            fake_validator = bin_dir / "skills-ref"
            fake_validator.write_text(
                "#!/usr/bin/env bash\necho 'Valid skill (partial output)'\nexit 1\n",
                encoding="utf-8",
            )
            fake_validator.chmod(0o755)
            env = os.environ.copy()
            env.update(
                {
                    "SKILLS_DIR": str(fixture / "skills"),
                    "SKILLS_REF_DIR": str(ref_dir),
                }
            )

            result = subprocess.run(
                ["bash", str(SCRIPT)],
                cwd=ROOT,
                env=env,
                text=True,
                capture_output=True,
                check=False,
            )

        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Failed: 1", result.stdout)
        self.assertIn("Valid skill (partial output)", result.stdout)


if __name__ == "__main__":
    unittest.main()
