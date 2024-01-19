import streamlit as st
import replicate

st.title("Realistic Audio Generator")
st.subheader("an AI model that generates realistic audio")

prompt = st.text_area("Enter your prompt here","Edo25 minor g melodies that sound dissonant and cinematic. Leading up to a crescendo that resolves in a 9th harmonic")

# Dropdowns
top_k_options = [100, 250, 500]
selected_top_k = st.selectbox('Select Top K', top_k_options)

top_p_options = [0, 0.5, 1]
selected_top_p = st.selectbox('Select Top P', top_p_options)

duration_options = [10, 20, 30]
selected_duration = st.selectbox('Select Duration', duration_options)

temperature_options = [0.5, 1, 1.5]
selected_temperature = st.selectbox('Select Temperature', temperature_options)

if st.button('Generate Audio'):
    client = replicate.Client(api_token=st.secrets.replicate_api_token)
    output = client.run(
        "meta/musicgen:b05b1dff1d8c6dc63d14b0cdb42135378dcb87f6373b0d3d341ede46e59e2b38",
        input={
            "top_k": selected_top_k,
            "top_p": selected_top_p,
            "prompt": prompt,
            "duration": selected_duration,
            "temperature": selected_temperature,
            "continuation": False,
            "model_version": "stereo-large",
            "output_format": "wav",
            "continuation_start": 0,
            "multi_band_diffusion": False,
            "normalization_strategy": "peak",
            "classifier_free_guidance": 3
        }
    )
    st.audio(output)  # Use st.audio() for audio files
