import streamlit as st
import replicate

st.title("Wazzap")


output = replicate.run(
    "lucataco/realvisxl-v2.0:7d6a2f9c4754477b12c14ed2a58f89bb85128edcdd581d24ce58b6926029de08",
    input={
        "width": 1024,
        "height": 1024,
        "prompt": "dark shot, front shot, closeup photo of a 25 y.o latino man, perfect eyes, natural skin, skin moles, looks at viewer, cinematic shot",
        "scheduler": "DPMSolverMultistep",
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