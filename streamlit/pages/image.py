import streamlit as st
import replicate

st.title("Realistic Image Generator")
st.subheader("an AI model that generates realistic images")

selected_style = st.radio('Select Style', ["Realistic", "From the 80s", "Futuristic"])
selected_subject_type = st.radio('Select Subject Type', ["Person", "Animal" ,"Vehicle","Other"])

# Text input for the subject
subject = st.text_input("Enter the subject here", "latino man")

# Dictionary for style details
style_details = {
    "Realistic": ", realistic, cinematic",
    "From the 80s": ", 80s art style",
    "Futuristic": ", futuristic style"
}

# Dictionary for subject type details
subject_type_details = {
    "Person": ", person, perfect eyes, natural skin, looks at viewer",
    "Animal": ", animal, majestic mane, in its natural habitat",
    "Vehicle": ", vehicle, sleek design, vibrant color, beautiful reflections",
    "Other": ""
}

# Construct the prompt based on the style, subject, and subject type
prompt = f"{subject}{style_details[selected_style]}{subject_type_details[selected_subject_type]}"

if st.button('Generate Image'):
    client = replicate.Client(api_token=st.secrets.replicate_api_token)
    output = client.run(
        "lucataco/realvisxl-v2.0:7d6a2f9c4754477b12c14ed2a58f89bb85128edcdd581d24ce58b6926029de08",
        input={
            "width": 1024,
            "height": 1024,
            "prompt": prompt,
            "scheduler": 'DPMSolverMultistep',
            "lora_scale": 0.6,
            "num_outputs": 1,
            "guidance_scale": 7,
            "apply_watermark": True,
            "negative_prompt": "(worst quality, low quality, illustration, 3d, 2d, painting, cartoons, sketch), open mouth",
            "prompt_strength": 0.8,
            "num_inference_steps": 40
        }
    )
    st.image(output)
