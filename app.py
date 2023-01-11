import openai
import streamlit as st

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

st.title("Pātai Bot Aotearoa")

history = st.empty()

message = st.text_input(prompt)
if message:
    history, output = chatgpt_clone(message, history)
    st.write(start_sequence + output)
