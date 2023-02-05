import os
import openai
import gradio as gr
import webbrowser

url = "http://127.0.0.1:7860"
webbrowser.open(url)

# if you have OpenAI API key as an environment variable, enable the below
openai.api_key = os.getenv("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")

# if you have OpenAI API key as a string, enable the below
openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "Ask Anything..."


def openai_create(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=[" Human:", " AI:"]
    )

    return response.choices[0].text


def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>Hello! This is Your AI Assistant. How can I help you...? </center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])
    gr.Markdown("""<h><bottom><center>Developed By: Ali Jan Khoso </bottom><center></h1>
        """)

block.launch(share=True)
