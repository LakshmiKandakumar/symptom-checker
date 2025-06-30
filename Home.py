import os
import streamlit as st
import textwrap
import requests
from groq import Groq
from streamlit_lottie import st_lottie
from dotenv import load_dotenv  # ✅ Import dotenv

# ✅ Load the .env file
load_dotenv()

st.set_page_config(page_title="Symptom Checker", page_icon="👨‍⚕️")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.title(" :rainbow[Symptom Checker]")

# side bar
with st.sidebar:
    try:
        lottie_url = "https://lottie.host/ba10b921-fb9f-4423-96ff-56e4dce1e02d/X9Qm4rbbCM.json"
        lottie_data = requests.get(lottie_url).json()
        st_lottie(lottie_data, key="sidebar-animation", height=300, width=300)
    except Exception as e:
        st.sidebar.error(f"Error loading animation: {e}")

# ✅ Use API key from .env
groq_api_key = os.getenv("GROQ_API_KEY")
groq_client = Groq(api_key=groq_api_key)

if "chat" not in st.session_state:
    st.session_state.chat = groq_client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an information extraction assistant."
                    " A user will describe their symptoms, "
                    "and you will provide possible medical conditions that match those symptoms. "
                    "Please respond with possible conditions and appropriate medical advice."
                    "Additionally, if the symptoms indicate a serious condition, suggest that the user see a doctor. "
                    "Use simple language and try to be interactive"
                    "Do not answer any other questions apart from these."
                ),
            }
        ],
        model="llama3-70b-8192"
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.chat_message("assistant", avatar="👨‍⚕️"):
    st.markdown("Welcome! I am a medical symptom checker bot. Describe your symptoms, and I will provide possible conditions and advice. For serious symptoms, I'll suggest seeing a doctor.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How are you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    try:
        response = groq_client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama3-70b-8192"
        )
        with st.chat_message("assistant", avatar="👨‍⚕️"):
            st.markdown(response.choices[0].message.content)
        st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})
    except Exception as e:
        with st.chat_message("assistant", avatar="👨‍⚕️"):
            st.markdown("I can't help you with that.")
