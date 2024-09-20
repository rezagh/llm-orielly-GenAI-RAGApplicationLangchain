#https://ai.google.dev/gemini-api/docs/models/gemini

from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
# Load environment variables from .env file
load_dotenv()

# Print all environment variables to debug
#print(os.environ)

# Print the value of OPENAI_API_KEY
print(os.getenv("GOOGLE_API_KEY"))

llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key=os.getenv("GOOGLE_API_KEY"))
response  = llm.invoke("Hello, how are you?")
print(response)
