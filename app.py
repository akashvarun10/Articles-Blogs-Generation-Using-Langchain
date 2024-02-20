import streamlit as st
from langchain.prompts import PromptTemplate
# from langchain.llms import CTransformers
from langchain_community.llms import CTransformers



## function to get response form LLAMA2 model
config={'max_new_tokens':256, 'temperature':0.01}
def getLLama2Response(input_text, no_words, style):
    # llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',model_file='ggml-model.bin',model_type='llama',config=config)
    llm = CTransformers(model='marella/gpt-2-ggml',config=config)
    
    ##Prompt Template

    template = """
            Write a blog for {style} job profile for a topic {input_text}
            within {no_words} words.
            """
    
    prompt = PromptTemplate(input_variables=['style', 'input_text', '=no_words)'], template=template)

    # generate response from llama2 model

    response= llm(prompt.format(style=style, input_text=input_text, no_words=no_words))
    print(response)
    return response
                                         






st.set_page_config(page_title="Generate Articles/ Blogs", page_icon="🔗", layout="centered", initial_sidebar_state="collapsed")

st.header("Generate Articles/ Blogs")

input_text = st.text_input("Enter the topic")

## Creating 2 mores columns for additional 2 fields 

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("Enter the number of words")
with col2:
    style = st.selectbox("Writing the Articles/Blog for",
                         (' Researchers','Students','Data Scientists','General Audience'),index=0)
    
submit = st.button("Generate")

## Final response 

if submit:
    st.write(getLLama2Response(input_text, no_words, style))



