from flask import request, jsonify

from app import app
from bot.chatbot import RebotClient
from bot.voice_client import VoiceClient
from config import SAY_HELLO

rebot = RebotClient()
voice = VoiceClient()


@app.route("/_ping")
def ping():
    return "PONG"


@app.route("/hook", methods=['POST'])
def web_hook():
    values = request.get_json()
    topic = values.get("topic")
    print(topic)

    if not topic:
        return jsonify({"stat": "ERROR", "message": "no topic"})
    elif topic != "conversation.user.replied" and topic != "conversation.user.created":
        return jsonify({"stat": "RETURN", "topic": topic})

    data = values.get("data")
    if not data:
        return jsonify({"stat": "ERROR", "message": "no data"})

    conversation_id = data.get("conversation_id")
    if not conversation_id:
        return jsonify({"stat": "ERROR", "message": "no conversation_id"})

    if topic == "conversation.user.created":
        voice.send_message_to_user(conversation_id, SAY_HELLO)
    messages = data.get("conversation_parts")
    if not messages:
        return jsonify({"stat": "ERROR", "message": "no conversation_parts"})
    message = messages[0]

    user_info = data.get("user", {})
    print(user_info, message)
    reply = rebot.get_message(user_info.get("contact_id"), message.get("body"))
    print(reply)
    result = voice.send_message_to_user(conversation_id, reply)

    if not result:
        return jsonify({"stat": "ERROR", "message": "Voice send message error"})

    return jsonify({"stat": "OK", "message": "thanks"})

