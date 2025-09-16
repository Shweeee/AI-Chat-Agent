# backend/app/memory_client.py
import os
import requests

MEMORY_API_URL = os.getenv("MEMORY_API_URL")  # e.g., mem0 index search endpoint
MEMORY_API_KEY = os.getenv("MEMORY_API_KEY")

def get_relevant_memories(username: str, query: str, k: int = 4):
    """
    Query the memory service using the user's username and the current query (RAG).
    This is mem0-style: you would typically embed the query, then search by username-specific namespace.
    """
    if not MEMORY_API_URL:
        return []

    payload = {
        "namespace": username,
        "query": query,
        "top_k": k
    }
    headers = {"Authorization": f"Bearer {MEMORY_API_KEY}"}
    r = requests.post(f"{MEMORY_API_URL}/search", json=payload, headers=headers, timeout=10)
    r.raise_for_status()
    data = r.json()
    # expected: list of {text: "...", score: ..., metadata: {...}}
    return data.get("results", [])

def save_memory(username: str, text: str, meta: dict = None):
    """Save user message to memory under username namespace."""
    if not MEMORY_API_URL:
        return None
    payload = {
        "namespace": username,
        "items": [
            {"text": text, "metadata": meta or {}}
        ]
    }
    headers = {"Authorization": f"Bearer {MEMORY_API_KEY}"}
    r = requests.post(f"{MEMORY_API_URL}/upsert", json=payload, headers=headers, timeout=10)
    r.raise_for_status()
    return r.json()
