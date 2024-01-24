import streamlit as st
from PIL import Image

# Load images
image1 = Image.open('./media/image8.png')
image2 = Image.open('./media/image9.png')
image3 = Image.open('./media/image1.png')
image4 = Image.open('./media/image2.png')
image5 = Image.open('./media/image3.png')
image6 = Image.open('./media/image4.png')
image7 = Image.open('./media/image5.png')
image8 = Image.open('./media/image6.png')
image9 = Image.open('./media/image7.png')
image10 = Image.open('./media/image8.png')
image11 = Image.open('./media/image9.png')


# Create a new page for the gallery
def gallery():
    st.title("Image Gallery")

    # Create a grid with 3 images per row
    col1, col2, col3 = st.beta_columns(3)

    with col1:
        st.image(image1, use_column_width=True)
    with col2:
        st.image(image2, use_column_width=True)
    with col3:
        st.image(image3, use_column_width=True)

    col4, col5, col6 = st.beta_columns(3)

    with col4:
        st.image(image4, use_column_width=True)
    with col5:
        st.image(image5, use_column_width=True)
    with col6:
        st.image(image6, use_column_width=True)

# Call the function to display the gallery
gallery()