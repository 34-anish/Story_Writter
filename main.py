# Dependencies
import os
from secret_key import openapi_key

#OPENAI
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SequentialChain

os.environ['OPENAI_API_KEY'] = openapi_key

#APP Framework
st.title("Story Writer")
prompt = st.text_input("PLUG IN THE TITLE FOR THE CONTENT")

title_template = PromptTemplate(
    input_variables=['topic'],
    template='write me a title about {topic}'
)

script_template = PromptTemplate(
    input_variables=['title'],
    template='write me a short story based on the title: {title}'
)
#LLMS
llm = OpenAI(temperature= 0.9)
title_chain = LLMChain(llm=llm,prompt=title_template,verbose =True,output_key = 'title')
script_chain = LLMChain(llm=llm,prompt=script_template,verbose =True,output_key = 'script')
sequential_chain = SequentialChain(chains=[title_chain,script_chain], input_variables=['topic'],output_variables = ['title','script'])

if prompt:
    response = sequential_chain({'topic' :prompt})
    st.write(response['title'])
    st.write(response['script'])