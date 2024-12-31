# check :-  load env variable to main.py
import os
from dotenv import load_dotenv

from pydantic import  SecretStr
from langchain_google_genai import ChatGoogleGenerativeAI

#Load environment variables from .env file
load_dotenv()

if __name__ == '__main__':
    print("hello LangChain")
    #print(os.environ.get('GEMINI_API_KEY', 'GEMINI_API_KEY not set'))
    # Fetch the API key from the environment variable
    gemini_api_key = SecretStr(os.environ["GEMINI_API_KEY"])
    
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY is not set. Please provide the API key in your environment.")
    
    print("API Key:", gemini_api_key)

    # Initialize the ChatGoogleGenerativeAI model
    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  # Specify the model
        api_key=gemini_api_key,  # Pass the API key      
    )
    
    print("Model initialized successfully")


## OUTPUT
# hello LangChain
# API Key: **********
# Model initialized successfully
# WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
# E0000 00:00:1735652446.211158  253161 init.cc:229] grpc_wait_for_shutdown_with_timeout() timed out.
