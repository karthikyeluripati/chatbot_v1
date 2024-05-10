from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


#Langsmith tracking
os.environ["LANGCHAIN_TRACKING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user queries"),
        ("user","question:{question}")
    ]
)

#stramlit framework
st.title('Langchain Demo with llama2')
input_text=st.text_input("Search the topic u want")

#LLAMA 2 LLM
llm=Ollama(model="llama2")
output_parser=StrOutputParser()

chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
