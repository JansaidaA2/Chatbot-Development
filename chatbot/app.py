from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.set_page_config(page_title="ChatGPT-like Assistant", layout="wide")
st.title("🧠 LangChain ChatGPT-like Assistant")

# Initialize memory in session state
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

# Setup LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", streaming=True)

# Use ConversationChain WITHOUT custom prompt
conversation = ConversationChain(
    llm=llm,
    memory=st.session_state.memory,
    verbose=True
)

# Input
user_input = st.chat_input("Ask me anything...")

# Display history
for message in st.session_state.memory.chat_memory.messages:
    with st.chat_message(message.type):
        st.markdown(message.content)

# Run if there's input
if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        response = conversation.predict(input=user_input)
        st.markdown(response)

