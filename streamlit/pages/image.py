import streamlit as st
import replicate

st.title("Realistic Image Generator")
st.subheader("an AI model that generates realistic images")

# Dropdown for style selection
style_options = ["realistic", "80s", "futuristic"]
selected_style = st.selectbox('Select Style', style_options)

# Text input for the subject
subject = st.text_input("Enter the subject here", "latino man")

# dark shot, front shot, closeup photo of a 25 y.o latino man, perfect eyes, natural skin, skin moles, looks at viewer, cinematic shot
# Construct the prompt based on the style and subject
if selected_style == "realistic":
    prompt = f"{subject}, realistic, cinematic shot"
elif selected_style == "80s":
    prompt = f"{subject}, 80s art style"
elif selected_style == "futuristic":
    prompt = f"{subject}, futuristic style"

# Dropdowns
scheduler_options = ["DPMSolverMultistep"]
selected_scheduler = st.selectbox('Select Scheduler', scheduler_options)

num_outputs_options = [1, 2, 3]
selected_num_outputs = st.selectbox('Select Number of Outputs', num_outputs_options)

if st.button('Generate Image'):
    client = replicate.Client(api_token=st.secrets.replicate_api_token)
    output = client.run(
        "lucataco/realvisxl-v2.0:7d6a2f9c4754477b12c14ed2a58f89bb85128edcdd581d24ce58b6926029de08",
        input={
            "width": 1024,
            "height": 1024,
            "prompt": prompt,
            "scheduler": selected_scheduler,
            "lora_scale": 0.6,
            "num_outputs": selected_num_outputs,
            "guidance_scale": 7,
            "apply_watermark": True,
            "negative_prompt": "(worst quality, low quality, illustration, 3d, 2d, painting, cartoons, sketch), open mouth",
            "prompt_strength": 0.8,
            "num_inference_steps": 40
        }
    )
    st.image(output)