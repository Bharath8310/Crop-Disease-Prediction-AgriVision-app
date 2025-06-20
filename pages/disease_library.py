# pages/disease_library.py
import streamlit as st
from utils.helpers import set_page

# Add CSS for better visuals
def set_custom_style():
    st.markdown("""
        <style>
        .disease-card {
            background-color: #f9f9f9;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        .disease-image {
            border-radius: 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.15);
        }
        </style>
    """, unsafe_allow_html=True)

# Disease data using image URLs
diseases = {
    "🍅 Tomato - Late Blight": {
        "image": "https://content.ces.ncsu.edu/media/images/IMG_5813.jpg",
        "description": "A serious disease caused by *Phytophthora infestans*, leading to large, dark, greasy spots on leaves and stems.",
        "treatment": "Use fungicides like copper hydroxide or mancozeb. Remove and destroy infected plants. Avoid overhead watering."
    },
    "🍅 Tomato - Early Blight": {
        "image": "https://extension.umd.edu/sites/extension.umd.edu/files/styles/optimized/public/2021-05/hgic_veg_early%20blight%20lesions%20on%20tomato_1573858_1200.jpg?itok=-1EwR8BC",
        "description": "Caused by *Alternaria solani*, symptoms include concentric rings on lower leaves and eventual defoliation.",
        "treatment": "Apply fungicides like chlorothalonil. Remove infected leaves and rotate crops regularly."
    },
    "🥔 Potato - Late Blight": {
        "image": "https://spudsmart.com/wp-content/uploads/2017/05/potato_late-blight_08_zoom-Photo-OMAFRA-900x580.jpeg",
        "description": "*Phytophthora infestans* affects potato leaves and tubers, causing rot and yield loss.",
        "treatment": "Apply systemic fungicides and practice good field hygiene."
    },
    "🍇 Grape - Black Rot": {
        "image": "https://kentuckypestnews.wordpress.com/wp-content/uploads/2016/07/black-rot-of-grape_figure-1.jpg",
        "description": "Caused by *Guignardia bidwellii*, it creates brown spots with black margins on leaves and fruits.",
        "treatment": "Prune infected parts and use fungicides like myclobutanil."
    },
    "🌽 Corn - Leaf Blight": {
        "image": "https://extension.umn.edu/sites/extension.umn.edu/files/northernleafblight2_600px.jpg",
        "description": "*Exserohilum turcicum* causes elongated gray-green lesions on corn leaves, leading to tissue death.",
        "treatment": "Use resistant hybrids, rotate crops, and apply fungicides when necessary."
    }
}

def disease_library_page():
    set_custom_style()

    st.title("🌿 Disease Library & Info")
    st.markdown("Explore **common plant diseases**, their **symptoms**, and **recommended remedies** below:")

    # Display each disease as a card
    for name, info in diseases.items():
        with st.container():
            st.markdown('<div class="disease-card">', unsafe_allow_html=True)
            cols = st.columns([1.2, 2])
            with cols[0]:
                st.image(info["image"], use_column_width=True, caption=None, output_format="auto")
            with cols[1]:
                st.subheader(name)
                st.markdown(f"**🦠 Description:** {info['description']}", unsafe_allow_html=True)
                st.markdown(f"**💊 Treatment:** {info['treatment']}", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # Back button
    if st.button("🔙 Back to Dashboard", key="back_from_library"):
        set_page("dashboard")
