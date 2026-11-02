# WriteFlow – AI Email & Message Writer

WriteFlow is an AI-powered application that helps users generate personalized emails, WhatsApp messages, and SMS using Google's Gemini API.

Users can select a writing tone, output language, recipient, and message purpose to generate ready-to-use content.

## Features

- **AI Message Generation:** Generate messages using Google Gemini.
- **Multiple Formats:** Email, WhatsApp Message, and SMS.
- **Multiple Tones:** Professional, Formal, Friendly, and Casual.
- **Multiple Languages:** English, Hindi, and Hinglish.
- **Personalization:** Add sender name and recipient details.
- **Editable Output:** Edit generated messages before using them.
- **Download:** Download generated messages as text files.
- **Message History:** Save and view previously generated messages.
- **Delete Options:** Delete individual messages or clear all history.
- **Database:** Store message history using SQLite.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | User interface |
| Google Gemini API | AI message generation |
| SQLite | Message history storage |
| python-dotenv | Environment variable management |
| google-genai | Gemini API integration |

## Project Structure

```text
AI_Email_Writer/
│
├── app.py
├── ai_service.py
├── ai_engine.py
├── prompts.py
├── database.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── writeflow.db
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI_Email_Writer
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API Key

Create a `.env` file in the project root directory.

Add:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace the placeholder with your own API key. Never publish your API key.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## How to Use

1. Open WriteFlow.
2. Enter your sender name.
3. Select the message type and writing tone.
4. Enter the recipient.
5. Add the email subject if applicable.
6. Describe your message requirements.
7. Select the output language.
8. Click Generate Message.
9. Edit or download the generated message.
10. Access previously generated messages through Message History.

## Database

WriteFlow uses SQLite to store generated messages, including recipient, subject, purpose, tone, content type, language, and generated content.

## Security

- API keys are stored in environment variables.
- The `.env` file should not be uploaded to GitHub.
- The local database may contain personal message content, so do not publish it.

## Future Improvements

- User registration and login.
- Saved sender profiles.
- More writing styles and languages.
- Email sending integration.
- Message templates.
- Deployment as a public web application.

## Author

**Neeraj Kumar Pandit**

Project: WriteFlow – AI Email & Message Writer

## License

This project is intended for educational and learning purposes.
