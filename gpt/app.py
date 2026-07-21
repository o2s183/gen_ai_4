from langchain_community.llms import Ollama 
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

#streamlit code
st.title("where should we begin?")
input_text = st.text_input("Enter your prompt here:")


llm  = Ollama(model="gemma2:latest")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser


#validation based outputw
if input_text:
    st.write(chain.invoke({"input": input_text}))