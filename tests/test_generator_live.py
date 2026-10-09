from src.generation.generator import generate_answer

context = [
    {
        "text": (
            "A summons is an official court document requiring a person "
            "to appear before a court. The document specifies the required "
            "appearance details."
        ),
        "source": "sample_procedure_guide.pdf",
        "page": 1,
    }
]

question = "What is a court summons?"

answer = generate_answer(question, context)

print("Question:", question)
print("Answer:", answer)

assert isinstance(answer, str)
assert answer.strip(), "The generator returned an empty answer."

print("\nLive generation test passed.")