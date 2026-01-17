import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configuration settings
DATABASE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database", "attacks.db")

# Validate keys
if not OPENAI_API_KEY:
    print("WARNING: OPENAI_API_KEY not found in .env file.")
if not GOOGLE_API_KEY:
    print("WARNING: GOOGLE_API_KEY not found in .env file.")
