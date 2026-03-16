import fitz
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Load Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)


def extract_text_from_pdf(uploaded_file):
    text = ""

    try:
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()

    except Exception as e:
        print(f"Error reading PDF: {e}")

    return text


def ask_ai(prompt, max_tokens=500):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )

    return response.choices[0].message.content