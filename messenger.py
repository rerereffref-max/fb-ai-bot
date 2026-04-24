import requests
from config import PAGE_ACCESS_TOKEN

def send_message(user_id, text):
    url = f"https://graph.facebook.com/v19.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"

    requests.post(url, json={
        "recipient": {"id": user_id},
        "message": {"text": text}
    }, timeout=5)