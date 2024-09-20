from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Print all environment variables to debug
#print(os.environ)

# Print the value of OPENAI_API_KEY
print(os.getenv("OPENAI_API_KEY"))