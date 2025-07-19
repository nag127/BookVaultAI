from openai import OpenAI
from config.llm_config import openai_api_key

# Initialize OpenAI client
client = OpenAI(api_key=openai_api_key)

def get_embedding(text, model="text-embedding-3-small"):
    response = client.embeddings.create(
        input=[text],
        model=model
    )
    return response.data[0].embedding