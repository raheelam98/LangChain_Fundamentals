# check :-  import env variable to main.py
import os

#Load environment variables from .env file
load_dotenv()

if __name__ == '__main__':
    print("Hello Lang Chain")
  
    print(os.environ.get('OPENAI_API_KEY', 'OPENAI_API_KEY not set'))
