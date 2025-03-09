import os
from dotenv import load_dotenv

load_dotenv()
# Fetch the API key from the environment
api_key = os.getenv('GROQ_API_KEY')

if api_key:
    print("API Key successfully fetched")
else:
    print("Error: API Key not found")
