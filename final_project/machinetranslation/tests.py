import unittest
from translator import english_to_french, french_to_english

class testTranslatorMethods(unittest.TestCase):

    def test_french_to_english_null_input(self):
         self.assertNotEqual(english_to_french('None'), '   ')  

    def test_english_to_french_null_input(self):
        self.assertNotEqual(english_to_french('None'), '   ')  

    def test_english_to_french_hello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english_hello(self):
         self.assertEqual(french_to_english("Bonjour"), "Hello")


if __name__ == "__main__":
    unittest.main()