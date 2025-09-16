# backend/app/llm_client.py
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_reply(prompt_data: dict, model: str = "gpt-4o-mini"):
    system = prompt_data["system"]
    memory_snippets = prompt_data.get("memory_snippets", "")
    user_text = prompt_data["user_text"]
    username = prompt_data["username"]

    messages = [
        {"role": "system", "content": system},
    ]
    if memory_snippets:
        messages.append({"role": "system", "content": f"Memory for {username}:\n{memory_snippets}"})
    messages.append({"role": "user", "content": user_text})

    resp = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.2,
        max_tokens=400,
    )
    text = resp["choices"][0]["message"]["content"].strip()
    return text
