import os
from dotenv import load_dotenv
from langchain.schema import HumanMessage
from pydantic import SecretStr
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Fetch the API key from the environment variable
gemini_api_key = SecretStr(os.environ["GEMINI_API_KEY"])
print("API Key",gemini_api_key)

# Initialize the ChatGoogleGenerativeAI model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=gemini_api_key
)

# Create a list of messages
messages = [HumanMessage(content="Write a song about green color")]

# Send a message and print the response using .invoke()
response = model.invoke(messages)
print(response.content)

# .env :- GEMINI_API_KEY=
