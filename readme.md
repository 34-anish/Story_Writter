Inspired by: https://www.youtube.com/watch?v=MlK6SIjcjE8&t=1069s
```
# Dependencies
import os
from secret_key import openapi_key

import streamlit as st
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = openapi_key

#APP Framework
st.title("HELLO WORLD")
prompt = st.text_input("PLUG IN")

#LLMS
llm = OpenAI(temperature= 0.9)

if prompt:
    response = llm(prompt)
    st.write(response)
![f6256aa3952ec637dca0b7b5b53c5c71.png](./_resources/f6256aa3952ec637dca0b7b5b53c5c71.png)
```
In this code we simply deployed the model with the streamlit with the openai being called on the backend
![b07dbc7b933f45fc6c4e040a1b1c63a1.png](./_resources/b07dbc7b933f45fc6c4e040a1b1c63a1.png)
**Template**
```
# Dependencies
import os
from secret_key import openapi_key

#OPENAI
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY'] = openapi_key

#APP Framework
st.title("HELLO WORLD")
prompt = st.text_input("PLUG IN")

title_template = PromptTemplate(
    input_variables=['topic'],
    template='write me a sexy video title about {topic}'
)
#LLMS
llm = OpenAI(temperature= 0.9)
title_chain = LLMChain(llm=llm,prompt=title_template,verbose =True)

if prompt:
    response = title_chain.run(prompt)
    st.write(response)
```
Now there is a change in terms of how the input can be passed
**CHAINS**
![d8f4ecb1e5d29d6638df46cb60d17989.png](./_resources/d8f4ecb1e5d29d6638df46cb60d17989.png)
*Simple Sequential Chain* to encorporate the stacking of the chains
```
# Dependencies
import os
from secret_key import openapi_key

#OPENAI
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SimpleSequentialChain

os.environ['OPENAI_API_KEY'] = openapi_key

#APP Framework
st.title("Youtube Title Recommender")
prompt = st.text_input("PLUG IN THE TITLE FOR THE CONTENT")

title_template = PromptTemplate(
    input_variables=['topic'],
    template='write me a youtube title about {topic}'
)

script_template = PromptTemplate(
    input_variables=['title'],
    template='write me a youtube script based on the title: {title}'
)
#LLMS
llm = OpenAI(temperature= 0.9)
title_chain = LLMChain(llm=llm,prompt=title_template,verbose =True)
script_chain = LLMChain(llm=llm,prompt=script_template,verbose =True)
sequential_chain = SimpleSequentialChain(chains=[title_chain,script_chain],verbose=True)


if prompt:
    response = sequential_chain.run(prompt)
    st.write(response)
```
The problem with the simple sequential chain is the prompt->title-> script but the title is unlikely to come up
![1625484c2e789811fe982d51200f96a9.png](./_resources/1625484c2e789811fe982d51200f96a9.png)
**Final Project**
`streamlit run main.py` runs the project
![353771ebe42c763e5f36d2a94d4ad489.png](./_resources/353771ebe42c763e5f36d2a94d4ad489.png)
![ca2f2ea23caf8f74c5bdfb1fef34f069.png](./_resources/ca2f2ea23caf8f74c5bdfb1fef34f069.png)