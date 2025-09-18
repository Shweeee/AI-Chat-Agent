# AI Chat Agent

A real-time AI chat agent with memory support, built with FastAPI, LiveKit, and mem0. 
The agent can recall past conversations and respond contextually.

## Features
- Real-time chat using LiveKit
- Memory-enhanced responses with mem0
- Supports multiple LLM providers (OpenAI, Groq, OpenRouter)
- Dockerized backend for easy deployment
- Minimal frontend chat UI (Next.js optional)

## Tech Stack
- Backend: Python, FastAPI
- Memory: mem0
- Real-Time Communication: LiveKit
- LLM: Groq
- Containerization: Docker
- Environment Management: python-dotenv
- Data Handling: pydantic
- HTTP Requests: requests

## Setup
### Clone the repository
```bash
git clone https://github.com/Shweeee/AI-Chat-Agent.git
cd AI-Chat-Agent/backend


```markdown
### Configure environment variables
Create a `.env` file with:

MEM0_API_KEY=<your_mem0_api_key>
LIVEKIT_API_KEY=<your_livekit_api_key>
LIVEKIT_API_SECRET=<your_livekit_api_secret>
LLM_API_KEY=<your_llm_api_key>
GROQ_API_KEY=<your_groq_api_key>

```

### Build and run backend with Docker
```bash
docker build -t ai-chat-backend .
docker run --env-file .env -p 8000:8000 ai-chat-backend

```

```markdown
## API

### POST /message
Send a message to the AI agent.

Request Body:
{
  "username": "string",
  "message": "string"
}

Response:
"AI response message"

```
## Frontend (Optional)
If using the Next.js chat UI:

cd ../frontend
npm install
npm run dev

Open http://localhost:3000 to start chatting.

## Docker Notes
- .env is ignored in Git
- Always provide environment variables using --env-file

## Author
Swetha M. – Full Stack Developer



