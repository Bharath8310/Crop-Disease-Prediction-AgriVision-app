import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import json # To load class names

# --- Configuration (Moved here, specific to this page) ---
IMG_HEIGHT = 224
IMG_WIDTH = 224

# Paths to your saved model and class names (Adjust paths if 'best_model_leaf.h5' and 'disease_info.json'
# are NOT in the root directory relative to where app.py is run.
# A common pattern is to put models/data in a 'data' folder at the root.
# For now, assuming they are in the same directory as app.py or accessible from it.)
MODEL_PATH = 'best_model_leaf.h5'
CLASS_NAMES_PATH = 'disease_info.json'

# --- Load Model (Cached for performance) ---
@st.cache_resource
def get_model():
    # It's generally good practice to explicitly state where the model file should be.
    # If your model is in the root and pages/scan_upload.py is run by app.py in root,
    # then 'best_model_leaf.h5' is fine. If not, adjust path like '../best_model_leaf.h5'
    # if it's one level up from 'pages' folder.
    try:
        model = load_model(MODEL_PATH)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}. Please ensure '{MODEL_PATH}' exists.")
        st.stop() # Stop execution if model can't be loaded

model = get_model()

# --- Load Class Names and Cures Data (Cached) ---
@st.cache_data
def load_disease_data():
    try:
        with open(CLASS_NAMES_PATH, 'r') as f:
            data = json.load(f)
        
        class_names_list = list(data.keys())
        cures_lookup = {name: info["cure"] for name, info in data.items()}
        return class_names_list, cures_lookup
    except FileNotFoundError:
        st.error(f"Error: Disease information file '{CLASS_NAMES_PATH}' not found. Please ensure it's in the correct directory.")
        st.stop()
    except json.JSONDecodeError:
        st.error(f"Error: Could not decode JSON from '{CLASS_NAMES_PATH}'. Check file format.")
        st.stop()
    except Exception as e:
        st.error(f"An unexpected error occurred while loading disease data: {e}")
        st.stop()

class_names, cures_data = load_disease_data()
num_classes = len(class_names)


# --- Prediction Function ---
def predict_disease(image):
    img = image.resize((IMG_HEIGHT, IMG_WIDTH))
    img_array = np.array(img)
    img_array = img_array / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0) # Add batch dimension

    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions[0])
    confidence = np.max(predictions[0]) * 100

    if predicted_class_index >= num_classes:
        st.error(f"Prediction out of bounds: Model predicted class index {predicted_class_index}, but only {num_classes} classes are defined.")
        st.warning("This might indicate a mismatch between the trained model and the loaded class names.")
        return "Unknown Disease", 0.0
    
    predicted_class_name = class_names[predicted_class_index]
    return predicted_class_name, confidence

# --- Main function for the Scan/Upload page ---
def scan_upload_page():
    st.markdown("<h2 style='text-align: center; color: #2E8B57;'>⬆️ Scan / Upload Leaf Image</h2>", unsafe_allow_html=True)
    st.write("Upload an image of a plant leaf to get a diagnosis and suggested cure.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("")
        st.write("Classifying...")

        with st.spinner('Predicting...'):
            predicted_class_name, confidence = predict_disease(image)

        if predicted_class_name != "Unknown Disease":
            parts = predicted_class_name.split('___')
            
            leaf_type_raw = parts[0]
            disease_name_raw = ""
            if len(parts) > 1:
                disease_name_raw = parts[1]

            leaf_type_display = leaf_type_raw.replace('_', ' ').replace('( ', '(').replace(' )', ')').strip()
            
            disease_status_display = ""
            if "healthy" in disease_name_raw.lower():
                disease_status_display = "Healthy"
            else:
                disease_status_display = f"Diseased ({disease_name_raw.replace('_', ' ').strip()})"

            st.subheader("Prediction Result:")
            st.write(f"**Plant:** {leaf_type_display}")
            st.write(f"**Disease Status:** {disease_status_display}")
            st.write(f"**Confidence:** {confidence:.2f}%")

            if predicted_class_name in cures_data:
                st.subheader("Suggested Cure/Management:")
                st.info(cures_data[predicted_class_name])
            else:
                st.warning("Cure information not available for this specific class. Please consult an agricultural expert.")
        
        st.markdown("---")
        st.markdown("If you wish to scan another image, simply upload a new one above.")

# Example usage if you were to run this file directly for testing (not needed when integrated)
if __name__ == '__main__':
    # This block won't run when imported by app.py
    st.set_page_config(layout="centered") # Minimal config for direct test
    scan_upload_page()