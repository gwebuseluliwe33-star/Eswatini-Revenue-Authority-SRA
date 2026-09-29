import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

st.title("Assignment Bot")

with st.sidebar:
    user_key = st.text_input("Gemini API key", type="password")
    st.markdown("[Get a key](https://aistudio.google.com/apikey)")

api_key = user_key or os.environ.get("GEMINI_API_KEY")
if not api_key:
    st.info("Enter your Gemini API key in the sidebar to start chatting.")
    st.stop()

client = genai.Client(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Say something"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    history = [
        types.Content(
            role="user" if m["role"] == "user" else "model",
            parts=[types.Part(text=m["content"])],
        )
        for m in st.session_state.messages[:-1]
    ]

    with st.chat_message("assistant"):
        try:
            chat = client.chats.create(model="gemini-3.1-flash-lite", history=history)
            response = chat.send_message(prompt)
            reply = response.text or ""
        except Exception as e:
            reply = f"Error: {e}"
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
