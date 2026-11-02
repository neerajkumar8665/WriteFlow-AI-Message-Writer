
import unittest
from ai_service import generate_with_ai


class TestAIService(unittest.TestCase):

    def test_prompt_generation(self):
        result = generate_with_ai(
            "Manager",
            "Leave Request",
            "Request leave for two days",
            "Professional",
            "Email",
            "English"
        )
        self.assertIsInstance(result, str)
        self.assertIn("Manager", result)
        self.assertIn("Leave Request", result)

    def test_empty_recipient(self):
        with self.assertRaises(ValueError):
            generate_with_ai(
                "", "Leave Request", "Request leave",
                "Professional", "Email", "English"
            )

    def test_empty_purpose(self):
        with self.assertRaises(ValueError):
            generate_with_ai(
                "Manager", "Leave Request", "",
                "Professional", "Email", "English"
            )

    def test_empty_subject(self):
        with self.assertRaises(ValueError):
            generate_with_ai(
                "Manager", "", "Request leave",
                "Professional", "Email", "English"
            )

    def test_invalid_content_type(self):
        with self.assertRaises(ValueError):
            generate_with_ai(
                "Manager", "Hello", "Send a message",
                "Professional", "Invalid", "English"
            )

    def test_invalid_tone(self):
        with self.assertRaises(ValueError):
            generate_with_ai(
                "Manager", "Hello", "Send a message",
                "Invalid", "Email", "English"
            )

    def test_invalid_language(self):
        with self.assertRaises(ValueError):
            generate_with_ai(
                "Manager", "Hello", "Send a message",
                "Professional", "Email", "Invalid"
            )


if __name__ == "__main__":
    unittest.main()
