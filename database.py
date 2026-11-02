
import sqlite3

DB_NAME = "writeflow.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    try:
        with get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipient TEXT NOT NULL,
                    subject TEXT,
                    purpose TEXT NOT NULL,
                    tone TEXT NOT NULL,
                    content_type TEXT NOT NULL,
                    language TEXT NOT NULL,
                    generated_message TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
    except sqlite3.Error as e:
        raise RuntimeError(f"Database initialization failed: {e}")


def save_message(
    recipient,
    subject,
    purpose,
    tone,
    content_type,
    language,
    generated_message
):
    try:
        with get_connection() as conn:
            conn.execute("""
                INSERT INTO messages (
                    recipient, subject, purpose, tone,
                    content_type, language, generated_message
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                recipient, subject, purpose, tone,
                content_type, language, generated_message
            ))
    except sqlite3.Error as e:
        raise RuntimeError(f"Could not save message: {e}")


def get_messages():
    try:
        with get_connection() as conn:
            cursor = conn.execute(
                "SELECT * FROM messages ORDER BY id DESC"
            )
            return cursor.fetchall()
    except sqlite3.Error as e:
        raise RuntimeError(f"Could not fetch messages: {e}")


def delete_message(message_id):
    try:
        with get_connection() as conn:
            conn.execute(
                "DELETE FROM messages WHERE id = ?",
                (message_id,)
            )
    except sqlite3.Error as e:
        raise RuntimeError(f"Could not delete message: {e}")


def delete_all_messages():
    try:
        with get_connection() as conn:
            conn.execute("DELETE FROM messages")
    except sqlite3.Error as e:
        raise RuntimeError(f"Could not clear history: {e}")
