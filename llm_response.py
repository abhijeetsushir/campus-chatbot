import os
import json
from groq import Groq
from dotenv import load_dotenv
from difflib import get_close_matches

# Load environment variables
load_dotenv()

# Load the FAQ data once
with open("faq_data.json", "r", encoding="utf-8") as f:
    faq_data = json.load(f)

# Setup Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))



def get_llm_response(prompt):
    prompt_lower = prompt.lower().strip()

    # Extract all questions from faq
    questions = [item["question"].lower() for item in faq_data]

    # Use fuzzy matching to find the best match
    match = get_close_matches(prompt_lower, questions, n=1, cutoff=0.6)

    if match:
        for item in faq_data:
            if item["question"].lower() == match[0]:
                print("🔹 Answer from FAQ")
                return item["answer"]

    # If no good match found, fall back to LLM
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful campus assistant. Answer clearly and informatively "
                "about college-related queries like library, exams, registration, ID cards, events, etc."
            ),
        },
        {"role": "user", "content": prompt},
    ]

    try:
        chat_completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=messages,
        )
        print("⚙️ Answer from LLM")
        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"⚠️ Sorry, I couldn't fetch the response from the model. Error: {str(e)}"
