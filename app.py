import html
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
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&display=swap');

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
        radial-gradient(circle at 90% 0%, rgba(173,145,96,0.12), transparent 42%),
        var(--bg);
    color: var(--navy);
    font-family: 'DM Sans', sans-serif;
}

header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }

.block-container {
    max-width: 1200px !important;
    padding: 3.2rem 4vw 2rem !important;
}

/* ---------- Hamburger (restyles Streamlit's sidebar toggle) ---------- */
[data-testid="stSidebarCollapsedControl"] svg,
[data-testid="stExpandSidebarButton"] svg,
[data-testid="stExpandSidebarButton"] span {
    display: none !important;
}
[data-testid="stSidebarCollapsedControl"] button::after,
[data-testid="stExpandSidebarButton"]::after {
    content: "☰";
    font-size: 1.5rem;
    line-height: 1;
    color: var(--navy);
}
[data-testid="stSidebarCollapsedControl"] button,
[data-testid="stExpandSidebarButton"] {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    box-shadow: 0 4px 14px rgba(32,42,60,0.06);
}
[data-testid="stSidebarCollapsedControl"] button:hover,
[data-testid="stExpandSidebarButton"]:hover {
    border-color: var(--gold) !important;
}

/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"] {
    background: var(--surface);
    border-right: 1px solid var(--border);
}
section[data-testid="stSidebar"] * { color: var(--navy); }
section[data-testid="stSidebar"] div[data-testid="stCaptionContainer"] * { color: var(--muted) !important; }
section[data-testid="stSidebar"] div[data-testid="stButton"] button {
    justify-content: flex-start;
    text-align: left;
    min-height: 44px;
    border-radius: 12px;
}
section[data-testid="stSidebar"] div[data-testid="stButton"] button p {
    text-align: left;
    font-size: 0.9rem;
}
/* Selected history item */
section[data-testid="stSidebar"] button[kind="primary"],
section[data-testid="stSidebar"] button[data-testid="stBaseButton-primary"] {
    background: #F3EEDF !important;
    border: 1px solid var(--gold) !important;
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
    max-width: 540px;
}

.chips { margin-top: 1.1rem; display: flex; gap: 0.5rem; flex-wrap: wrap; }
.chip {
    font-size: 0.74rem;
    font-weight: 600;
    color: var(--navy);
    background: rgba(255,255,255,0.8);
    border: 1px solid #DED4BF;
    border-radius: 999px;
    padding: 0.3rem 0.8rem;
}

/* Logo: pinned to the right edge of its column */
div[data-testid="stImage"] {
    display: flex;
    justify-content: flex-end;
}
div[data-testid="stImage"] img { object-fit: contain; }

/* ---------- Question box ---------- */
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

/* ---------- Buttons (suggestions, sidebar, clear) ---------- */
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
}

