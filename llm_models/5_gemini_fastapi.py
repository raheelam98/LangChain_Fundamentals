import os
from fastapi import FastAPI
from pydantic import BaseModel, SecretStr
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

from dotenv import load_dotenv

# Load environment variables (if needed)
load_dotenv()

# Create a FastAPI app
app = FastAPI()

# Define the message model that will be used to parse the incoming request body
class Message(BaseModel):
    content: str

# Function to process the message with ChatGoogleGenerativeAI and return the response
async def send_message(content: str) -> dict:
    # Fetch the API key from the environment variable
    gemini_api_key = SecretStr(os.environ["GEMINI_API_KEY"])
    
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY is not set. Please provide the API key in your environment.")

    # Initialize the ChatGoogleGenerativeAI model
    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  # Specify the model
        api_key=gemini_api_key,  # Pass the API key      
    )

    try:
        # Generate a response using the provided content
        # Generate a response using the provided content
        result = await model.agenerate(messages=[[HumanMessage(content=content)]])

        # Extract the text from the generations attribute
        # Generate a response using the provided content
        result = await model.agenerate(messages=[[HumanMessage(content=content)]])

        # Extract the text from the generations attribute
        if hasattr(result, "generations"):
            for generation_list in result.generations:
                for generation in generation_list:
                    if hasattr(generation, "text"):
                        return {"response": generation.text}
                    
        # Fallback if no text is found
        return {"response": "No response text found."}

        # # Extract only the generated text (poem or response content)
        # if result and "generations" in result:
        #     response_text = result["generations"][-1][-1]["text"]
        # else:
        #     response_text = "No response generated."

        # # Return only the response text (poem or context)
        # return response_text
    

    except Exception as e:
        return {"error": str(e)}

# POST endpoint to handle incoming requests and get a response from the model
@app.post("/chat/")
async def chat(message: Message):
    try:
        # Send the message content to the model and await the result
        result = await send_message(message.content)
        return result
    except Exception as e:
        return {"error":str(e)}



# import os
# from fastapi import FastAPI
# from pydantic import BaseModel
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.schema import HumanMessage

# from dotenv import load_dotenv

# # Load environment variables (if needed)
# load_dotenv()

# # Create a FastAPI app
# app = FastAPI()

# # Define the message model that will be used to parse the incoming request body
# class Message(BaseModel):
#     content: str

# # Function to process the message with ChatGoogleGenerativeAI and return the response
# async def send_message(content: str) -> dict:
#     # Fetch the API key from the environment variable
#     gemini_api_key = os.getenv("GEMINI_API_KEY")
    
#     if not gemini_api_key:
#         raise ValueError("GEMINI_API_KEY is not set. Please provide the API key in your environment.")

#     # Initialize the ChatGoogleGenerativeAI model
#     model = ChatGoogleGenerativeAI(
#         model="gemini-1.5-flash",  # Specify the model
#         google_api_key=gemini_api_key,  # Pass the API key      
#     )

#     try:
#         # Generate a response using the provided content
#         result = await model.agenerate(messages=[[HumanMessage(content=content)]])
#         # Return the response as a dictionary
#         return {"response": result}

#         # # Extract only the generated text (poem or response content)
#         # if result and "generations" in result:
#         #     response_text = result["generations"][-1][-1]["text"]
#         # else:
#         #     response_text = "No response generated."

#         # # Return only the response text (poem or context)
#         # return response_text
    

#     except Exception as e:
#         return {"error": str(e)}

# # POST endpoint to handle incoming requests and get a response from the model
# @app.post("/chat/")
# async def chat(message: Message):
#     try:
#         # Send the message content to the model and await the result
#         result = await send_message(message.content)
#         return result  # Return the response from the model
#     except Exception as e:
#         return {"error": str(e)}



# .env  GEMINI_API_KEY=, 
