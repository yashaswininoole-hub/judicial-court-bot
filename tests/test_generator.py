from src.generation.generator import generate_answer


def test_empty_question():
    result = generate_answer("   ", [])
    assert "enter a question" in result.lower()


def test_empty_context():
    result = generate_answer("What is a summons?", [])
    assert "reference material" in result.lower()


if __name__ == "__main__":
    test_empty_question()
    test_empty_context()
    print("Basic generator tests passed.")