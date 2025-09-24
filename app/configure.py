
from dotenv import load_dotenv 
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # fixed spelling
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
