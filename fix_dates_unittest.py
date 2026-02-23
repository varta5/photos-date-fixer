import unittest

from fix_dates import get_file_extension

class TestFixDates(unittest.TestCase):

    def test_get_file_extension(self):
        self.assertEqual(get_file_extension("example.txt"), "txt")
        self.assertEqual(get_file_extension("another.example.txt"), "txt")
        self.assertEqual(get_file_extension("example.jpg"), "jpg")
        self.assertEqual(get_file_extension("example.jpeg"), "jpeg")
        self.assertEqual(get_file_extension("Corrert filename 2026.02.23.jpg"), "jpg")
        self.assertEqual(get_file_extension("example"), "")
        self.assertEqual(get_file_extension(""), "")
        self.assertEqual(get_file_extension("."), "")
        self.assertEqual(get_file_extension(".gitignore"), "")
        self.assertEqual(get_file_extension("This is a sentence."), "")
        self.assertEqual(get_file_extension("Incorrert filename 2026.02.23."), "")

if __name__ == "__main__":
    unittest.main()
