import streamlit as st
import replicate

st.title("Realistic Image Generator")
st.subheader("an AI model that generates realistic images")

# Dropdowns for style and subject type selection
selected_style = st.selectbox('Select Style', ["Realistic", "From the 80s", "Futuristic"])
selected_subject_type = st.selectbox('Select Subject Type', ["Person", "Animal" ,"Vehicle","Other"])

subject = st.text_input("Enter the subject here", "latino man")

type = ""
if selected_style == "Realistic":
    type = ", realistic, cinematic"
elif selected_style == "From the 80s":
    type = ", 80s art style"
elif selected_style == "Futuristic":
    type = ", futuristic style"

# Construct the prompt based on the style, subject, and subject type
additional_info = ""
if selected_subject_type == "Person":
    additional_info = ", perfect eyes, natural skin, looks at viewer"
elif selected_subject_type == "Animal":
    additional_info = ", majestic mane, in its natural habitat"
elif selected_subject_type == "Vehicle":
    additional_info = ", sleek design, vibrant color, beautiful reflections"
elif selected_subject_type == "Other":
    additional_info = ""

prompt = f"{subject}{type}{additional_info}"

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