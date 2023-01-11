import os
import openai
import streamlit as st
import gradio as gr

api_key = os.environ["OPENAI_API_KEY"]
#openai.api_key = api_key

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = " "

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
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

st.set_page_config(page_title="My Gradio App", layout="wide")

if st.button('Run App'):
    block = gr.Blocks()

    with block:
        gr.Markdown("""<h1><center>Pātai Bot Aotearoa</center></h1>
        """)
        chatbot = gr.Chatbot()
        message = gr.Textbox(placeholder=prompt)
        state = gr.State()
        submit = gr.Button("SEND")
        submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

    block.launch(share=True)
