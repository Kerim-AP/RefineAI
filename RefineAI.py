import streamlit as st
import openai

st.set_page_config(page_title="RefineAI", layout="wide")

st.image("logo.jpg", width=100)
st.title("RefineAI ✨ – AI-Powered Essay Rewriter")

api_key = st.text_input("🔐 Enter your OpenAI API Key", type="password")

text_input = st.text_area("✍️ Paste your text here:")

if st.button("🔁 Paraphrase"):
    if not api_key:
        st.warning("Please enter your OpenAI API key.")
    elif not text_input.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Paraphrasing..."):
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You're a professional writing assistant."},
                    {"role": "user", "content": f"Paraphrase this: {text_input}"}
                ]
            )
            paraphrased = response.choices[0].message.content
            st.success("✅ Done!")
            st.text_area("🪄 Refined Output:", paraphrased, height=200)
