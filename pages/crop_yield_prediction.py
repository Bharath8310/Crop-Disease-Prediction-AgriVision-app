# pages/crop_yield_prediction.py
import streamlit as st
from utils.helpers import set_page

def crop_yield_prediction_page():
    st.title("Crop Yield Prediction")
    st.markdown("Predict the yield of your crops based on various environmental factors.")
    st.warning("This page is under construction.")
    st.write("---")
    if st.button("Back to Dashboard", key="back_from_yield"):
        set_page("dashboard")
