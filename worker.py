from queue import q
from ai import ask_ai
from messenger import send_message

def process_message(user_id, text):
    reply = ask_ai(text)
    send_message(user_id, reply)