from dotenv import load_dotenv
from langchain.schema import HumanMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize ChatOpenAI with streaming and callbacks
chat = ChatOpenAI(
    streaming=True, 
    callbacks=[StreamingStdOutCallbackHandler()], 
    temperature=0
)

# Create a list of messages
messages = [HumanMessage(content="Write a song about sparkling water")]

# Send a message and print the response
response = chat(messages)
print(response.content)

# .env 
# OPENAI_API_KEY=
