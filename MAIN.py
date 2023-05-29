# Bring in deps
import os 


import streamlit as st 

API=st.text_input("Enter Your OpenAI API", type="password")
os.environ['OPENAI_API_KEY'] = API

# App framework
st.title('🦜🔗 Essay Writer')
prompt = st.text_input('Plug in your prompt here') 
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


st.info("Error asks to enter the API key. It will disappear automatically once you enter the API Key of Openai.")
st.success("No idea how to get your API key,  well")
if st.button("Press Me"):
    link = '[Youtube](https://www.youtube.com/watch?v=nafDyRsVnXU)'
    st.markdown(link, unsafe_allow_html=True)
# Llms
llm = OpenAI(temperature=0.9) 
essay_chain = LLMChain(llm=llm, prompt=essay_template, verbose=True, output_key='essay', memory=essay_memory)



# Show stuff to the screen if there's a prompt
if prompt: 
    essay = essay_chain.run(prompt)
    
    

    st.write(essay) 
    

    with st.expander('Essay Writing History'): 
        st.info(essay_memory.buffer)

st.info("Error asks to enter the API key. It will disappear automatically once you enter the API Key of Openai.")

