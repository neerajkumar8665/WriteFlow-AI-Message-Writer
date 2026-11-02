
import unittest
from ai_engine import generate_ai_message


class TestAIEmailWriter(unittest.TestCase):

    def test_english_email(self):
        result = generate_ai_message(
            "College Teacher",
            "Leave",
            "I am suffering from fever.",
            "Professional",
            "Email",
            "English"
        )

        self.assertIn("Subject: Leave", result)
        self.assertIn("Dear College Teacher", result)

    def test_hindi_email(self):
        result = generate_ai_message(
            "College Teacher",
            "Leave",
            "Mujhe bukhar hai.",
            "Formal",
            "Email",
            "Hindi"
        )

        self.assertIn("आदरणीय", result)

    def test_hinglish_email(self):
        result = generate_ai_message(
            "College Teacher",
            "Leave",
            "Mujhe fever hai.",
            "Professional",
            "Email",
            "Hinglish"
        )

        self.assertIn("Namaste", result)

    def test_whatsapp(self):
        result = generate_ai_message(
            "Friend",
            "",
            "I will come tomorrow.",
            "Friendly",
            "WhatsApp Message",
            "English"
        )

        self.assertIn("Hello Friend", result)

    def test_sms(self):
        result = generate_ai_message(
            "Teacher",
            "",
            "I am absent today.",
            "Casual",
            "SMS",
            "English"
        )

        self.assertIn("I am absent today.", result)

    def test_empty_recipient(self):
        with self.assertRaises(ValueError):
            generate_ai_message(
                "", "Leave", "Fever",
                "Formal", "Email", "English"
            )


if __name__ == "__main__":
    unittest.main()
