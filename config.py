import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
MODEL_PATH = "./model/llama-2-7b-chat.ggmlv3.q4_0.bin"
INDEX_NAME = "medical-chatbot"