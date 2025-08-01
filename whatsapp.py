import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_whatsapp_message(number: str, message: str) -> str:
    instance_id = os.getenv("INSTANCE_ID")
    token = os.getenv("API_TOKEN")

    url = f"https://api.ultramsg.com/{instance_id}/messages/chat"
    payload = {"token": token, "to": number, "body": message}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return f"📤 Message sent to {number}"
    else:
        return f"❌ Failed: {response.text}"
