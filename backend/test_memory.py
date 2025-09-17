from memory import client

username = "testuser"

# Add messages
client.add(messages=[{"role": "user", "content": "I love pizza!"}], user_id=username)
client.add(messages=[{"role": "assistant", "content": "Pizza is amazing!"}], user_id=username)

# Retrieve messages
results = client.search(query=username, version="v2", filters={"user_id": username})
print("Raw results:", results)
print("Memory context:", "\n".join([res.get("content", "") for res in results]))
