import streamlit as st
import replicate

st.title("Object Generator")
st.subheader("an AI model that generates 3D objects")

prompt = st.text_area("Enter your prompt here","orange cat pirate")


if st.button('Generate Video'):
    client = replicate.Client(api_token=st.secrets.replicate_api_token)
    output = replicate.run(
        "adirik/mvdream:38af22609c9a779c2203c2009ff7451f115b44cde8d9a65ad132980714b82f34",
        input={
            "prompt": prompt,
            "max_steps": 10000,
            "guidance_scale": 50,
            "negative_prompt": "ugly, bad anatomy, blurry, pixelated obscure, unnatural colors, poor lighting, dull, and unclear, cropped, lowres, low quality, artifacts, duplicate, morbid, mutilated, poorly drawn face, deformed, dehydrated, bad proportions"
        }
    )
    st.write(output)