# judicial-court-bot

# JurisAI — Legal Clarity

**Making legal and judicial information easier to understand.**

JurisAI is an AI-powered legal information chatbot designed to help users understand court procedures, judicial processes, and legal terminology through clear, accessible, plain-language explanations. It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from a collection of legal documents and generate responses grounded in the available sources.

Powered by a locally running Large Language Model (LLM) through Ollama, JurisAI combines document retrieval with AI-generated explanations to make legal information easier to navigate while prioritizing transparency, responsible AI use, and user safety.

> **Disclaimer:** JurisAI is an informational tool, not a substitute for a qualified legal professional. It does not provide personalized legal advice, predict judicial decisions, or replace official legal sources.

---

## Features

- **Conversational Interface:** Ask questions about court procedures, judicial processes, and legal terminology in a simple chat interface.
- **Retrieval-Augmented Generation (RAG):** Retrieves relevant passages from the available legal documents before generating an answer.
- **Source-Grounded Responses:** Uses retrieved document passages to reduce unsupported or fabricated answers.
- **Plain-Language Explanations:** Simplifies complex legal terminology and procedural information.
- **Local AI Inference:** Uses Ollama to run the language model locally, reducing dependence on external LLM APIs.
- **Context-Aware Responses:** Uses the user's question and retrieved document context to generate relevant answers.
- **Responsible AI Safeguards:** Restricts legal-advice requests, judicial-outcome predictions, and questions outside the application's intended scope.
- **Interactive Streamlit UI:** Provides an accessible interface for asking questions and viewing responses.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive chatbot interface |
| Ollama | Local LLM inference and response generation |
| Llama 3.2 (if configured) | Language model for generating responses |
| Sentence Transformers | Converts text into semantic embeddings |
| FAISS | Efficient similarity search over document embeddings |
| PyMuPDF | Extracts text from PDF documents |
| NumPy | Numerical operations on embedding vectors |
| LangChain Text Splitters | Splits documents into manageable text chunks |
| Pytest | Testing application components and behavior |
| Git and GitHub | Version control and team collaboration |

## How It Works

JurisAI follows a Retrieval-Augmented Generation (RAG) workflow.

1. **Document Collection:** Legal documents, court procedure guides, and other relevant official PDFs are collected.
2. **PDF Extraction:** Text is extracted from the PDF files.
3. **Text Chunking:** Extracted text is divided into smaller chunks while retaining relevant source metadata, such as document names and page numbers.
4. **Embedding Generation:** A Sentence Transformers model converts the chunks into numerical vectors that represent their semantic meaning.
5. **Vector Indexing:** FAISS stores the vectors and enables efficient similarity searches.
6. **Context Retrieval:** When a user submits a question, the retriever identifies relevant document passages.
7. **Answer Generation:** The retrieved passages and question are passed to the Ollama-powered language model.
8. **Response Delivery:** The chatbot returns a natural-language answer grounded in the retrieved information, subject to the application's safety rules.

### Architecture

```text
User Question
     |
     v
Streamlit Chat Interface
     |
     v
Question and Context Retrieval
     |
     v
FAISS Vector Search <--- Indexed Legal Documents
     |
     v
Relevant Document Passages
     |
     v
Safety Rules and Prompt Construction
     |
     v
Ollama LLM
     |
     v
Grounded Answer
     |
     v
Streamlit Response Display
```

The document-indexing pipeline runs separately from normal question answering. The index must be built before the chatbot can retrieve passages from the collected PDFs.

## Getting Started

Follow these instructions to run JurisAI locally.

### Prerequisites

Install the following before proceeding:

