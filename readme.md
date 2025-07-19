```markdown
# BookVaultAI

BookVaultAI is a Flask-based web application designed to process PDF books, generate summaries, and answer questions about the content using natural language processing and machine learning models, specifically leveraging OpenAI's GPT-4 model.

## Description

BookVaultAI enables users to upload PDF books, which are then processed to extract and chunk text. This text is stored in a vector database for efficient querying. The application provides a concise summary of the book and allows users to ask questions, receiving answers generated through advanced AI models.

## Features

- **PDF Processing**: Upload and process PDF books to extract and store text chunks.
- **Summarization**: Generate a concise summary of the uploaded book.
- **Question Answering**: Enable users to ask questions about the book content and receive AI-generated answers.
- **User Interface**: An interactive HTML-based front-end for seamless interaction.

## Prerequisites

- **Python**: Ensure Python 3.6 or higher is installed.
- **OpenAI API Key**: Obtain an OpenAI API key to access GPT-4 functionalities.
- **ChromaDB setup**: Ensure ChromaDB is set up for vector storage and querying.

## Setup Instructions

### Step 1: Environment Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd BookVaultAI
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source env/bin/activate
     ```

### Step 2: Install Required Libraries

Install the necessary Python libraries:
```bash
pip install Flask PyPDF2 openai chromadb
```

### Step 3: Configure the Application

1. **Setup OpenAI API Key**: In `config/llm_config.py`, set your OpenAI API key:
   ```python
   openai_api_key = "your_actual_openai_api_key"
   ```

2. **Ensure ChromaDB is properly configured**.

## How to Run

1. **Start the Flask Application**:
   ```bash
   python app.py
   ```

2. **Access the Application**: Open your browser and go to `http://127.0.0.1:5000/` to view the BookVaultAI interface.

## Technologies Used

- **Flask**: For web framework and templating.
- **OpenAI GPT-4**: For generating summaries and answering questions.
- **ChromaDB**: A vector database for efficient text querying.
- **PyPDF2**: For reading and extracting text from PDF files.
- **Bootstrap**: For front-end styling.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

By following these instructions, you will have a fully functional BookVaultAI application ready to process PDFs and interact with users using AI. Enjoy exploring your books with the power of AI!
```