
import streamlit as st

from ai_service import generate_with_gemini
from database import (
    create_table,
    save_message,
    get_messages,
    delete_message,
    delete_all_messages
)

st.set_page_config(
    page_title="WriteFlow | Message Studio",
    page_icon="✉️",
    layout="centered"
)

# ---------------- DATABASE ----------------

try:
    create_table()
except Exception as e:
    st.error(str(e))
    st.stop()


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 5%, #172554 0%, transparent 30%),
        radial-gradient(circle at 90% 80%, #312e81 0%, transparent 25%),
        #080e1c;
    color: #f8fafc;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, p, label {
    color: #f1f5f9 !important;
}

.hero {
    background: linear-gradient(120deg, #1e1b4b, #1d4ed8);
    padding: 34px;
    border-radius: 22px;
    border: 1px solid #475569;
    margin-bottom: 28px;
    box-shadow: 0 15px 40px rgba(37, 99, 235, 0.18);
}

.hero h1 {
    font-size: 38px;
    font-weight: 800;
    margin: 0;
    letter-spacing: -1.5px;
}

.hero p {
    color: #cbd5e1 !important;
    margin-top: 10px;
    font-size: 15px;
}

.tag {
    display: inline-block;
    background: rgba(255,255,255,0.12);
    color: #bfdbfe;
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 30px;
    padding: 6px 12px;
    font-size: 12px;
    margin-bottom: 15px;
}

.stTextInput input, .stTextArea textarea {
    background: #0f172a !important;
    color: white !important;
    border: 1px solid #334155 !important;
    border-radius: 11px !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background: #0f172a;
    border: 1px solid #334155;
    border-radius: 11px;
}

.stButton button {
    background: linear-gradient(90deg, #6366f1, #2563eb);
    color: white;
    border: none;
    border-radius: 12px;
    min-height: 48px;
    font-weight: 700;
}

.stButton button:hover {
    background: linear-gradient(90deg, #4f46e5, #1d4ed8);
    color: white;
}

.stDownloadButton button {
    background: #172554;
    color: #bfdbfe;
    border: 1px solid #3b82f6;
    border-radius: 11px;
    min-height: 45px;
}

hr {
    border-color: #29364d;
}

footer, #MainMenu {
    visibility: hidden;
}

.output-heading {
    background: #172554;
    padding: 15px 18px;
    border-radius: 12px;
    border-left: 4px solid #6366f1;
    margin-bottom: 15px;
}

.footer-text {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown("""
<div class="hero">
    <div class="tag">✦ YOUR PERSONAL MESSAGE STUDIO</div>
    <h1>✉️ WriteFlow</h1>
    <p>Create clear, professional and personalized emails and messages in one place.</p>
</div>
""", unsafe_allow_html=True)


# ---------------- INPUT FORM ----------------

st.markdown("### ✨ Create your message")

col1, col2 = st.columns(2)

with col1:
    content_type = st.selectbox(
        "📝 Content Type",
        ["Email", "WhatsApp Message", "SMS"]
    )

with col2:
    tone = st.selectbox(
        "🎯 Writing Tone",
        ["Professional", "Formal", "Friendly", "Casual"]
    )

# NEW: SENDER NAME

sender_name = st.text_input(
    "✍️ Your Name (Sender)",
    placeholder="e.g. Neeraj Kumar",
    max_chars=100
)

recipient = st.text_input(
    "👤 Recipient",
    placeholder="e.g. College Teacher",
    max_chars=100
)

subject = ""

if content_type == "Email":
    subject = st.text_input(
        "📌 Email Subject",
        placeholder="e.g. Leave Application",
        max_chars=150
    )

purpose = st.text_area(
    "💬 Message Requirements",
    placeholder="Explain what you want to communicate...",
    height=145,
    max_chars=2000
)

language = st.selectbox(
    "🌐 Output Language",
    ["English", "Hindi", "Hinglish"]
)

st.caption("Choose your preferred format, tone and language.")


# ---------------- GENERATE WITH GEMINI ----------------

if st.button("✨ Generate Message", use_container_width=True):

    if not sender_name.strip():
        st.warning("Please enter your name.")

    elif not recipient.strip():
        st.warning("Please enter the recipient.")

    elif not purpose.strip():
        st.warning("Please enter your message requirements.")

    elif content_type == "Email" and not subject.strip():
        st.warning("Please enter the email subject.")

    else:
        try:
            with st.spinner("Gemini is writing your message..."):

                result = generate_with_gemini(
                    sender_name.strip(),
                    recipient.strip(),
                    subject.strip(),
                    purpose.strip(),
                    tone,
                    content_type,
                    language
                )

                if not result or not result.strip():
                    raise RuntimeError("Gemini returned an empty message.")

                save_message(
                    recipient.strip(),
                    subject.strip(),
                    purpose.strip(),
                    tone,
                    content_type,
                    language,
                    result
                )

            st.session_state["generated_result"] = result

            st.session_state["output_version"] = (
                st.session_state.get("output_version", 0) + 1
            )

            st.success("Message generated successfully with Gemini AI!")

        except ValueError as e:
            st.warning(str(e))

        except Exception as e:
            st.error(f"Gemini API Error: {e}")


# ---------------- OUTPUT ----------------

if "generated_result" in st.session_state:

    st.markdown("---")

    st.markdown("""
    <div class="output-heading">
        <h3 style="margin:0;">📩 Your Generated Message</h3>
        <p style="margin:5px 0 0;color:#bfdbfe !important;font-size:13px;">
            Your message is ready. You can edit or download it.
        </p>
    </div>
    """, unsafe_allow_html=True)

    version = st.session_state.get("output_version", 0)

    edited_result = st.text_area(
        "Edit your message",
        value=st.session_state["generated_result"],
        height=280,
        key=f"editable_output_{version}"
    )

    st.download_button(
        "📥 Download message",
        data=edited_result,
        file_name="writeflow_message.txt",
        mime="text/plain",
        use_container_width=True
    )


# ---------------- MESSAGE HISTORY ----------------

st.markdown("---")
st.markdown("### 🕘 Message History")

try:
    messages = get_messages()

    if messages:

        if st.button("🗑️ Clear All History"):
            st.session_state["confirm_clear_history"] = True

        if st.session_state.get("confirm_clear_history", False):

            st.warning("Are you sure you want to delete all messages?")

            col1, col2 = st.columns(2)

            with col1:
                if st.button("Yes, Delete All"):
                    try:
                        delete_all_messages()
                        st.session_state["confirm_clear_history"] = False
                        st.success("All messages deleted!")
                        st.rerun()
                    except Exception as e:
                        st.error(str(e))

            with col2:
                if st.button("Cancel"):
                    st.session_state["confirm_clear_history"] = False
                    st.rerun()

        for message in messages:

            with st.expander(
                f"{message[1]} — {message[7][:35]}"
            ):

                st.write("Recipient:", message[1])
                st.write("Subject:", message[2])
                st.write("Type:", message[5])
                st.write("Language:", message[6])
                st.write("Created:", message[8])

                st.text_area(
                    "Saved Message",
                    value=message[7],
                    height=150,
                    key=f"history_{message[0]}"
                )

                if st.button(
                    "🗑️ Delete Message",
                    key=f"delete_{message[0]}"
                ):
                    try:
                        delete_message(message[0])
                        st.success("Message deleted successfully!")
                        st.rerun()
                    except Exception as e:
                        st.error(str(e))

    else:
        st.session_state["confirm_clear_history"] = False
        st.info("No saved messages yet.")

except Exception as e:
    st.error(f"History error: {e}")


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer-text">
    WriteFlow • Built with Python & Streamlit
    <br>
    Your words, your way.
</div>
""", unsafe_allow_html=True)
