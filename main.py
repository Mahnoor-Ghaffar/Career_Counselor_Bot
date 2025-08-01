import os
import streamlit as st
from dotenv import load_dotenv
import requests
from career import suggest_careers
from whatsapp import send_whatsapp_message

load_dotenv()

st.set_page_config(page_title="Career Counselor Bot 💬")

st.title("🤖 Career Counselor Bot")
st.write("Salam beta! Apne interests neeche likho, main suggest karti hoon kya career best rahega.")

user_input = st.text_area("✍️ Aapke Interests:", height=100)

phone_number = st.text_input("📞 (Optional) WhatsApp Number (e.g., +923001234567):")

if st.button("🔍 Suggest Careers"):
    if not user_input.strip():
        st.warning("Please enter some interests.")
    else:
        with st.spinner("Soch rahi hoon... 💭"):
            # Suggest careers
            suggestions = suggest_careers(user_input)
            suggestion_text = "Aap ke liye ye career options suitable ho sakti hain:\n- " + "\n- ".join(suggestions)

            st.success(suggestion_text)

            if phone_number.strip():
                with st.spinner("WhatsApp pe message bhej rahi hoon..."):
                    result = send_whatsapp_message(phone_number.strip(), suggestion_text)
                    st.info(result)
