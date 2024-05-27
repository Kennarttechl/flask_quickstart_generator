# load_env.py
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set the necessary environment variables for Twine
os.environ['TWINE_USERNAME'] = os.getenv('username')
os.environ['TWINE_PASSWORD'] = os.getenv('password')
