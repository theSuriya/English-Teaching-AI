import streamlit as st
import google.generativeai as genai
import os
import requests

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro-latest")
prompt = """
you are a english teacher.so, understand the following Tanglish query and give a correct English sentance with proper grammar:
Tanglish query: {tamil_text}
"""

prompt_1 = """
You are an English teacher. Please understand the following Tanglish query and provide a correct English sentence with correct grammar:
input:
Tanglish query: {tamil_text}

example input 1: amma kita pasikidhu nu english la epdi sollanum?
example Output 1: mom, i am hungry

example input 2: teacher kita bathroom poonu tu epdi kekuradhu
example Output 2: Excuse me, teacher. May I please be excused to use the restroom?

note: output must in one line
"""

def generate_response(input_text, prompt):
  query = prompt.format(tamil_text=input_text)
  # model = genai.GenerativeModel("gemini-1.5-pro-latest")
  response = model.generate_content(query)
  return response.text

def txt2speech(text):
  API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
  api_token = os.getenv('HUGGING_FACE')
  headers = {"Authorization": f"Bearer {api_token}"}
  payloads = {'inputs': text}

  response = requests.post(API_URL, headers=headers, json=payloads)
  
  with open('audio_answer.mp3', 'wb') as file:
      file.write(response.content)
  

st.title("🏫 English Teaching AI")
example_text = "park ku pooga epdi english la vazhi kekuradhu?"
user_query = st.text_area("Type Tamil or Tanglish sentance", value=example_text)
submit = st.button("Analyze")
if submit:
    with st.spinner("### 🤖Processing..."):
        answer = generate_response(user_query, prompt_1)
        txt2speech(f"In English: You can say, {answer}")
        st.audio("audio_answer.mp3")
    with st.spinner("### 🤖Analyzing your Query..."):
        response = generate_response(user_query, prompt)
        st.markdown(response)
