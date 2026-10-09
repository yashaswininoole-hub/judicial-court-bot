import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="JurisAI | Legal Clarity",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==================== STYLING ====================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600&display=swap');

:root {
    --bg: #F7F6F2;
    --surface: #FFFFFF;
    --navy: #202A3C;
    --gold: #AD9160;
    --muted: #747B87;
    --border: #E8E4DA;
}

.stApp {
    background:
        radial-gradient(circle at 85% 0%, rgba(173,145,96,0.10), transparent 40%),
        var(--bg);
    color: var(--navy);
    font-family: 'DM Sans', sans-serif;
}

header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }

.block-container {
    max-width: 1200px !important;
    padding: 1.4rem 4vw 2rem !important;
}

/* ---------- Brand ---------- */
.brand {
    font-size: 1.15rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    color: var(--navy);
}
.brand span { color: var(--gold); }

/* ---------- Hero ---------- */
.eyebrow {
    color: var(--gold);
    text-transform: uppercase;
    font-size: 0.72rem;
    letter-spacing: 0.18em;
    font-weight: 700;
}

.hero {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(2.4rem, 4.4vw, 4rem);
    line-height: 1.12;
    letter-spacing: -0.03em;
    color: var(--navy);
    margin: 0.6rem 0 0.9rem;
}
.hero span { color: var(--gold); }

.subtitle {
    font-size: 1rem;
    line-height: 1.7;
    color: var(--muted);
    max-width: 560px;
}

/* Logo (right column) */
div[data-testid="stImage"] {
    display: flex;
    justify-content: center;
}
div[data-testid="stImage"] img {
    object-fit: contain;
    filter: drop-shadow(0 10px 24px rgba(32,42,60,0.12));
}

/* ---------- Chatbox ---------- */
div[data-testid="stForm"] {
    background: var(--surface);
    border: 1px solid #DED4BF;
    border-radius: 22px;
    padding: 1rem 1.2rem;
    box-shadow: 0 8px 35px rgba(32,42,60,0.06), 0 0 22px rgba(173,145,96,0.10);
    transition: box-shadow 0.25s ease, border-color 0.25s ease;
}
div[data-testid="stForm"]:focus-within {
    border-color: var(--gold);
    box-shadow: 0 8px 38px rgba(32,42,60,0.08), 0 0 26px rgba(173,145,96,0.22);
}

/* Make typed text visible: override Streamlit's inner wrappers */
div[data-testid="stTextInput"] div[data-baseweb="input"],
div[data-testid="stTextInput"] div[data-baseweb="base-input"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}
div[data-testid="stTextInput"] input {
    background: transparent !important;
    color: var(--navy) !important;
    -webkit-text-fill-color: var(--navy) !important;
    caret-color: var(--gold) !important;
    font-family: 'DM Sans', sans-serif;
    font-size: 1.02rem;
}
div[data-testid="stTextInput"] input::placeholder {
    color: var(--muted) !important;
    -webkit-text-fill-color: var(--muted) !important;
    opacity: 1;
}

/* Submit button */
div[data-testid="stFormSubmitButton"] button {
    background: var(--navy) !important;
    border: none;
    border-radius: 12px;
    min-height: 44px;
    transition: all 0.2s ease;
}
div[data-testid="stFormSubmitButton"] button p {
    color: #FFFFFF !important;
    font-weight: 600;
}
div[data-testid="stFormSubmitButton"] button:hover { background: #34445D !important; }

/* ---------- Suggestion / secondary buttons ---------- */
div[data-testid="stButton"] button {
    background: rgba(255,255,255,0.9) !important;
    border: 1px solid var(--border);
    border-radius: 13px;
    min-height: 48px;
    transition: all 0.2s ease;
}
div[data-testid="stButton"] button p { color: var(--navy) !important; }
div[data-testid="stButton"] button:hover {
    background: #FFFFFF !important;
    border-color: var(--gold);
    box-shadow: 0 4px 14px rgba(32,42,60,0.06);
    transform: translateY(-1px);
}

/* ---------- Chat messages ---------- */
div[data-testid="stChatMessage"] {
    background: var(--surface) !important;
    border: 1px solid var(--border);
    border-left: 4px solid var(--gold);
    border-radius: 16px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.8rem;
    box-shadow: 0 4px 18px rgba(32,42,60,0.04);
}
/* User question gets a softer cream card */
div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) {
    background: #FBF9F3 !important;
    border-left-color: var(--navy);
}
/* Force readable text everywhere inside messages */
div[data-testid="stChatMessage"] p,
div[data-testid="stChatMessage"] li,
div[data-testid="stChatMessage"] span,
div[data-testid="stChatMessage"] strong,
div[data-testid="stChatMessage"] h1,
div[data-testid="stChatMessage"] h2,
div[data-testid="stChatMessage"] h3,
div[data-testid="stChatMessage"] h4 {
    color: var(--navy) !important;
    line-height: 1.7;
}

