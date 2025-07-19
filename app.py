from flask import Flask, request, jsonify, render_template

from services.pdf_reader import read_pdf
from agents.chunking_agent import chunk_text
from agents.qa_agent import answer_question
from services.embedding_service import get_embedding
from services.chroma_service import store_chunk
from agents.summarizer_agent import summarize_book

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    text = read_pdf(file)
    chunks = chunk_text(text)

    # Store in Chroma
    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        store_chunk(chunk, embedding, id=f"chunk_{i}")

    # Call summarizer agent
    summary = summarize_book(chunks)

    return jsonify({
        "message": f"{len(chunks)} chunks stored.",
        "summary": summary
    })

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")
    answer = answer_question(question)
    return jsonify({"answer": answer})



@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)