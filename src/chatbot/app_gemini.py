# Import necessary libraries
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import StreamlitChatMessageHistory

import yaml
import config  # Assuming you have a config.py file with your configurations
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load personal context from YAML file
with open(config.INFO_PATH, "r") as file:
    dict_personal_context = yaml.safe_load(file)
    personal_context = yaml.dump(dict_personal_context)

# Load prompt message from file
with open(config.PROMPT_PATH, "r") as file:
    prompt_message = file.read()

# Configure Streamlit page settings
st.set_page_config(
    page_title=f"{config.CHATBOT_NAME}: Chat with me!",
    page_icon="./public/favicon.png",  # Use a built-in emoji or a URL to an image
    menu_items={
        'About': f"""
            {config.CHATBOT_NAME} {config.VERSION_NUMBER}\n
            @ 2024 {config.AUTHOR}. All rights reserved."""
    }
)

# --- Streamlit UI ---

# Display chatbot logo
st.image(config.LOGO_PATH, width=600)

# Load and apply custom CSS
with open(config.CSS_PATH, "r") as f:
    st.markdown(f.read(), unsafe_allow_html=True)

# Add a link to your website
st.markdown(f'<div class="container"><a href="{config.WEBSITE_URL}" class="website-link">Visit my website</a></div>', 
            unsafe_allow_html=True)

# Display disclaimer in an expander
with open(config.DISCLAIMER_PATH, "r") as f:
    disclaimer_text = f.read()

with st.expander("ℹ️ Disclaimer"):
    st.write(disclaimer_text)

# --- LangChain setup ---

# Initialize Gemini language model
model = ChatGoogleGenerativeAI(
    model=config.GEMINI_MODEL,
    temperature=0.4,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Format the prompt with personal context
formatted_prompt = prompt_message.format(personal_context)

# Create a chat prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", formatted_prompt),
        MessagesPlaceholder(variable_name="history"),
        ("user", "{question}"),
    ]
)

# Create a chain with the prompt and model
chain = prompt | model

# Initialize chat message history for Streamlit
msgs = StreamlitChatMessageHistory()

# Create a chain that can use message history
chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: msgs,  # Always return the instance created earlier
    input_messages_key="question",
    history_messages_key="history",
)

# --- Streamlit chat interface ---

# Initialize chat messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {'role': 'assistant', 'content': config.WELCOME_MESSAGE}
    ]

# Display chat messages from history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user", avatar=config.USER_AVATAR).markdown(message["content"])
    else:
        st.chat_message("assistant", avatar=config.SYSTEM_AVATAR).markdown(message["content"])

# Get user input from chat input field
if prompt := st.chat_input("Ask me something 🙂"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=config.USER_AVATAR):
        st.markdown(prompt)

    # Generate response and add it to chat history
    chat_config = {"configurable": {"session_id": "any"}} 

    try:
        response = chain_with_history.invoke({"question": prompt}, chat_config).content
    except Exception as e:  # Catch any exceptions during response generation
        print(f"Error generating response: {e}")  # Print error for debugging
        response = config.WAITING_MESSAGE  # Display a waiting message
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant", avatar=config.SYSTEM_AVATAR):
        st.markdown(response)