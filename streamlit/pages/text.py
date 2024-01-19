import streamlit as st
import replicate

st.title("AI Text Generator")
st.subheader("an AI model that generates creative text")

prompt = st.text_area("Enter your prompt here", "Can you write me a poem about steamed hams?")

# Dropdowns
top_k_options = [10, 50, 100]
selected_top_k = st.selectbox('Select Top K', top_k_options)

top_p_options = [0.5, 0.9, 1]
selected_top_p = st.selectbox('Select Top P', top_p_options)

temperature_options = [0.5, 0.7, 1]
selected_temperature = st.selectbox('Select Temperature', temperature_options)

repetition_penalty_options = [1, 1.15, 1.5]
selected_repetition_penalty = st.selectbox('Select Repetition Penalty', repetition_penalty_options)

max_new_tokens_options = [100, 500, 1000]
selected_max_new_tokens = st.selectbox('Select Max New Tokens', max_new_tokens_options)

if st.button('Generate Text'):
    placeholder = st.empty()
    client = replicate.Client(api_token=st.secrets.replicate_api_token)
    output = client.run(
        "mistralai/mistral-7b-instruct-v0.1:5fe0a3d7ac2852264a25279d1dfb798acbc4d49711d126646594e212cb821749",
        input={
            "debug": False,
            "top_k": selected_top_k,
            "top_p": selected_top_p,
            "prompt": "The prompt is: " + prompt,
            "temperature": selected_temperature,
            "max_new_tokens": selected_max_new_tokens,
            "min_new_tokens": -1,
            "prompt_template": "{prompt}",
            "repetition_penalty": selected_repetition_penalty
        }
    )
    text = ''
    # Stream the output word by word
    for word in output:
        text += word
        placeholder.text(text)