/* ---------- Answer card (question + answer in ONE box) ---------- */
.st-key-answer_card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-top: 3px solid var(--gold);
    border-radius: 20px;
    padding: 1.6rem 1.8rem 1.4rem;
    box-shadow: 0 10px 40px rgba(32,42,60,0.07);
}
.st-key-answer_card p,
.st-key-answer_card li,
.st-key-answer_card span,
.st-key-answer_card strong,
.st-key-answer_card h1,
.st-key-answer_card h2,
.st-key-answer_card h3,
.st-key-answer_card h4 {
    color: var(--navy) !important;
}
.st-key-answer_card p,
.st-key-answer_card li {
    font-size: 1.02rem;
    line-height: 1.75;
}
.q-text {
    font-family: 'Playfair Display', Georgia, serif;
    font-style: italic;
    font-size: 1.45rem;
    line-height: 1.35;
    color: var(--navy);
    margin: 0.35rem 0 0.2rem;
}
.card-sep {
    height: 1px;
    background: linear-gradient(90deg, var(--gold), transparent);
    margin: 1rem 0 1rem;
    opacity: 0.6;
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

div[data-testid="stSpinner"] * { color: var(--muted) !important; }

@media (max-width: 768px) {
    .block-container { padding: 3rem 1rem 2rem !important; }
    .hero { font-size: 2.4rem; }
    .st-key-answer_card { padding: 1.2rem 1.2rem 1rem; }
}
</style>
""", unsafe_allow_html=True)


# ==================== STATE ====================
# history: list of {"question", "answer", "sources"}
# view_idx: which history item is open (None = home screen)

if "history" not in st.session_state:
    st.session_state.history = []

if "view_idx" not in st.session_state:
    st.session_state.view_idx = None

if "queued_question" not in st.session_state:
    st.session_state.queued_question = ""


# ==================== HELPERS ====================

def ask(question: str, language: str = "English") -> None:
    try:
        from src.pipeline import answer_question

        with st.spinner("Preparing your explanation..."):
            result = answer_question(question, language)

        answer = result.get("answer", "No answer was returned. Please try again.")
        sources = result.get("sources", [])

    except Exception:
        answer = (
            "The backend is not ready or could not process your question. "
            "Please check that the retrieval and generation modules are available."
        )
        sources = []

    st.session_state.history.append(
        {"question": question, "answer": answer, "sources": sources}
    )
    st.session_state.view_idx = len(st.session_state.history) - 1


def render_answer(item: dict) -> None:
    with st.container(key="answer_card"):
        st.markdown(
            '<div class="eyebrow">YOUR QUESTION</div>'
            f'<div class="q-text">{html.escape(item["question"])}</div>'
            '<div class="card-sep"></div>'
            '<div class="eyebrow">JURISAI EXPLAINS</div>',
            unsafe_allow_html=True,
        )
        st.markdown(item["answer"])

        if item.get("sources"):
            with st.expander("View sources and references"):
                for source in item["sources"]:
                    st.markdown(f"**{source.get('source', 'Legal document')}**")
                    if source.get("page") is not None:
                        st.caption(f"Page {source['page']}")
                    st.write(source.get("text", ""))


def short(text: str, n: int = 44) -> str:
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def suggest_followups(question: str) -> list[str]:
    """Return procedural follow-up questions based on the current topic."""
    q = question.lower()

    if "summons" in q:
        return [
            "What happens after a summons is received?",
            "How is a summons different from a warrant?",
            "What does appearing before a court mean?",
        ]
    if "hearing" in q:
        return [
            "What usually happens after a hearing?",
            "What is an adjournment?",
            "What are the different stages of a court case?",
        ]
    if "filing" in q or "file a case" in q:
        return [
            "What happens after a case is filed?",
            "What is a court notice?",
            "What happens during the first hearing?",
        ]
    if "stage" in q or "process" in q or "procedure" in q:
        return [
            "What happens during a court hearing?",
            "What is a summons?",
            "What can happen after a hearing?",
        ]
    return [
        "What are the different stages of a court case?",
        "What happens during a court hearing?",
        "What is a summons?",
    ]


def render_followups(item: dict) -> None:
    """Render clickable follow-up questions with the existing button styling."""
    st.markdown("**Suggested questions**")
    for i, followup in enumerate(suggest_followups(item["question"])):
        if st.button(
            followup,
            key=f"followup_{st.session_state.view_idx}_{i}",
            use_container_width=True,
        ):
            st.session_state.queued_question = followup
            st.rerun()


# ==================== BRAND BAR ====================

header_left, header_right = st.columns([1, 1])

with header_left:
    st.markdown('<div class="brand">Juris<span>AI</span></div>', unsafe_allow_html=True)


# ==================== HERO (text left, logo right) ====================

logo_path = Path(__file__).parent / "assets" / "jurisai-logo.png"

hero_text, hero_logo = st.columns([1.25, 1], vertical_alignment="center", gap="large")

with hero_text:
    st.markdown('<div class="eyebrow">YOUR JUDICIAL PROCESS COMPANION</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero">Legal clarity.<br><span>Without complexity.</span></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="subtitle">Understand court procedures, hearing stages, and legal terms '
        'through clear, accessible explanations grounded in legal documents.</div>'
        '<div class="chips">'
        '<span class="chip">Plain language</span>'
        '<span class="chip">Source-backed</span>'
        '<span class="chip">Not legal advice</span>'
        '</div>',
        unsafe_allow_html=True,
    )

with hero_logo:
    if logo_path.exists():
        st.image(str(logo_path), width=300)


# ==================== QUESTION BOX ====================

st.write("")

with st.form("question_form", clear_on_submit=True):
    
    question = st.text_input(
        "Your question",
        placeholder="Ask anything about court procedures...",
        label_visibility="collapsed",
    )
    submitted = st.form_submit_button("Ask JurisAI", use_container_width=True)

to_ask = None
if submitted and question.strip():
    to_ask = question.strip()
elif st.session_state.queued_question:
    to_ask = st.session_state.queued_question
    st.session_state.queued_question = ""

if to_ask:
    ask(
        to_ask,
        st.session_state.get("response_language", "English"),
    )


# ==================== ANSWER (just below the box) / SUGGESTIONS ====================

st.write("")

view_idx = st.session_state.view_idx
history = st.session_state.history

if view_idx is not None and 0 <= view_idx < len(history):
    render_answer(history[view_idx])
    render_followups(history[view_idx])

else:
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


# ==================== SIDEBAR: HISTORY ====================

with st.sidebar:
    st.markdown('<div class="brand">Juris<span>AI</span></div>', unsafe_allow_html=True)
    st.write("")

    if st.button("＋  New question", key="new_q", use_container_width=True):
        st.session_state.view_idx = None
        st.rerun()

    st.write("")
    st.markdown('<div class="eyebrow">YOUR CONVERSATIONS</div>', unsafe_allow_html=True)
    st.write("")

    if not history:
        st.caption("Your questions will appear here.")
    else:
        # Newest first
        for i in reversed(range(len(history))):
            selected = (i == st.session_state.view_idx)
            if st.button(
                short(history[i]["question"]),
                key=f"hist_{i}",
                use_container_width=True,
                type="primary" if selected else "secondary",
                help=history[i]["question"],
            ):
                st.session_state.view_idx = i
                st.rerun()

        st.write("")
        if st.button("Clear history", key="clear_hist", use_container_width=True):
            st.session_state.history = []
            st.session_state.view_idx = None
            st.rerun()


# ==================== FOOTER ====================

st.write("")
st.write("")

st.markdown(
    '<div style="text-align:center;color:#747B87;font-size:0.78rem;line-height:1.8;'
    'border-top:1px solid #E8E4DA;padding-top:1rem;">'
    '<span style="color:#AD9160;font-weight:600;">JurisAI</span>'
    ' &nbsp;·&nbsp; General procedural information, not legal advice.'
    '<br>Always verify requirements with the relevant court or official source.'
    '</div>',
    unsafe_allow_html=True,
)