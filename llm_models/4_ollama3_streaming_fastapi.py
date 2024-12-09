import asyncio
from typing import AsyncIterable
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain_ollama import ChatOllama  # Corrected import for Ollama
from langchain.schema import HumanMessage
from pydantic import BaseModel

load_dotenv()

app = FastAPI()

class Message(BaseModel):
    content: str

# Function to handle sending a message to Ollama 3
async def send_message(content: str) -> AsyncIterable[str]:
    callback = AsyncIteratorCallbackHandler()
    model = ChatOllama(
        model = "llama3",  # Use the specific Ollama 3 model name
        streaming=True,
        verbose=True,
        callbacks=[callback],
    )

    task = asyncio.create_task(
        model.agenerate(messages=[[HumanMessage(content=content)]])
    )

    try:
        # Yield tokens from the Ollama model
        async for token in callback.aiter():
            yield token
    except Exception as e:
        print(f"Caught exception: {e}")
    finally:
        callback.done.set()

    await task

@app.post("/stream_chat/")
async def stream_chat(message: Message):
    # Create a generator for the streaming response
    generator = send_message(message.content)
    return StreamingResponse(generator, media_type="text/event-stream")


# .env  ollama=

# to run poetry 
# poetry run uvicorn app.main:app --port 8005 --reload


