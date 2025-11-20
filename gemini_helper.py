import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Load API Key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY missing in .env")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Ask Gemini (Text-only)
def ask_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")  # Use whichever model you want
        response = model.generate_content(prompt)
        return (response.text or "").strip()

    except Exception as e:
        print("Gemini Error:", e)
        return "⚠️ Gemini API Error"

# For future image analysis
def analyze_with_gemini(image_path, question=""):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        with open(image_path, "rb") as img:
            response = model.generate_content(
                [question, img]
            )
        return response.text.strip()
    except Exception as e:
        print("Gemini Image Error:", e)
        return "⚠️ Image analysis failed"
