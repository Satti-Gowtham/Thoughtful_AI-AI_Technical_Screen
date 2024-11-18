import streamlit as st
from util import Util

st.title("Thoughtful-AI Chatbot")

st.session_state.setdefault("model_provider", "OpenAI")
st.session_state.setdefault("base_url", "https://api.openai.com/v1")
st.session_state.setdefault("model", "gpt-4o")
st.session_state.setdefault("api_key", "")
st.session_state.setdefault("messages", [])

st.session_state["helper"] = Util(
    api_key=st.session_state["api_key"],
    base_url=st.session_state["base_url"],
    model=st.session_state["model"]
)

DATASET_PATH = './dataset.json'

# Function to handle model update
def update_config():
    config = {
        "OpenAI": {
            "model": "gpt-4o", 
            "base_url": "https://api.openai.com/v1"
        },
        "Groq": {
            "model": "llama-3.2-3b-preview", 
            "base_url": "https://api.groq.com/openai/v1"
        },
        "Cerebras": {
            "model": "llama3.1-8b", 
            "base_url": "https://api.cerebras.ai/v1"
        },
        "Grok-2": {
            "model": "grok-beta", 
            "base_url": "https://api.x.ai/v1"
        }
    }

    provider = st.session_state["model_provider"]
    if provider in config:
        st.session_state["model"], st.session_state["base_url"] = config[provider].values()

    # Reinitialize the helper with the updated configuration
    st.session_state["helper"] = Util(
        api_key=st.session_state["api_key"],
        base_url=st.session_state["base_url"],
        model=st.session_state["model"]
    )

# Sidebar: Model and API key input
with st.sidebar:
    model_provider = st.selectbox(
        "Please select an AI model provider",
        ("OpenAI", "Groq", "Cerebras", "Grok-2"),
        key="model_provider",
        on_change=update_config
    )
    
    api_key = st.text_input("Enter API key", type="password", key="api_key", on_change=update_config)

helper = st.session_state.get("helper")
dataset = helper.load_dataset(DATASET_PATH)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            stream = helper.get_answer(prompt, dataset['questions'])
            response = st.write_stream(stream)
        except Exception as e:
            response = st.write(e.message)

    
    st.session_state.messages.append({"role": "assistant", "content": response})
