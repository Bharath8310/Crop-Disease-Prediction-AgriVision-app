# app.py
import streamlit as st

# Import page functions
from pages.dashboard import dashboard_page
from pages.scan_upload import scan_upload_page
from pages.crop_yield_prediction import crop_yield_prediction_page
from pages.disease_library import disease_library_page
from pages.tips_best_practices import tips_best_practices_page
from pages.faq_help import faq_help_page

# Import helpers
from utils.helpers import set_page, apply_global_styles

# --- Page Configuration ---
st.set_page_config(
    page_title="AgriVision - Leaf Disease Detector",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Apply global styles once at the beginning
apply_global_styles()

# --- Global Session State Initialization ---
if 'current_page' not in st.session_state:
    st.session_state.current_page = "dashboard" # Default page is Dashboard

# --- Sidebar Navigation ---
with st.sidebar:
    st.image("https://placehold.co/100x100/A5D6A7/2E8B57?text=🌿", use_column_width=False) # Placeholder for logo
    st.markdown("<h1 style='text-align: center; color: white; margin-top: 1rem; margin-bottom: 2rem;'>AgriVision AI</h1>", unsafe_allow_html=True)

    # Define navigation buttons and their corresponding pages
    nav_items = [
        {"label": "📊 Dashboard (Home)", "page": "dashboard"},
        {"label": "⬆️ Scan / Upload Leaf Image", "page": "scan_upload"},
        {"label": "📈 Crop Yield Prediction", "page": "crop_yield_prediction"},
        {"label": "📚 Disease Library / Info", "page": "disease_library"},
        {"label": "💡 Tips & Best Practices", "page": "tips_best_practices"},
        {"label": "❓ FAQ / Help", "page": "faq_help"},
    ]

    for item in nav_items:
        is_active = st.session_state.current_page == item["page"]
        
        # Use an empty container to apply background to the active button
        # This is a common Streamlit hack for more custom button styling
        if is_active:
            button_html = f"""
            <div style="
                background-color: #3C9F63; /* Active background */
                border-radius: 0.5rem;
                padding: 0.75rem 1rem;
                margin-bottom: 0.5rem; /* Spacing between buttons */
                color: white;
                font-weight: 700;
                cursor: pointer;
                transition: all 0.2s ease-in-out;
            ">
                {item["label"]}
            </div>
            """
            st.markdown(button_html, unsafe_allow_html=True)
        else:
            # For inactive buttons, use the standard st.button
            # The global CSS in helpers.py will style these as transparent with light text
            if st.button(item["label"], key=f"nav_{item['page']}_sidebar", use_container_width=True):
                set_page(item["page"])

    st.markdown(
        """
        <div style="text-align: center; font-size: 0.8rem; color: #d0d0d0; margin-top: 1rem;">
            © 2024 AgriVision <br>All rights reserved.
        </div>
        """,
        unsafe_allow_html=True
    )


# --- Main Page Rendering Logic ---
if st.session_state.current_page == "dashboard":
    dashboard_page()
elif st.session_state.current_page == "scan_upload":
    scan_upload_page()
elif st.session_state.current_page == "crop_yield_prediction":
    crop_yield_prediction_page()
elif st.session_state.current_page == "disease_library":
    disease_library_page()
elif st.session_state.current_page == "tips_best_practices":
    tips_best_practices_page()
elif st.session_state.current_page == "faq_help":
    faq_help_page()
