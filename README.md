# 🤖 AI-Chatbot

This repository contains a simple AI chatbot built using OpenRouter's GPT-3.5-turbo model and Gradio for the web interface.

## ✨ Features

- 🤝 Interact with OpenRouter's GPT-3.5-turbo model.
- 🌐 Web-based interface using Gradio.
- 📝 Example prompts to get started.

## 🛠️ Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/kshanxs/AI-Chatbot.git
    cd AI-Chatbot
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Set your OpenRouter API key:
    Replace `"YOUR_OPENROUTER_API_KEY"` in the `app.py` file with your actual OpenRouter API key.

## 🚀 Usage

Run the script to start the chatbot interface:
```bash
python app.py
```

The Gradio interface will launch, allowing you to interact with the chatbot. You can use example prompts such as:
- "Poem on nature"
- "Explain black hole"
- "Python program palindrome"

## 📝 Notes

- Ensure you have a valid OpenRouter API key to use the chatbot.
- The chatbot uses the `gpt-3.5-turbo` model with a maximum token limit of 1024 and a temperature of 0.7 for generating responses.
