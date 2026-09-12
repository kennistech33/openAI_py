

import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Kennistech AI Terminal")
st.title("KENNISTECH AI TERMINAL")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

if "messages" not in st.session_state:
    st.session_state.messages = []

# show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# input box at bottom
question = st.chat_input("You >")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    try:
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=st.session_state.messages
        )
        answer = response.choices[0].message.content
    except Exception as e:
        answer = f"[Error] {e}"

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)