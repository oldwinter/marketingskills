import json
import pathlib
import subprocess
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".github" / "scripts" / "release-notes.py"


class ReleaseNotesTests(unittest.TestCase):
    def test_missing_version_is_an_error(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "test") as tmpdir:
            fixture = pathlib.Path(tmpdir)
            versions = fixture / "VERSIONS.md"
            versions.write_text("# Versions\n\n### 1.0.0 (2026-01-01)\n\n- First.\n", encoding="utf-8")
            result = subprocess.run(
                [
                    "python3",
                    str(SCRIPT),
                    "1.0.1",
                    "--versions-file",
                    str(versions),
                    "--notes-file",
                    str(fixture / "notes.md"),
                    "--title-file",
                    str(fixture / "title.txt"),
                ],
                text=True,
                capture_output=True,
                check=False,
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("no release notes for 1.0.1", result.stderr)

    def test_current_version_extracts_real_notes(self):
        version = json.loads(
            (ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
        )["version"]
        with tempfile.TemporaryDirectory(dir=ROOT / "test") as tmpdir:
            fixture = pathlib.Path(tmpdir)
            result = subprocess.run(
                [
                    "python3",
                    str(SCRIPT),
                    version,
                    "--versions-file",
                    str(ROOT / "VERSIONS.md"),
                    "--notes-file",
                    str(fixture / "notes.md"),
                    "--title-file",
                    str(fixture / "title.txt"),
                ],
                text=True,
                capture_output=True,
                check=False,
            )
            notes = (fixture / "notes.md").read_text(encoding="utf-8")
            title = (fixture / "title.txt").read_text(encoding="utf-8")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotEqual(notes.strip(), f"Release {version}")
        self.assertTrue(title.startswith(f"v{version} —"))


if __name__ == "__main__":
    unittest.main()
