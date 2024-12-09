import asyncio
from typing import AsyncIterable
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain_community.chat_models import ChatOpenAI  # Corrected import
from langchain.schema import HumanMessage
from pydantic import BaseModel

load_dotenv()

app = FastAPI()

class Message(BaseModel):
    content: str

async def send_message(content: str) -> AsyncIterable[str]:
    callback = AsyncIteratorCallbackHandler()
    model = ChatOpenAI(
        streaming=True,
        verbose=True,
        callbacks=[callback],
    )

    task = asyncio.create_task(
        model.agenerate(messages=[[HumanMessage(content=content)]])
    )

    try:
        async for token in callback.aiter():
            yield token
    except Exception as e:
        print(f"Caught exception: {e}")
    finally:
        callback.done.set()

    await task

@app.post("/stream_chat/")
async def stream_chat(message: Message):
    generator = send_message(message.content)
    return StreamingResponse(generator, media_type="text/event-stream")


## request body :- {"content": "write short pome hot spring"}
## response body :- Steam rising high  Hot spring's embrace, healing touch  Nature's warm caress

# .env  OPENAI_API_KEY=

# to run poetry 
# poetry run uvicorn app.main:app --port 6677 --reload








 









