import os
import requests
from dotenv import load_dotenv 
import json
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not set")

def generate_ai_reply(memory_context: str, user_message: str) -> str:
    """
    memory_context: previous messages from Mem0
    user_message: current user message
    """

    try:
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        conversation = []

        # Clean memory context: only include valid user/assistant lines
        if memory_context:
            for line in memory_context.split("\n"):
                line = line.strip()
                if not line:
                    continue
                if line.lower().startswith("user:"):
                    conversation.append({"role": "user", "content": line[5:].strip()})
                elif line.lower().startswith("assistant:"):
                    conversation.append({"role": "assistant", "content": line[10:].strip()})
                else:
                    # If format unknown, treat as user message
                    conversation.append({"role": "user", "content": line})

        # Add current user message
        conversation.append({"role": "user", "content": user_message})

        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": conversation,
            "temperature": 0.7,
            "max_tokens": 200
        }

        print("Payload sent to Groq API:", json.dumps(payload, indent=2))  # DEBUG

        res = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=15
        )
        res.raise_for_status()
        result = res.json()
        return result["choices"][0]["message"]["content"]

    except Exception as e:
        print("Error calling Groq API:", e)
        return "Sorry, I couldn't generate a response."
