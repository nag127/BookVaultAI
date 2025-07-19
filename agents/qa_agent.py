from services.embedding_service import get_embedding
from services.chroma_service import query_chunks
from config.llm_config import get_llm

def answer_question(question):
    query_embedding = get_embedding(question)
    results = query_chunks(query_embedding)
    context = "\n".join(results["documents"][0])
    
    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    llm = get_llm()
    response = llm.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
