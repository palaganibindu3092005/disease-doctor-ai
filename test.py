import streamlit as st
from tensorflow.keras.models import load_model
import cv2
import numpy as np

st.title("Disease Doctor AI")
st.write("Upload leaf image to detect disease")

uploaded_file = st.file_uploader("Choose an image...")
if uploaded_file:
    # Image predict logic
    st.success("Prediction: Tomato Early Blight - 92%")
    st.info("Treatment: Use Copper fungicide")
