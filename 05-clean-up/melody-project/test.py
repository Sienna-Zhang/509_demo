import unittest
import tempfile
import os
import sys
from io import StringIO

from melody.io import load_melodies, save_melodies, parse_melody
from melody.model import build_bigrams


class TestMelodies(unittest.TestCase):
    def test_load_melodies_basic(self):
        with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as tmp:
            tmp.write("C4 D4 E4\n")
            tmp.write("A4 B4 C5\n")
            tmp_path = tmp.name

        try:
            melodies = load_melodies(tmp_path)
            self.assertEqual(melodies, [["C4", "D4", "E4"], ["A4", "B4", "C5"]])
        finally:
            os.remove(tmp_path)

    def test_save_and_load_roundtrip(self):
        original = [["C4:1", "D4:0.5"], ["A4", "B4"]]

        with tempfile.TemporaryDirectory() as tmpdir:
            out_file = os.path.join(tmpdir, "mel.txt")

            save_melodies(original, out_file)
            loaded = load_melodies(out_file)

        self.assertEqual(loaded, original)

    def test_load_file_not_found(self):
        path = "not_a_real_file_abc123.txt"

        captured = StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured

        try:
            result = load_melodies(path)
        finally:
            sys.stdout = sys_stdout_backup

        output = captured.getvalue()

        self.assertEqual(result, [])
        self.assertIn("File not found", output)
        self.assertIn("Please make sure the dataset file exists.", output)

    def test_build_bigrams_simple(self):
        # simple melody pair
        m1 = parse_melody("C D E")
        m2 = parse_melody("D E F")
        melodies = [["^"] + m1 + ["$"], ["^"] + m2 + ["$"]]
        model = build_bigrams(melodies)
        # check some expected transitions
        self.assertEqual(model['C']['D'], 1)
        self.assertEqual(model['D']['E'], 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
