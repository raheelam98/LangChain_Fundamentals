# check :-  load env variable to main.py
import os
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

if __name__ == '__main__':
    print("hello LangChain")
    print(os.environ.get('TEST_API_KEY', 'TEST_API_KEY not set'))

# output :- hello LangChain    abc12345


# .env  
# TEST_API_KEY=abc12345

