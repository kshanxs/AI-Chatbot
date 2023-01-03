import openai
import gradio as gr

# API Key

openai.api_key = "API_KEY"

# OpenAI Chat Bot

def openai_chat(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

# ChatBot Function

def chatbot(input, history=[]):
    output = openai_chat(input)
    history.append((input, output))
    return history, history

# Examples to Try

try_examples = [
    "Poem on nature",
    "Quote on friends",
    "Explain black hole",
    "Python program palindrome",
    "Essay on India",
    "Suggest me best anime to watch",
    "quick sort algo c++",
    "Theory of relativity?",
]
# Gradio User Interface

text_in_out = gr.Interface(
    title= "AI Byte",
    examples = try_examples,
    description="Let's type something for me😊",
    fn = chatbot,
    inputs= ["text", 'state'],
    outputs= ["chatbot",'state'],
    allow_flagging="never",
    )

# Launch Function

frame = gr.TabbedInterface([text_in_out], ["Hello"])

if __name__ == "__main__":
    frame.launch(debug = True, share = True)
