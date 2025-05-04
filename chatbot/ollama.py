from langchain_community.chat_models import ChatOllama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

import streamlit as st
import os

# Streamlit UI setup
st.set_page_config(page_title="Ollama Chat Assistant", layout="wide")
st.title("🧠 LangChain Chat with Ollama")

# Memory init
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

# LLM setup with Ollama
llm = ChatOllama(model="gemma3:1b")  # or "llama2", "gemma", etc.

# ConversationChain
conversation = ConversationChain(
    llm=llm,
    memory=st.session_state.memory,
    verbose=True
)

# Chat interface
user_input = st.chat_input("Ask me anything...")

# Display history
for message in st.session_state.memory.chat_memory.messages:
    with st.chat_message(message.type):
        st.markdown(message.content)

# Process input
if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        response = conversation.predict(input=user_input)
        st.markdown(response)
