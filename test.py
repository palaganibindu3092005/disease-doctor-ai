import streamlit as st
from tensorflow.keras.models import load_model
import cv2
import numpy as np
from PIL import Image
import details

st.title("🌿 Disease Doctor AI")
st.write("Upload leaf image to detect disease")

# Load trained model - nee .h5 file path ivvali
# model = load_model('plant_disease_model.h5')

# Class names - nee model train chesina classes
class_names = ['Tomato_Early_Blight', 'Tomato_Healthy', 'Potato_Late_Blight']

uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Leaf", use_column_width=True)
    
    if st.button("Predict Disease"):
        with st.spinner('Analyzing...'):
            # 1. Image preprocess
            img = np.array(image)
            img = cv2.resize(img, (224, 224)) # model input size batti marchu
            img = np.expand_dims(img, axis=0)
            
            # 2. Prediction - ippudu dummy prediction
            # pred = model.predict(img)
            # predicted_class = class_names[np.argmax(pred)]
            # confidence = np.max(pred) * 100
            
            # Demo kosam dummy output
            predicted_class = 'Tomato__Early_Blight'
            confidence = 93.7%
            
            st.success(f"Prediction: {predicted_class.replace('_', ')} - {confidence:.2f}%")
            
            # 3. details.py nunchi info teesukovadam
            if predicted_class in details.disease_info:
                info = details.disease_info[predicted_class]
                st.info(f"**Treatment:** {info['treatment']}")
                st.warning(f"**Precaution:** {info['precaution']}")
