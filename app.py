import requests
import gradio as gr

# Set the API key for OpenRouter
OPENROUTER_API_KEY = "YOUR_OPENROUTER_API_KEY"  # Replace with your OpenRouter API key
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Function to interact with OpenRouter's API
def openrouter_chat(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:7860",
        "X-Title": "AI Byte Chatbot"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 1024,
        "temperature": 0.7
    }

    try:
        response = requests.post(
            f"{OPENROUTER_BASE_URL}/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )

        # Check if response is successful
        if response.status_code != 200:
            return f"Error: API returned status {response.status_code}. Response: {response.text[:500]}"

        result = response.json()

        # Check if response has expected structure
        if 'choices' not in result or not result['choices']:
            return f"Error: No choices in response. Full response: {result}"

        message = result['choices'][0]['message']['content']
        return message.strip()

    except requests.exceptions.Timeout:
        return "Error: Request timed out. Please try again."
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to OpenRouter API. Please check your internet connection."
    except requests.exceptions.RequestException as e:
        return f"Error: Request failed. {str(e)}"
    except Exception as e:
        return f"Error: Unexpected error occurred. {str(e)}"

# Simple chatbot function for Gradio 3.x
def chat_function(message):
    if message.strip() == "":
        return "Please enter a message."

    response = openrouter_chat(message)
    return response

# Create a simple Gradio interface compatible with version 3.x
demo = gr.Interface(
    fn=chat_function,
    inputs=gr.Textbox(label="Your Message", placeholder="Type your message here..."),
    outputs=gr.Textbox(label="AI Response"),
    title="AI Byte",
    description="Let's type something for me😊",
    examples=[
        "Poem on nature",
        "Quote on life",
        "Explain black hole",
        "Python program palindrome",
        "India's history",
        "What is AI?",
        "What is machine learning?",
        "Suggest me best anime to watch",
        "quick sort algo c++",
        "Theory of relativity?"
    ],
    allow_flagging="never"
)

# Launch the Gradio interface
if __name__ == "__main__":
    demo.launch(debug=True, share=True)

