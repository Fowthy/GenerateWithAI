import streamlit as st
import replicate

st.title("AI Text Generator")
st.subheader("an AI model that generates creative text")

# Radio button for text type selection
selected_text_type = st.radio('Select Text Type', ["Poem", "Lyrics", "Story", "Other"])

# Text input for the subject
subject = st.text_input("Enter the subject here", "steamed hams")

# Dictionary for text type details
text_type_details = {
    "Poem": "Can you write me a poem about",
    "Lyrics": "Can you write me lyrics about",
    "Story": "Can you write me a story about",
    "Other": "Can you write about"
}

# Construct the prompt based on the text type and subject
prompt = f"{text_type_details[selected_text_type]} {subject}?"


if st.button('Generate Text'):
    placeholder = st.empty()
    client = replicate.Client(api_token=st.secrets.replicate_api_token)
    output = client.run(
        "mistralai/mistral-7b-instruct-v0.1:5fe0a3d7ac2852264a25279d1dfb798acbc4d49711d126646594e212cb821749",
        input={
            "debug": False,
            "top_k": 10,
            "top_p": 0.5,
            "prompt": prompt,
            "temperature": 0.5,
            "max_new_tokens": 1000,
            "min_new_tokens": -1,
            "prompt_template": "{prompt}",
            "repetition_penalty": 1.25
        }
    )
    text = ''
    # Stream the output word by word
    for word in output:
        text += word
        placeholder.text(text)