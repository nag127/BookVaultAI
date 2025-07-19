from config.llm_config import get_chroma_client

# Initialize Chroma persistent client
chroma_client = get_chroma_client()

# Get or create collection
collection = chroma_client.get_or_create_collection(name="book_chunks")

def store_chunk(text, embedding, id):
    """Store a single chunk with its embedding and ID."""
    collection.add(documents=[text], embeddings=[embedding], ids=[id])

def query_chunks(query_embedding, n_results=3):
    """Query Chroma for similar chunks based on vector similarity."""
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents"]
    )
