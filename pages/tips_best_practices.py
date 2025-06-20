# pages/tips_best_practices.py
import streamlit as st
from utils.helpers import set_page

def set_custom_style():
    st.markdown("""
        <style>
            .tip-card {
                background-color: #f4f9f4;
                border-left: 6px solid #34a853;
                padding: 16px;
                border-radius: 10px;
                margin-bottom: 15px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            }
            .video-card {
                margin-top: 10px;
                margin-bottom: 30px;
            }
        </style>
    """, unsafe_allow_html=True)

def tips_best_practices_page():
    set_custom_style()

    st.title("🌾 Tips & Best Practices")
    st.markdown("Discover **seasonal farming tips**, **crop care guides**, and **pest control strategies** to improve yield and sustainability.")

    # --- Farming Tips Section ---
    st.subheader("🌱 Seasonal Farming Tips")
    with st.container():
        st.markdown("""
        <div class="tip-card">
            ✅ **Rabi Season:** Start sowing wheat, barley, and mustard between October and December. Ensure good soil moisture after monsoons.<br><br>
            ✅ **Kharif Season:** Begin sowing rice, millets, and cotton from June to July. Use rainwater harvesting techniques.<br><br>
            ✅ **Zaid Crops:** For summer crops like watermelon and cucumber, use drip irrigation to manage water efficiently.
        </div>
        """, unsafe_allow_html=True)

    # --- Crop Care Tips ---
    st.subheader("🌿 Crop Care & Soil Health")
    with st.container():
        st.markdown("""
        <div class="tip-card">
            🧪 **Soil Testing:** Test soil pH and nutrients before each season.<br><br>
            🌾 **Crop Rotation:** Rotate between legumes and cereals to naturally restore nitrogen in soil.<br><br>
            💧 **Smart Irrigation:** Use drip or sprinkler systems to reduce water waste and prevent fungal diseases.
        </div>
        """, unsafe_allow_html=True)

    # --- Pest & Disease Management ---
    st.subheader("🐛 Pest & Disease Control")
    with st.container():
        st.markdown("""
        <div class="tip-card">
            🌼 **Use Neem Oil:** A natural pesticide effective against common insects like aphids and whiteflies.<br><br>
            🧼 **Intercropping:** Grow pest-repellent plants like marigold along with main crops.<br><br>
            🚫 **Avoid Overwatering:** Many fungal diseases thrive in excess moisture. Water early in the morning.
        </div>
        """, unsafe_allow_html=True)


    # --- Educational Videos ---
    st.subheader("📺 Recommended Videos")

    with st.container():
        st.markdown('<div class="video-card">', unsafe_allow_html=True)
        st.video("https://youtu.be/pP6eB2sPbng?si=rZgFOSmBrVCDs58x")  # Sustainable farming
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="video-card">', unsafe_allow_html=True)
        st.video("https://youtu.be/W3P9deLFkk8?si=9hnInyk3Rp4IKpsJ")  # Natural Pest Control
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="video-card">', unsafe_allow_html=True)
        st.video("https://youtu.be/NCyNPwD_MNQ?si=aHU9Bnir1OOVculC")  # Soil health and composting
        st.markdown("</div>", unsafe_allow_html=True)


    # Back button
    if st.button("🔙 Back to Dashboard", key="back_from_tips"):
        set_page("dashboard")
