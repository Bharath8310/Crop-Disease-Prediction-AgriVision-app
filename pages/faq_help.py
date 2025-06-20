# pages/faq_help.py
import streamlit as st
from utils.helpers import set_page # Ensure set_page is imported

def faq_help_page():
    st.title("Frequently Asked Questions & Help")
    st.markdown("""
        Welcome to the Help Center! Here you'll find answers to common questions about using AgriVision AI.
        If you can't find what you're looking for, please feel free to reach out to our support.
    """)

    # --- FAQ Section ---
    st.header("General Questions")

    # FAQ 1: How to upload a good leaf image?
    with st.expander("How can I upload a good leaf image for accurate detection?", expanded=True):
        st.markdown("""
            For the best results and most accurate disease detection, please follow these guidelines when capturing and uploading leaf images:
            * **Clear Focus:** Ensure the leaf is in sharp focus. Blurry images reduce accuracy.
            * **Good Lighting:** Use natural, even lighting. Avoid strong shadows or direct sunlight that can cause glare.
            * **Single Leaf:** Try to capture a single leaf that represents the symptoms you're observing. If possible, remove distracting backgrounds.
            * **Full Leaf View:** Capture the entire leaf, including the petiole (leaf stalk) if possible, and any affected areas.
            * **High Resolution:** Use a device that can capture reasonably high-resolution images (e.g., a modern smartphone camera).
            * **File Format:** We currently support JPG, JPEG, and PNG formats.
        """)

    # FAQ 2: What weather data is needed for yield prediction?
    with st.expander("What kind of weather data is required for crop yield prediction?"):
        st.markdown("""
            Our crop yield prediction model typically utilizes a combination of historical and forecasted weather data. Key parameters include:
            * **Temperature:** Average, minimum, and maximum daily temperatures (Celsius or Fahrenheit).
            * **Precipitation:** Daily or weekly rainfall amounts (mm or inches).
            * **Humidity:** Relative humidity (%).
            * **Sunshine Hours:** Daily total hours of sunlight.
            * **Wind Speed:** Average daily wind speed (km/h or mph).
            * **Location:** Geographical coordinates (latitude and longitude) are crucial to pull localized weather data.
            * *Note: Specific requirements might vary as we integrate more advanced models.*
        """)

    # FAQ 3: Limitations of the model
    with st.expander("What are the limitations of the disease detection model?"):
        st.markdown("""
            While AgriVision AI is designed for high accuracy, it's important to understand its current limitations:
            * **Image Quality:** Poor quality, blurry, or improperly lit images can significantly reduce detection accuracy.
            * **Disease Severity:** Very early stages of disease, or extremely advanced/decayed stages, might be harder to diagnose accurately.
            * **New/Rare Diseases:** The model is trained on a specific dataset. It may not recognize diseases not present in its training data.
            * **Non-Disease Stress:** Symptoms caused by nutrient deficiencies, pest infestations (non-fungal/bacterial), or environmental stress (e.g., drought, heat) might be misidentified or flagged as "unidentified."
            * **Single Crop Focus:** While we classify crop types, the disease detection is specific to known diseases for that crop.
            * **Not a Substitute for Expert Advice:** This tool is a helpful assistant but should not replace professional agricultural advice or on-site inspections for critical decisions.
        """)


    # --- Support / Contact Information ---
    st.header("Need More Help?")
    st.info("""
        If you couldn't find an answer to your question, or if you're experiencing technical issues,
        please don't hesitate to contact our support team at **support@agrivisionai.com**.
        We aim to respond within 24-48 hours.
    """)

    # Option to navigate back to Dashboard
    if st.button("Back to Dashboard", key="back_from_faq_help"):
        set_page("dashboard")