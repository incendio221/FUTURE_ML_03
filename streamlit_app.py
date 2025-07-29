import streamlit as st
from dialogflow_utils import detect_intent_texts
import uuid

# ──────────────────────────────────────────────────
# BASIC APP CONFIG
# ──────────────────────────────────────────────────
st.set_page_config(page_title="Customer Support Chatbot",
                   page_icon="💬",
                   layout="centered",
                   initial_sidebar_state="collapsed")

# ──────────────────────────────────────────────────
# STYLE SHEET  (one block only)
# ──────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* ---------- Page background ---------- */
    html, body, [data-testid="stAppViewContainer"] {
        height: 100%;
        background: linear-gradient(130deg,#f1f5f8 0%,#eef2f7 100%) !important;
    }

    /* ---------- Title ---------- */
    .tg-title{
        text-align:center;
        font-size:2.2rem;
        font-weight:700;
        color:#0094ff;
        margin:2.5rem 0 1rem 0;
    }

    /* ---------- Chips menu ---------- */
    .chip-menu{
        display:flex;
        flex-wrap:wrap;
        gap:.5rem;
        justify-content:center;
        margin-bottom:1.5rem;
    }
    .chip{
        background:#ffffff;
        padding:.55rem 1.1rem;
        font-size:1rem;
        border:none;
        border-radius:1.3rem;
        color:#0094ff;
        cursor:pointer;
        box-shadow:0 1px 4px rgba(0,0,0,.05);
        transition:all .15s ease;
    }
    .chip:hover{background:#e8f4ff;color:#0072d4;}

    /* ---------- Message bubbles ---------- */
    .msg-row{display:flex;align-items:flex-end;margin-bottom:1rem;animation:fade .3s;}
    .msg-row.user{flex-direction:row-reverse;}
    .bubble{
        max-width:75%;
        padding:12px 18px;
        border-radius:1.1rem;
        font-size:1.05rem;
        line-height:1.4;
        box-shadow:0 2px 8px rgba(0,0,0,.04);
    }
    .bot   .bubble{background:#ffffff;border-bottom-left-radius:0;color:#222;}
    .user  .bubble{background:#dffbe2;border-bottom-right-radius:0;color:#222;}

    /* ---------- Avatar ---------- */
    .avatar{
        width:34px;height:34px;
        border-radius:50%;display:flex;align-items:center;justify-content:center;
        font-weight:600;font-size:1.1rem;color:#fff;margin:0 .5rem;
    }
    .bot  .avatar{background:#0094ff;}
    .user .avatar{background:#34c759;}

    /* ---------- Input bar ---------- */
    .input-wrapper{position:fixed;bottom:0;left:0;width:100%;padding:.8rem;background:transparent;}
    .input-inner{
        max-width:420px;margin:0 auto;display:flex;gap:.5rem;
    }
    /* remove Streamlit default styling */
    .stTextInput>div>div>input{
        border:1px solid #cfd8e3;border-radius:2rem;padding:.6rem 1rem;
    }

    /* ---------- Animation ---------- */
    @keyframes fade{from{opacity:0;transform:translateY(6px);}to{opacity:1;transform:none;}}
    @media (max-width:600px){
        .bubble{max-width:90%;}
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ──────────────────────────────────────────────────
# STATE INITIALIZATION
# ──────────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# ──────────────────────────────────────────────────
# TITLE
# ──────────────────────────────────────────────────
st.markdown("<div class='tg-title'>💬 Customer Support Bot</div>", unsafe_allow_html=True)

# ──────────────────────────────────────────────────
# ACTION CHIPS
# ──────────────────────────────────────────────────
MENU_OPTIONS = [
    "Track my order",
    "Return an item",
    "Shipping info",
    "Payment methods",
    "Contact support",
    "Refund status",
    "Product availability",
]

st.markdown("<div class='chip-menu'>", unsafe_allow_html=True)
for option in MENU_OPTIONS:
    if st.button(option, key=f"chip_{option}", help=option):
        st.session_state.chat_history.append(("You", option))
        reply = detect_intent_texts(option, session_id=st.session_state.session_id)
        st.session_state.chat_history.append(("Bot", reply))
st.markdown("</div>", unsafe_allow_html=True)

# ──────────────────────────────────────────────────
# CHAT LOG
# ──────────────────────────────────────────────────
if st.session_state.chat_history:
    for speaker, text in st.session_state.chat_history:
        role = "user" if speaker == "You" else "bot"
        avatar_char = "U" if speaker == "You" else "🤖"
        st.markdown(
            f"""
            <div class='msg-row {role}'>
                <div class='avatar'>{avatar_char}</div>
                <div class='bubble'>{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.markdown(
        """
        <p style='text-align:center;margin-top:3rem;color:#666;font-size:1.1rem;'>
            How can I help you today?
        </p>
        """,
        unsafe_allow_html=True
    )

# ──────────────────────────────────────────────────
# INPUT BAR
# ──────────────────────────────────────────────────
def handle_submit():
    msg = st.session_state.get("user_input", "").strip()
    if msg:
        st.session_state.chat_history.append(("You", msg))
        reply = detect_intent_texts(msg, session_id=st.session_state.session_id)
        st.session_state.chat_history.append(("Bot", reply))
        st.session_state.user_input = ""

st.markdown("<div class='input-wrapper'><div class='input-inner'>", unsafe_allow_html=True)
st.text_input("Type your message", placeholder="Type your message...",
              key="user_input", label_visibility="collapsed",
              on_change=handle_submit)
st.markdown("</div></div>", unsafe_allow_html=True)
