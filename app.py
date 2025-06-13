import streamlit as st
from llm_response import get_llm_response
import json

# Page configuration
st.set_page_config(page_title="🎓 Campus Assistant Chatbot", page_icon="🤖", layout="centered")

# Load suggested FAQs from JSON
with open("faq_data.json", "r") as f:
    faq_data = json.load(f)

suggested_questions = [q["question"] for q in faq_data[:5]]  # show top 5

# Custom CSS
st.markdown("""
    <style>
    .stChatMessage {
        font-size: 16px;
        padding: 10px;
        border-radius: 10px;
    }
    .user-message {
        background-color: #e0f7fa;
        text-align: right;
    }
    .bot-message {
        background-color: #f1f8e9;
        text-align: left;
    }
    .chat-container {
        padding: 20px;
        border-radius: 12px;
        background-color: #ffffff;
        margin-bottom: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📚 Campus HelpBot")
    st.markdown("Ask anything related to college life – library hours, exams, events, registration and more.")
    st.markdown("---")
    st.subheader("💡 Suggested Questions")
    for question in suggested_questions:
        if st.button(question):
            st.session_state["pending_question"] = question
            st.rerun()
    st.markdown("---")
    st.markdown("🔒 **Powered by LLaMA 3.3 + FAQ Data**")

# Title
st.title("🤖 iCloud Campus Chatbot")
st.markdown("Get answers to your campus-related queries instantly!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Set up prompt from input or suggested question
suggested = st.session_state.pop("pending_question", None) if "pending_question" in st.session_state else None
user_input = st.chat_input("Type your question here...", key="chatbox")
prompt = suggested or user_input

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Process new message
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = get_llm_response(prompt)
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

# Footer
st.markdown("""
---
<center style='font-size: 13px; color: gray'>
Built with ❤️ using Streamlit + Groq + JSON FAQ
</center>
""", unsafe_allow_html=True)
