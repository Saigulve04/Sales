from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve API Key
API_KEY = os.getenv("API_KEY")

# Check if the API key is loaded properly
if API_KEY is None:
    raise ValueError(" API_KEY is missing! Check your .env file.")

print(f" API Key Loaded: {API_KEY[:6]}********")  # Partially display for security
