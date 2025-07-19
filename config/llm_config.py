from openai import OpenAI
from chromadb.config import Settings
import chromadb

openai_api_key = "sk-Your API Key"

# LLM client
def get_llm():
    return OpenAI(api_key=openai_api_key)

# ChromaDB client
def get_chroma_client(persist_dir="./data/chroma_storage"):
    return chromadb.PersistentClient(path=persist_dir)