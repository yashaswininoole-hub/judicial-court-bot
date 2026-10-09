
from src.retrieval.retriever import retrieve_context
from src.generation.generator import generate_answer


def answer_question(question: str) -> dict:
    """Retrieve legal passages and generate a grounded answer."""

    if not question or not question.strip():
        return {
            "answer": "Please enter a question.",
            "sources": [],
            "status": "invalid_input",
        }

    try:
        context = retrieve_context(question)

        if not context:
            return {
                "answer": (
                    "I couldn't find relevant information in the "
                    "available documents. Please try rephrasing "
                    "your question."
                ),
                "sources": [],
                "status": "no_context",
            }

        answer = generate_answer(question, context)

        return {
            "answer": answer,
            "sources": context,
            "status": "ok",
        }

    except Exception:
        return {
            "answer": (
                "Sorry, I couldn't process your question. "
                "Please try again."
            ),
            "sources": [],
            "status": "error",
        }
