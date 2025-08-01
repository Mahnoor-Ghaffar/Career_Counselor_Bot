import google.generativeai as genai
import streamlit as st

# Gemini API key from Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Correct model name for free tier users
model = genai.GenerativeModel("gemini-1.5-flash")
# ✅ Use correct model name

def suggest_careers(interests: str) -> list[str]:
    prompt = f"""
You are a career counselor AI.
User's interests: {interests}
Suggest 3 suitable career options in bullet points. Be specific and helpful.
"""

    try:
        response = model.generate_content(prompt)
        careers = response.text.strip().split("\n")
        careers = [c.lstrip("-• ").strip() for c in careers if c.strip()]
        return careers
    except Exception as e:
        return [f"Error from Gemini: {str(e)}"]
