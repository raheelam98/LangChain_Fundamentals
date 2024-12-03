# basic prompt (hard coded text) but don't have real_time data

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

llm = ChatOpenAI(model="gpt-4o",temperature=0)
res = llm("Taj Mahal is in ____")
print(res)
# output :- content='The Taj Mahal is in Agra, India.'

res2 = llm("Karachi Weather")
print(res2)
# output :- content="I currently don't have real-time data access to provide the current weather conditions in Karachi

