import streamlit as st
import replicate

st.title("Object Generator")
st.subheader("an AI model that generates 3D objects")

prompt = st.text_area("Enter your prompt here","orange cat pirate")


if st.button('Generate Video'):
    client = replicate.Client(api_token=st.secrets.replicate_api_token)
    output = replicate.run(
        "cjwbw/shap-e:5957069d5c509126a73c7cb68abcddbb985aeefa4d318e7c63ec1352ce6da68c",
        input={
            "prompt": "orange cat",
            "save_mesh": False,
            "batch_size": 1,
            "render_mode": "nerf",
            "render_size": 128,
            "guidance_scale": 15
        }
    )
    st.image(output)


st.header('Output for "orange cat"')
st.image('./media/orangecat.gif', width=960)