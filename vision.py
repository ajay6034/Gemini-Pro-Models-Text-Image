from dotenv import load_dotenv
load_dotenv() # loading all the env variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get response 

model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text


## initialize streamlit App

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")

input = st.text_input("Input Prompt: ", key="input")


# Title of the app
st.title("Image Upload Example")

# Create file uploader for image
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
image=""
# Display the uploaded image
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

submit=st.button("Tell me about the image")

## if submit is clicked
if submit:
    response= get_gemini_response(input, image)
    st.subheader("The Response is")
    st.write(response)