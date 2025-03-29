from PIL import Image, ImageEnhance
import streamlit as st
from io import BytesIO

# Title of the Streamlit app
st.title("Image Brightness and Contrast Adjustment")

# File uploader allows user to add their own image
uploaded_image = st.file_uploader("Choose a photo", type=["jpg", "jpeg", "png"])

if uploaded_image:
    # Open the uploaded image
    pil_image = Image.open(uploaded_image)

    # Display the original image
    st.image(pil_image, caption="Original Image", use_container_width=True)

    # Brightness adjustment
    brightness = st.slider("Adjust Brightness", 0.0, 2.0, 1.0)
    enhancer = ImageEnhance.Brightness(pil_image)
    brightened_image = enhancer.enhance(brightness)

    # Contrast adjustment
    contrast = st.slider("Adjust Contrast", 0.0, 2.0, 1.0)
    enhancer = ImageEnhance.Contrast(brightened_image)
    enhanced_image = enhancer.enhance(contrast)

    # Display the enhanced image
    st.image(enhanced_image, caption="Enhanced Image", use_container_width=True)

    # Convert the output image to bytes
    img_byte_arr = BytesIO()
    enhanced_image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # Provide a download button for the user to save the output image
    st.download_button(
        label="Download Enhanced Image",
        data=img_byte_arr,
        file_name="enhanced_image.png",
        mime="image/png"
    )
