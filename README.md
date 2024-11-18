# Thoughtful-AI Chatbot

This project is a simple chatbot application powered by multiple AI model providers. The chatbot provides answers based on a predefined dataset and can fall back to a generic response in case of API errors.

## Features

- **Model Provider Support**: Choose between multiple AI model providers (e.g., OpenAI, Groq, Cerebras, Grok-2).
- **API Key Integration**: Securely input and store API keys to authenticate requests to the AI models.
- **Chat Interface**: A conversational interface that allows users to interact with the chatbot.

## Requirements

- Python 3.x
- Streamlit
- OpenAI Python SDK

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Satti-Gowtham/thoughtful-ai-chatbot.git
cd thoughtful-ai-chatbot
```
2. Install dependencies:
```bash
    pip install -r requirements.txt
```
3. Obtain an API key for the model provider you want to use (e.g., OpenAI, Groq, Cerebras, or Grok-2).

## Configuration

- The application uses **Streamlit** to create an interactive web interface.
- The **model provider** and **API key** can be configured in the sidebar of the app.
- The default model provider is set to **OpenAI**, and the API key should be entered in the sidebar when the app is running.

## Usage

1. Run the app:
```bash
streamlit run app.py
```
2. Open the app in your web browser.
3. Select a model provider, enter your API key, and start chatting with the chatbot.