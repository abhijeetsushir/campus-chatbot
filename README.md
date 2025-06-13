# 📚 Campus Chatbot (Streamlit + Groq LLaMA 3)

A smart campus assistant chatbot built using Streamlit and Groq’s LLaMA 3 model. It answers frequently asked student queries (e.g., about library, exams, ID cards) from a structured FAQ dataset and intelligently handles other academic questions using LLM.

## 🚀 Features

- 🧠 Powered by Groq’s LLaMA 3 (70B) model
- 💡 Built-in campus FAQ knowledge from JSON
- 💬 Natural language response generation
- 🎯 Suggestive question buttons for better UX
- ⚡ Clean, responsive Streamlit UI

## 📁 Project Structure
📦 icloud_campusCHATbot
├── app.py # Streamlit UI code
├── llm_response.py # Logic to fetch replies from JSON or Groq LLM
├── faq_data.json # Preloaded campus FAQs
├── .env # Stores your GROQ_API_KEY (not tracked in Git)
├── .gitignore
└── requirements.txt # Python dependencies
