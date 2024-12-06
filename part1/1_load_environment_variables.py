# check :-  load env variable to main.py
import os
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

if __name__ == '__main__':
    print("hello LangChain") 
    print(os.environ.get('TEST', 'TEST not set'))

# output :- hello LangChain    abc12345


# .env  
# TEST=abc12345
