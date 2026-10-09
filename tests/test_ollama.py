import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Explain what a court summons is in one simple sentence."
        }
    ]
)

print(response["message"]["content"])