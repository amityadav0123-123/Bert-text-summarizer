import streamlit as st
from transformers import pipeline

# Load Summarization Model
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

# Custom Background
def set_bg():
    page_bg = """
    <style>
    body {
        background: url('https://source.unsplash.com/1600x900/?sea') no-repeat center center fixed;
        background-size: cover;
        color: white;
    }
    .stTextArea, .stTextInput {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #008CBA;
        color: white;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

set_bg()

# Streamlit App UI
st.title("📜 Text Summarization using BERT 🤖")
st.write("Enter a long paragraph, and the AI will summarize it!")

# User Input
text = st.text_area("✍️ Enter text to summarize:", height=200)

# Summarization Button
if st.button("Summarize 🔥"):
    if text.strip():
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
        st.success(f"**📝 Summary:** {summary[0]['summary_text']}")
    else:
        st.warning("⚠️ Please enter some text to summarize.")
