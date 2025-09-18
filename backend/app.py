from fastapi import FastAPI
from pydantic import BaseModel
from memory import retrieve_user_memory, save_message
from llm import generate_ai_reply
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



@app.get("/")
def root():
    return {"message": "AI Chat Backend is running 🚀"}


# CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

class MessageRequest(BaseModel):
    username: str
    message: str

@app.post("/message")
async def handle_message(req: MessageRequest):
    username = req.username
    user_message = req.message

    # 1️⃣ Save user message to Mem0
    save_message(username, "user", user_message)

    # 2️⃣ Retrieve memory context for this user
    memory_context = retrieve_user_memory(username)

    # 3️⃣ Generate AI reply using Groq LLM
    ai_reply = generate_ai_reply(memory_context, user_message)

    # 4️⃣ Save AI reply to Mem0
    save_message(username, "assistant", ai_reply)

    # 5️⃣ Return AI reply to frontend
    return {"reply": ai_reply}
