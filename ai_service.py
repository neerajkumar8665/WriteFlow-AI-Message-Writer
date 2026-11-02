
import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()


def generate_with_gemini(
    sender_name,
    recipient,
    subject,
    purpose,
    tone,
    content_type,
    language
):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "Gemini API key missing. Check your .env file."
        )

    prompt = f"""
Write a short, natural and ready-to-use message.

Sender: {sender_name}
Recipient: {recipient}
Subject: {subject}
Purpose: {purpose}
Tone: {tone}
Type: {content_type}
Language: {language}

Rules:
- Follow the requested language and tone.
- Do not invent personal details.
- For email, include a subject and greeting.
- For WhatsApp and SMS, keep it concise.
- End with the sender name: {sender_name}
- Return only the final message.
"""

    try:
        client = genai.Client(api_key=api_key)

        start_time = time.perf_counter()

        response = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt,
            generation_config={
                "thinking_level": "minimal"
            }
        )

        elapsed = time.perf_counter() - start_time

        result = response.output_text

        if not result or not result.strip():
            raise RuntimeError("Gemini returned an empty response.")

        print(f"Gemini response time: {elapsed:.2f} seconds")

        return result.strip()

    except Exception as e:
        raise RuntimeError(
            f"Gemini generation failed: {e}"
        ) from e
