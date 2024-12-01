"""
This module defines configuration settings for the Streamlit-based chatbot application.

It includes paths to essential files, UI settings, model parameters, and 
other constants used throughout the application.

Configuration Options:

- INFO_PATH: Path to the YAML file containing personal information for the chatbot.
- PROMPT_PATH: Path to the text file containing the initial prompt for the language model.
- LOGO_PATH: Path to the image file used as the chatbot's logo.
- CSS_PATH: Path to the CSS file for customizing the chatbot's appearance.
- DISCLAIMER_PATH: Path to the text file containing the disclaimer.
- USER_AVATAR: Path to the image file used as the user's avatar in the chat.
- SYSTEM_AVATAR: Path to the image file used as the chatbot's avatar in the chat.
- WEBSITE_URL: URL of the website to be linked in the chatbot interface.
- GEMINI_MODEL: Name of the Gemini Pro model to use (e.g., 'gemini-1.5-pro').
- WELCOME_MESSAGE: Initial message displayed by the chatbot.
- WAITING_MESSAGE: Message displayed when the chatbot is busy.
- VERSION_NUMBER: Version number of the chatbot application.
- CHATBOT_NAME: Name of the chatbot.
- AUTHOR: Name or pseudonym of the chatbot's creator.

Customization:

Modify the values of these variables to customize the chatbot's behavior, 
appearance, and content.
"""

INFO_PATH = "./model_data/information.yaml"
PROMPT_PATH = "./model_data/prompt.txt"
LOGO_PATH = "./public/logo_with_name.png"
CSS_PATH = "./public/custom.css"
DISCLAIMER_PATH = "./disclaimer.txt"

USER_AVATAR = './public/user_icon.png'
SYSTEM_AVATAR = './public/system_icon.png'

WEBSITE_URL = "https://webiste.me/"

GEMINI_MODEL = 'gemini-1.5-flash' # gemini-1.5-pro

WELCOME_MESSAGE = """Hi, welcome! I'm your personal chatbot 🙂 Feel free to ask me anything"""
WAITING_MESSAGE = """At the moment I am pretty busy answering question. Why don't we
                        grab a coffee and continue the conversation later?"""
VERSION_NUMBER = "v0.0.1"
CHATBOT_NAME = "Chatbot"
AUTHOR = "Your personal chatbot"
