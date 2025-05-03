from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama


import  streamlit as st
import os
from dotenv import load_dotenv


## Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


### Prompt template

prompt= ChatPromptTemplate.from_messages(
    [
        ("system", "You are a assistant. Please provide response to user questions"),
        ("user", "Question:{question}")
    ]
)


## streamlit framework

st.title('Langchain with OLlama2 API')
input_text = st.text_input("Search the topic you want ")

## Lets call Ollama Llama2  LLM

llm = Ollama(model = "llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))