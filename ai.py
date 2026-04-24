import requests
from config import OPENAI_API_KEY

def ask_ai(message):
    url = "https://api.openai.com/v1/chat/completions"

    for _ in range(3):  # retry 3 ครั้ง
        try:
            r = requests.post(
                url,
                headers={
                    "Authorization": f"Bearer {OPENAI_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-4o-mini",
                    "messages": [
                        {"role": "system", "content": "ตอบกวนๆ ฉลาดๆ สั้น"},
                        {"role": "user", "content": message}
                    ]
                },
                timeout=10
            )

            return r.json()["choices"][0]["message"]["content"]

        except:
            continue

    return "กูคิดไม่ออกว่ะ ลองใหม่ดิ 😅"