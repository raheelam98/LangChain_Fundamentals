from dotenv import load_dotenv
from langchain.schema import HumanMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_ollama import ChatOllama

# Load environment variables (if needed)
load_dotenv()

# Initialize ChatOllama with the required model and callback
chat = ChatOllama(model = "llama3",
      # Replace this with the model you want to use
    callbacks=[StreamingStdOutCallbackHandler()]
)

# Create a list of messages
messages = [HumanMessage(content="Write a song about sparkling water")]

# Send a message and print the response
response = chat(messages)
print(response.content)

# .env
# ollama=
