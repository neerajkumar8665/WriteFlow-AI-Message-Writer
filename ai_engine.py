
def generate_ai_message(
    recipient,
    subject,
    purpose,
    tone,
    content_type,
    language
):
    recipient = recipient.strip()
    subject = subject.strip()
    purpose = purpose.strip()

    if not recipient:
        raise ValueError("Recipient cannot be empty.")

    if not purpose:
        raise ValueError("Message requirements cannot be empty.")

    if len(recipient) > 100:
        raise ValueError("Recipient name is too long.")

    if len(purpose) > 2000:
        raise ValueError("Message requirements cannot exceed 2000 characters.")

    if content_type not in ["Email", "WhatsApp Message", "SMS"]:
        raise ValueError("Invalid content type.")

    if language not in ["English", "Hindi", "Hinglish"]:
        raise ValueError("Invalid language.")

    if tone not in ["Professional", "Formal", "Friendly", "Casual"]:
        raise ValueError("Invalid writing tone.")

    if content_type == "Email" and not subject:
        raise ValueError("Email subject cannot be empty.")

    templates = {
        "Hindi": {
            "Formal": (
                f"आदरणीय {recipient} जी,",
                "आपके विचारार्थ धन्यवाद।\n\nसादर,\nआपका नाम"
            ),
            "Professional": (
                f"नमस्कार {recipient} जी,",
                "आपकी समझ और सहयोग के लिए धन्यवाद।\n\nसादर,\nआपका नाम"
            ),
            "Friendly": (
                f"नमस्ते {recipient} जी,",
                "आपका बहुत-बहुत धन्यवाद!"
            ),
            "Casual": (
                f"हेलो {recipient}!",
                "धन्यवाद!"
            )
        },
        "Hinglish": {
            "Formal": (
                f"Adarniya {recipient} ji,",
                "Aapke sahyog ke liye dhanyavaad.\n\nSadar,\nAapka naam"
            ),
            "Professional": (
                f"Namaste {recipient} ji,",
                "Aapki samajh aur sahyog ke liye dhanyavaad.\n\nRegards,\nAapka naam"
            ),
            "Friendly": (
                f"Hello {recipient} ji,",
                "Bahut bahut dhanyavaad!"
            ),
            "Casual": (
                f"Hi {recipient}!",
                "Thanks!"
            )
        },
        "English": {
            "Formal": (
                f"Respected {recipient},",
                "Thank you for your consideration.\n\nYours sincerely,\nYour Name"
            ),
            "Professional": (
                f"Dear {recipient},",
                "Thank you for your understanding and support.\n\nRegards,\nYour Name"
            ),
            "Friendly": (
                f"Hello {recipient},",
                "Thank you so much!\n\nBest regards,\nYour Name"
            ),
            "Casual": (
                f"Hi {recipient}!",
                "Thanks!"
            )
        }
    }

    greeting, closing = templates[language][tone]

    if content_type == "SMS":
        return f"{greeting}\n\n{purpose}\n\n{closing.splitlines()[0]}"

    if content_type == "Email":
        subject_label = "विषय" if language == "Hindi" else "Subject"

        return (
            f"{subject_label}: {subject}\n\n"
            f"{greeting}\n\n"
            f"{purpose}\n\n"
            f"{closing}"
        )

    if content_type == "WhatsApp Message":
        return f"{greeting}\n\n{purpose}\n\n{closing}"
