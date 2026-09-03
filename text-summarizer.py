from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.set_page_config(
    page_title="AI Text Summarizer",
    layout="centered"
)

st.markdown("""
<style>

    .main {
        padding-top: 2rem;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .summary-box {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.3);
        margin-top: 20px;
    }

    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 50px;
        font-size: 17px;
        font-weight: 600;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

st.markdown(
    '<div class="title"> AI Text Summarizer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Turn lengthy text into clear, concise summaries using AI.</div>',
    unsafe_allow_html=True
)

st.subheader("Enter your text")

user = st.text_area(
    "Paste your text below",
    height=250,
    placeholder="Paste an article, paragraph, notes, or any lengthy text here..."
)

if st.button("Summarize Text"):

    if user.strip() == "":
        st.warning("Please enter some text first.")

    else:
        prompt = f"""
        Summarize the following text clearly and concisely.

        Keep the main ideas and important information.
        Remove unnecessary details.

        Text:
        {user}
        """

        with st.spinner("AI is generating your summary..."):
            result = model.invoke(prompt)

        summary = result.content[0]["text"]

        st.subheader("Summary")

        st.markdown(
            f"""
            <div class="summary-box">
                {summary}
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown(
    '<div class="footer">Built with Python • Gemini • LangChain • Streamlit</div>',
    unsafe_allow_html=True
)
