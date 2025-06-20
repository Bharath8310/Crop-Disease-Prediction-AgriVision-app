# pages/dashboard.py
import streamlit as st
import time
from utils.helpers import get_dashboard_stats, apply_global_styles  # Custom helpers

# Inject some CSS
def set_custom_style():
    st.markdown("""
        <style>
            .section-box {
                background-color: #f5fdf7;
                border-radius: 15px;
                padding: 20px;
                margin-bottom: 20px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.06);
            }
            .rainfall-status {
                font-size: 20px;
                padding: 12px;
                border-radius: 10px;
                background-color: #e0f3ff;
                border-left: 5px solid #0077b6;
                margin-bottom: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

def dashboard_page():
    set_custom_style()
    
    st.title("🌿 AgriVision AI Dashboard")

    st.markdown("""
        ### Welcome to **AgriVision AI**, your intelligent Agricultural Assistant!  
        Get a quick overview of today's **leaf disease detections**, and dive into smart features to support your farming needs.
    """)

    st.info("""
        **Instructions:** Use the menu on the left to:
        - 📸 Scan a leaf image
        - 📈 Predict crop yields
        - 📚 Browse disease info
        - 🎓 Learn tips & best practices
    """)

    st.subheader("🌾 Agriculture in India Overview")

    with st.container():
        st.markdown("""
        <div class="section-box">
            🧑‍🌾 India is one of the world's largest agrarian economies, with over 60% of its rural population relying on agriculture.  
            The major crops include **rice, wheat, cotton, sugarcane, and pulses**.  
            Technological advancements like AI, soil sensors, and precision irrigation are transforming Indian agriculture.

            👉 This platform helps bring those technologies closer to farmers and agricultural researchers.
        </div>
        """, unsafe_allow_html=True)

    # Rainfall Status
    st.subheader("🌧️ Rainfall Status (Mock Data)")
    st.markdown("""
    <div class="rainfall-status">
        🚨 <strong>Rainfall Alert:</strong> Moderate rainfall expected in Maharashtra and Kerala over the next 48 hours.  
        💡 Plan irrigation accordingly and delay pesticide spraying during rains.
    </div>
    """, unsafe_allow_html=True)

    # Disease stats
    st.subheader("🦠 Present-Day Leaf Disease Detection Stats")

    stats = get_dashboard_stats()

    st.markdown(f"<p class='text-sm text-gray-600'>📅 Data updated on: {time.strftime('%B %d, %Y')} | ⏱ Last Sync: {stats['lastUpdated']}</p>", unsafe_allow_html=True)
    st.write("")

    st.subheader("📊 Today's Overview")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Cases Detected", value=stats["totalCasesToday"])
    with col2:
        st.metric(label="Most Common Disease", value="Blight")
    with col3:
        st.metric(label="Healthy Leaves Detected", value=f"{stats['casesByDiseaseType'][-2]['count']}")
    st.subheader("📌 Disease Breakdown")

    for disease in stats["casesByDiseaseType"]:
        st.markdown(f"**{disease['name']}:** {disease['count']} cases ({disease['percentage']:.1f}%)")
        st.progress(disease['percentage'] / 100)

    # Optional: If you want global styling to be applied once
    # apply_global_styles()
