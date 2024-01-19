import streamlit as st
import replicate

st.title("Realistic Video Generator")
st.subheader("an AI model that generates realistic videos")

prompt = st.text_area("Enter your prompt here","A video of Taylor Swift smiling")

# Dropdowns
scheduler_options = ["EulerAncestralDiscreteScheduler"]
selected_scheduler = st.selectbox('Select Scheduler', scheduler_options)

steps_options = [10, 20, 30]
selected_steps = st.selectbox('Select Number of Steps', steps_options)

if st.button('Generate Video'):
    client = replicate.Client(api_token=st.secrets.replicate_api_token)
    output = client.run(
        "charlesmccarthy/hotshot-a40:12e43c65e07546ebe88cc1f15c44417fd95f9236d0fdc9b5559cbaa1b134c112",
        input={
            "steps": selected_steps,
            "width": 384,
            "height": 672,
            "prompt": prompt,
            "scheduler": selected_scheduler,
            "negative_prompt": "blurry"
        }
    )
    st.image(output)