- Python 3.10 or a compatible version supported by the project dependencies.
- Git.
- [Ollama](https://ollama.com/download).
- The language model configured in `src/generation/generator.py`.


### 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/yashaswininoole-hub/judicial-court-bot.git
cd judicial-court-bot
```

### 2. Create and Activate a Virtual Environment (Recommended)

Create a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages from `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

If an installation fails, check the Python version and the package's compatibility with your operating system.

### 4. Set Up Ollama

Install Ollama and make sure it is running.

If the project is configured to use Llama 3.2, download the model with:

```bash
ollama pull llama3.2
```

Verify that the model is available:

```bash
ollama list
```

If `generator.py` specifies a different Ollama model, download that model instead. The configured model name must match the model available locally.

### 5. Build the Document Index

If the repository does not already contain a valid index, run:

```bash
python -m scripts.build_index
```

This script extracts PDF text, creates chunks and embeddings, and builds the FAISS index and associated chunk metadata.

After successful indexing, the expected output includes files similar to:

```text
data/
└── index/
    ├── legal.index
    └── chunks.json
```

The exact output depends on the indexing implementation. If the command reports that no PDFs were found, verify that the files are inside `data/raw/`. Scanned PDFs may require OCR before their text can be extracted.

### 6. Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

Streamlit will display a local URL, usually:

```text
http://localhost:8501
```

Open this URL in your browser to start chatting with JurisAI.

Enter a question about court procedures or legal terminology and submit it through the interface.

**Note:** If the document index has not been generated, the application may run but fail to retrieve relevant legal information.

## Example Questions

Questions within the intended scope include:

- What is a court summons?
- What are the general stages of a civil court case?
- What does an affidavit mean?
- What is the difference between an appeal and a revision?
- What happens during a preliminary hearing?

Answers depend on the coverage, accuracy, and availability of the indexed documents.

## Safety, Scope and Limitations

JurisAI is designed to provide general legal information, not professional legal representation.

### What JurisAI Can Do

- Explain general legal terminology.
- Describe court procedures covered by its reference documents.
- Summarize relevant passages from available legal sources.
- Help users understand procedural information in plain language.

### What JurisAI Cannot Do

- **Act as a legal adviser:** It cannot provide personalized legal advice, represent users, or replace a qualified lawyer.
- **Predict judicial rulings:** It cannot reliably predict what a particular judge will decide or guarantee the outcome of a case.
- **Make case-specific legal decisions:** It cannot determine a user's legal rights, liability, litigation strategy, or best course of action.
- **Answer unrelated questions:** It is not intended to function as a general-purpose chatbot for topics outside its legal-information scope.
- **Guarantee complete or current information:** Its answers are limited by the indexed documents, their accuracy, and their date of publication.
- **Replace official sources:** Users should verify important information against current court rules, official government publications, and qualified legal professionals.

### Grounding and Responsible Use

The application is designed to prioritize retrieved document context over unsupported model-generated claims. When relevant information cannot be found in the available documents, it should communicate that limitation rather than inventing a source or presenting speculation as fact.

However, RAG does not eliminate hallucinations, retrieval errors, or outdated information. Responses should always be independently verified before being relied upon.

## Project Structure

The repository is organized into separate modules for the user interface, retrieval, generation, and testing.

```text
judicial-court-bot/
├── app.py
├── src/
│   ├── generation/
│   │   └── generator.py
│   ├── retrieval/
│   │   ├── document_loader.py
│   │   ├── chunker.py
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   └── retriever.py
│   └── pipeline.py
├── scripts/
│   └── build_index.py
├── tests/
├── data/
│   ├── raw/
│   └── index/
├── requirements.txt
├── .gitignore
└── README.md
```


## Testing

Run the automated test suite with:

```bash
python -m pytest
```

To test retrieval separately, after the document index has been built, run:

```bash
python -m tests.test_retrieval
```

Additional tests can be used to verify answer generation, empty inputs, irrelevant questions, safety restrictions, and the handling of questions unsupported by the available documents.

## Future Improvements

Potential areas for further development include:

- Improved multilingual question answering and document retrieval.
- Better support for scanned PDFs through OCR.
- More comprehensive legal-document coverage.
- Stronger source citations and document-page references in responses.
- Expanded safety and hallucination evaluations.
- Retrieval-quality benchmarking and end-to-end testing.
- Deployment with appropriate privacy, security, and operational safeguards.

## Disclaimer

JurisAI is an educational and informational project. It does not establish an attorney-client relationship and must not be relied upon as a substitute for professional legal advice. Always consult a qualified legal professional and verify important information with the relevant official sources.

---

**JurisAI — Legal clarity, grounded in documents.**
