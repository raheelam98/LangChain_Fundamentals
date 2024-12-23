# check :-  load env variable to main.py
import os
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

if __name__ == '__main__':
    print("hello LangChain")
    print(os.environ.get('GEMINI_API_KEY', 'GEMINI_API_KEY not set'))
