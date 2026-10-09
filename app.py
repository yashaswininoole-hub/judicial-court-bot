from src.pipeline import answer_question

import streamlit as st

st.set_page_config(
    page_title="CourtFlow AI",
    page_icon="⚖️",
    layout="centered",
)

st.title("⚖️ CourtFlow AI")
st.caption("Judicial Court Process & Case Flow Explainer")

st.info(
    "Understand court procedures in simple terms. "
    "This tool provides general information, not legal advice."
)

with st.sidebar:
    st.header("About CourtFlow AI")
    st.write("Explore court procedures and common legal terms.")

    st.subheader("Try asking")
    examples = [
        "What is a summons?",
        "What happens during a hearing?",
        "What are the stages of a court case?",
        "How is a court case filed?",
    ]

    for example in examples:
        st.write(f"• {example}")

    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask about court procedures...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Temporary response until backend integration is ready
    result = answer_question(question)
    answer = result["answer"]

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
