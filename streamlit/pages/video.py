import streamlit as st
import replicate

st.title("Realistic Video Generator")
st.subheader("an AI model that generates realistic videos")

prompt = st.text_area("Enter your prompt here","A muscular man lifting heavy dumbbels in the gym, HD, 8k, realistic")


if st.button('Generate Video'):
    client = replicate.Client(api_token=st.secrets.replicate_api_token)
    output = client.run(
        "lucataco/hotshot-xl:78b3a6257e16e4b241245d65c8b2b81ea2e1ff7ed4c55306b511509ddbfd327a",
        input={
            "mp4": False,
            "seed": 6226,
            "steps": 35,
            "width": 672,
            "height": 384,
            "prompt": prompt,
            "scheduler": "EulerAncestralDiscreteScheduler",
            "negative_prompt": "blurry"
        }
    )
    st.image(output)