from mem0 import MemoryClient
import os
from dotenv import load_dotenv

load_dotenv()

MEM0_API_KEY = os.getenv("MEM0_API_KEY")
if not MEM0_API_KEY:
    raise ValueError("MEM0_API_KEY not set")

client = MemoryClient(api_key=MEM0_API_KEY)

def save_message(username: str, role: str, content: str):
    try:
        client.add(
            messages=[{"role": role, "content": content}],
            user_id=username
        )
        print(f"Saved {role} message for {username}")
    except Exception as e:
        print(f"Error saving {role} message:", e)

def retrieve_user_memory(username: str) -> str:
    try:
        results = client.search(
            query=username,
            version="v2",
            filters={"user_id": username}
        )
        print("Raw results:", results)
        
        # Extract message content from 'memory' key
        context = "\n".join([res.get("memory", "") for res in results])
        print(f"Memory context for {username}:\n{context}")
        return context
    except Exception as e:
        print("Error fetching memory:", e)
        return ""
