from config.llm_config import get_llm

def summarize_book(chunks, max_chunks=10):
    """
    Summarizes the first few chunks of the book.
    Adjust `max_chunks` to limit input size.
    """
    # Concatenate first few chunks
    text_to_summarize = "\n\n".join(chunks[:max_chunks])
    
    prompt = f"""
You are a helpful assistant. Summarize the following book content in a concise, easy-to-read format:

{text_to_summarize}

Summary:
"""

    llm = get_llm()
    response = llm.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
