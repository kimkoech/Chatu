import tempfile
import unittest
from pathlib import Path

import chatu


class ChatuTranslationTests(unittest.TestCase):
    def test_translate_source_replaces_only_identifiers(self):
        mapping = {"kwa": "for", "katika": "in", "upana": "range", "na": "and"}
        source = 'kwa i katika upana(3):\n    chapisha("upana na kwa")\n'

        result = chatu.translate_source(source, mapping)

        self.assertIn("for i in range(3):", result)
        self.assertIn('chapisha("upana na kwa")', result)

    def test_compile_script_generates_python_file(self):
        with tempfile.TemporaryDirectory() as tempdir:
            td = Path(tempdir)
            script = td / "hello.ch"
            csv_file = td / "translations.csv"

            script.write_text('chapisha("Hujambo")\n', encoding="utf-8")
            csv_file.write_text('print, chapisha\n', encoding="utf-8")

            output = chatu.compile_script(script, csv_file)
            compiled_text = output.read_text(encoding="utf-8")

            self.assertTrue(output.exists())
            self.assertIn('print("Hujambo")', compiled_text)

    def test_main_returns_error_on_missing_script(self):
        exit_code = chatu.main(["missing.ch"])
        self.assertEqual(exit_code, 1)


if __name__ == "__main__":
    unittest.main()