/* ---------- Sources expander ---------- */
div[data-testid="stExpander"] {
    background: #FBF9F3;
    border: 1px solid var(--border);
    border-radius: 12px;
}
div[data-testid="stExpander"] * { color: var(--navy) !important; }
div[data-testid="stCaptionContainer"],
div[data-testid="stCaptionContainer"] * { color: var(--muted) !important; }

/* Spinner */
div[data-testid="stSpinner"] * { color: var(--muted) !important; }

hr { border-color: var(--border); }

@media (max-width: 768px) {
    .block-container { padding: 1rem 1rem 2rem !important; }
    .hero { font-size: 2.4rem; }
}
</style>
""", unsafe_allow_html=True)


# ==================== STATE ====================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "queued_question" not in st.session_state:
    st.session_state.queued_question = ""


# ==================== HELPERS ====================

def ask(question: str) -> None:
    """Run the pipeline and store the Q&A pair in session state."""
    st.session_state.messages.append({"role": "user", "content": question})

    try:
        from src.pipeline import answer_question

        with st.spinner("Preparing your explanation..."):
            result = answer_question(question)

        answer = result.get("answer", "No answer was returned. Please try again.")
        sources = result.get("sources", [])

    except Exception:
        answer = (
            "The backend is not ready or could not process your question. "
            "Please check that the retrieval and generation modules are available."
        )
        sources = []

    st.session_state.messages.append(
        {"role": "assistant", "content": answer, "sources": sources}
    )


def render_message(message: dict) -> None:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message["role"] == "assistant" and message.get("sources"):
            with st.expander("View sources and references"):
                for source in message["sources"]:
                    st.markdown(f"**{source.get('source', 'Legal document')}**")
                    if source.get("page") is not None:
                        st.caption(f"Page {source['page']}")
                    st.write(source.get("text", ""))


# ==================== BRAND BAR ====================

header_left, header_right = st.columns([1, 1])

with header_left:
    st.markdown('<div class="brand">Juris<span>AI</span></div>', unsafe_allow_html=True)

with header_right:
    st.markdown(
        '<div style="text-align:right;color:#747B87;font-size:0.82rem;padding-top:5px;">'
        'JUDICIAL PROCESS EXPLAINER</div>',
        unsafe_allow_html=True,
    )

st.divider()


# ==================== HERO (text left, logo right) ====================

logo_path = Path(__file__).parent / "assets" / "jurisai-logo.png"

hero_text, hero_logo = st.columns([1.4, 1], vertical_alignment="center", gap="large")

with hero_text:
    st.markdown('<div class="eyebrow">YOUR JUDICIAL PROCESS COMPANION</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero">Legal clarity.<br><span>Without complexity.</span></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="subtitle">Understand court procedures, hearing stages, and legal terms '
        'through clear, accessible explanations grounded in legal documents.</div>',
        unsafe_allow_html=True,
    )

with hero_logo:
    if logo_path.exists():
        st.image(str(logo_path), width=260)


# ==================== QUESTION BOX ====================

st.write("")
st.write("")

with st.form("question_form", clear_on_submit=True):
    question = st.text_input(
        "Your question",
        placeholder="Ask anything about court procedures...",
        label_visibility="collapsed",
    )
    submitted = st.form_submit_button("Ask JurisAI", use_container_width=True)

# Decide what to ask (typed question or clicked suggestion)
to_ask = None
if submitted and question.strip():
    to_ask = question.strip()
elif st.session_state.queued_question:
    to_ask = st.session_state.queued_question
    st.session_state.queued_question = ""

if to_ask:
    ask(to_ask)


# ==================== ANSWERS (directly below the box) ====================

if st.session_state.messages:
    st.write("")
    st.markdown('<div class="eyebrow">YOUR CONVERSATION</div>', unsafe_allow_html=True)
    st.write("")

    # Newest Q&A first, so the latest answer sits right under the text box
    messages = st.session_state.messages
    pairs = [messages[i:i + 2] for i in range(0, len(messages), 2)]

    for pair in reversed(pairs):
        for message in pair:
            render_message(message)

    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()

else:
    # ==================== SUGGESTIONS (only before first question) ====================
    st.write("")
    st.markdown(
        '<div class="eyebrow" style="text-align:center;margin-bottom:0.8rem;">'
        'START WITH A COMMON QUESTION</div>',
        unsafe_allow_html=True,
    )

    suggestions = [
        "What is a summons?",
        "What happens during a hearing?",
        "What are the stages of a court case?",
        "How is a court case filed?",
    ]

    col1, col2 = st.columns(2)
    for i, suggestion in enumerate(suggestions):
        with (col1 if i % 2 == 0 else col2):
            if st.button(suggestion, key=f"suggestion_{i}", use_container_width=True):
                st.session_state.queued_question = suggestion
                st.rerun()


# ==================== FOOTER ====================

st.write("")
st.write("")
st.divider()

st.markdown(
    '<div style="text-align:center;color:#747B87;font-size:0.78rem;line-height:1.8;">'
    '<span style="color:#AD9160;font-weight:600;">JurisAI</span>'
    ' &nbsp;·&nbsp; General procedural information, not legal advice.'
    '<br>Always verify requirements with the relevant court or official source.'
    '</div>',
    unsafe_allow_html=True,
)