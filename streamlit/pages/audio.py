import streamlit as st
import replicate

st.title("Realistic Audio Generator")
st.subheader("an AI model that generates realistic audio")

# Radio button for model selection
selected_model = st.sidebar.radio('Select Model', ["melody-large", "riffusion"])

# Text input for the prompt
prompt = st.text_input("Enter the prompt here", "rock and roll song in the style of ACDC")

if st.button('Generate Audio'):
    client = replicate.Client(api_token=st.secrets.replicate_api_token)
    
    if selected_model == "melody-large":
        output = client.run(
            "meta/musicgen:b05b1dff1d8c6dc63d14b0cdb42135378dcb87f6373b0d3d341ede46e59e2b38",
            input={
                "top_k": 250,
                "top_p": 0,
                "prompt": "Rock and Roll song in the style of ACDC",
                "duration": 25,
                "temperature": 1,
                "continuation": False,
                "model_version": "melody-large",
                "output_format": "wav",
                "continuation_start": 0,
                "multi_band_diffusion": False,
                "normalization_strategy": "peak",
                "classifier_free_guidance": 3
            }
        )
        st.audio(output)
    elif selected_model == "riffusion":
        output = client.run(
            "riffusion/riffusion:8cf61ea6c56afd61d8f5b9ffd14d7c216c0a93844ce2d82ac1c9ecc9c7f24e05",
            input={
                "alpha": 0.5,
                "prompt_a": "funky synth solo",
                "prompt_b": "90's rap",
                "denoising": 0.75,
                "seed_image_id": "vibes",
                "num_inference_steps": 50
            }
        ) 
        st.audio(output['audio'])
        st.image(output['spectrogram'])