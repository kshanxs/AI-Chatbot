import openai
import gradio as gr

# Set the API key for OpenAI
openai.api_key = "API_KEY"

# Function to interact with OpenAI's GPT-3 model
def openai_chat(prompt):
    # Create a completion using the specified engine and parameters
    completions = openai.Completion.create(
        engine="text-davinci-003",  # The model to use
        prompt=prompt,              # The input prompt
        max_tokens=1024,            # Maximum number of tokens to generate
        n=1,                        # Number of completions to generate
        temperature=0.5,            # Sampling temperature
    )

    # Extract the message from the completion response
    message = completions.choices[0].text
    return message.strip()

# Function to handle the chatbot interaction
def chatbot(input, history=[]):
    # Get the response from the OpenAI model
    output = openai_chat(input)
    # Append the input and output to the history
    history.append((input, output))
    return history, history

# List of example prompts to try with the chatbot
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

# Create a Gradio interface for the chatbot
text_in_out = gr.Interface(
    title="AI Byte",                # Title of the interface
    examples=try_examples,          # Example prompts to display
    description="Let's type something for me😊",  # Description of the interface
    fn=chatbot,                     # Function to call for generating responses
    inputs=["text", 'state'],       # Input types: text and state
    outputs=["chatbot", 'state'],   # Output types: chatbot and state
    allow_flagging="never",         # Disable flagging of responses
)

# Create a tabbed interface with the Gradio interface
frame = gr.TabbedInterface([text_in_out], ["Hello"])

# Launch the Gradio interface
if __name__ == "__main__":
    frame.launch(debug=True, share=True)
