# Personal Chatbot

This is a simple Streamlit-based chatbot that uses Google Gemini Pro as its language model. It's designed to be easily customizable with your own personal information and deployed as an open-source project.

**See a live example of this chatbot in action:** [LLMassi](https://massimilianobotticelli.me/llmassi/)

## Features

* **Personalized Responses:** The chatbot is initialized with your personal information (from `information.yaml`) to provide more relevant and engaging conversations.
* **Persistent Chat History:** Streamlit's `st.session_state` is used to maintain chat history within a session.
* **Customizable Prompt:** You can modify the `prompt.txt` file to guide the chatbot's behavior and responses.
* **Easy Deployment:** The chatbot can be easily deployed using Streamlit's sharing platform or other deployment methods.
* **Customizable UI:**  The chatbot's appearance can be customized using CSS (`custom.css`) and by providing your own logo (`logo_with_name.png`) and avatar icons (`user_icon.png`, `system_icon.png`).

## Getting Started

### Prerequisites

* **Python 3.11 or higher**
* **A Google Cloud Project**
* **An API key for Gemini** ([Google AI for Developers](https://ai.google.dev/))
* **Poetry** (for dependency management)

### Installation

1. **Clone the repository:**
   ```bash
   git clone [invalid URL removed]
   ```

2. **Install dependencies using Poetry:**

   ```bash
   poetry install
   ```

3. **Set up your environment variables:**

   * Create a `.env` file in the root directory.
   * Add your Gemini Pro API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

4. **Configure the chatbot:**

   * Update `information.yaml` with your personal information (see the example provided).
   * Customize the `prompt.txt` file to define the chatbot's initial system prompt.
   * (Optional) Modify `config.py` if you want to change any of the default settings (e.g., `CHATBOT_NAME`, `VERSION_NUMBER`, `WEBSITE_URL`, etc.).

### Running the Chatbot

```bash
poetry run streamlit run app.py
```

## Customization

* **Personal Information:** Update `information.yaml` with your own details.
* **Prompt Engineering:** Modify `prompt.txt` to fine-tune the chatbot's responses.
* **Appearance:** 
    * Replace `logo_with_name.png` with your own logo.
    * Update `custom.css` to change the styling of the chatbot.
    * Replace `user_icon.png` and `system_icon.png` with your preferred avatar icons.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

## About the Author

This chatbot was created by **Massimiliano Botticelli**. You can find more about me and my work here:

* [**Personal Website**](https://massimilianobotticelli.me/)
* [**Linkedin**](https://www.linkedin.com/in/massimilianobotticelli/)
