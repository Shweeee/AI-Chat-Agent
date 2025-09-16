# backend/app/livekit_client.py
import os
import requests

LIVEKIT_URL = os.getenv("LIVEKIT_URL")
LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")

def send_message_to_room(room: str, sender: str, text: str):
    """
    Placeholder implementation. For production, use LiveKit Server SDK (python) to broadcast a data message.
    If you don't have the server SDK handy, you can implement a helper that the frontend polls.
    """
    # Example: POST to your own webhook/relay that frontend polls.
    # For now, just print (or implement a REST -> LiveKit SDK call).
    print(f"[LiveKit] room={room} sender={sender} text={text}")
    return True
