# Bring in deps
import os 
from openai_api import API_KEY 

import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper 

os.environ['OPENAI_API_KEY'] = API_KEY

# App framework
st.title('🦜🔗 Essay Writer')
prompt = st.text_input('Plug in your prompt here') 

# Prompt templates
essay_template = PromptTemplate(
    input_variables = ['topic'], 
    template='write me an essay on the topic {topic}'
)



# Memory 
essay_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')



# Llms
llm = OpenAI(temperature=0.9) 
essay_chain = LLMChain(llm=llm, prompt=essay_template, verbose=True, output_key='essay', memory=essay_memory)



# Show stuff to the screen if there's a prompt
if prompt: 
    essay = essay_chain.run(prompt)
    
    

    st.write(essay) 
    

    with st.expander('Essay Writing History'): 
        st.info(essay_memory.buffer)

