import os 
import streamlit as st 

st.set_page_config(page_title='Essay Writer', layout='wide')

with st.sidebar:
    API=st.text_input("Enter Your OpenAI API", type="password")
    
    if API:
        st.balloons()
        
    st.text('Made by Muhammad Umer')
        
os.environ['OPENAI_API_KEY'] = API

# App framework
st.title('🦜🔗 Essay Writer')
if API:
    prompt = st.text_input('Enter your topic here') 
else:
    st.warning("Open the sidebar and enter your OpenAI API key")

    
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper 

# Prompt templates


essay_template = PromptTemplate(
    input_variables = ['topic'], 
    template='write me an essay on the topic {topic}'
)

# Memory 
essay_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')

# Llms
if API:
    llm = OpenAI(temperature=0.9) 
    essay_chain = LLMChain(llm=llm, prompt=essay_template, verbose=True, output_key='essay', memory=essay_memory)

# Show stuff to the screen if there's a prompt
    if prompt: 
        essay = essay_chain.run(prompt)
        st.write(essay) 
        

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

