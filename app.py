from flask import Flask, request
from config import VERIFY_TOKEN
from queue import q
from worker import process_message

app = Flask(_name_)

@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "error"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    for entry in data.get("entry", []):
        for event in entry.get("messaging", []):
            if "message" not in event:
                continue

            user_id = event["sender"]["id"]
            text = event["message"].get("text", "")

            # 👉 ไม่ประมวลผลตรงนี้
            q.enqueue(process_message, user_id, text)

    return "ok"

if _name_ == "_main_":
    app.run(port=5000)