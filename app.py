from langchain_ollama.chat_models import ChatOllama
import streamlit as st

# Adding History

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from pydantic import BaseModel


llm = ChatOllama(model="deepseek-r1:8b")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an AI chatbot having a conversation with a human. Use the following context to understand the human question and answer English and Arabic. Include emojis in your answer. ",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        (   "human", 
            "{input}"
        ),
    ]
)

chain = prompt | llm

history = StreamlitChatMessageHistory()

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

# Add custom CSS for RTL direction
st.markdown(
    """
    <style>
    body {
        direction: rtl;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("نظام الذكاء الاصطناعي لكلية القيادة والأركان")


for message in st.session_state["langchain_messages"]:
    role = "user" if message.type == "human" else "assistant"
    with st.chat_message(role):
        st.markdown(
            f'<div style="text-align: right; direction: rtl;">{message.content}</div>',
            unsafe_allow_html=True
        )

question = st.chat_input("Your Question")
if question:
    with st.chat_message("user"):
        st.markdown(
            f'<div style="text-align: right; direction: rtl;">{question}</div>',
            unsafe_allow_html=True
        )
    response = chain_with_history.stream(
        {"input": question}, config={"configurable": {"session_id": "any"}}
    )
    with st.chat_message("assistant"):
        st.write_stream(response)
