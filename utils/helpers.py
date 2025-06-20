# utils/helpers.py
import streamlit as st
import time

# --- Helper Function to Change Page ---
def set_page(page_name):
    """Updates the session state to change the current page."""
    st.session_state.current_page = page_name

# --- Mock Data for Dashboard ---
def get_dashboard_stats():
    """Returns mock data for agricultural leaf disease statistics."""
    stats = {
        "totalCasesToday": 152,
        "casesByDiseaseType": [
            {"name": "Blight", "count": 48, "percentage": 31.6},
            {"name": "Mildew", "count": 35, "percentage": 23.0},
            {"name": "Rust", "count": 28, "percentage": 18.4},
            {"name": "Leaf Spot", "count": 22, "percentage": 14.5},
            {"name": "Healthy", "count": 19, "percentage": 12.5},
            {"name": "Other/Unidentified", "count": 0, "percentage": 0.0},
        ],
        "lastUpdated": st.session_state.get('last_updated_time', time.strftime("%I:%M %p")),
    }
    st.session_state.last_updated_time = stats["lastUpdated"]
    return stats

# --- Global CSS Styles ---
def apply_global_styles():
    """
    Applies custom CSS for general page aesthetics, background, fonts,
    and button/metric styling. Now uses a background image.
    """
    st.markdown("""
        <style>
        /* Import Google Font - Quicksand */
        @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap');

        /* Background Image for a fresh village feel */
        body {
            background-image: url("https://media.istockphoto.com/id/1786486973/photo/young-sprout-agricultural-technologies-banner.jpg?s=612x612&w=0&k=20&c=5RCxOczVxCdND-NLRx2LrlaYwnpexMY34by5C0ixL04=");
            background-size: cover; /* Cover the entire viewport */
            background-position: center center; /* Center the image */
            background-repeat: no-repeat; /* Do not repeat the image */
            background-attachment: fixed; /* Ensures image covers full height even with scroll */
            font-family: 'Quicksand', sans-serif; /* Apply Quicksand to the whole body */
            color: #1A1A1A; /* VERY DARK GRAY for primary text - almost black */
        }

        /* Adjust Streamlit specific containers for background */
        .stApp {
            background: none; /* Remove Streamlit's default background if any */
        }
        .main .block-container {
            padding-top: 2rem;
            padding-right: 2rem;
            padding-left: 2rem;
            padding-bottom: 2rem;
            color: #1A1A1A; /* Ensure text in main container is dark */
        }

        /* Card-like styling for content blocks (e.g., in Dashboard) */
        .stMarkdown, .stAlert, .stForm, .stExpander, .stFileUploader, .stTextInput, .stNumberInput {
            background-color: rgba(255, 255, 255, 0.95); /* Slightly more opaque white */
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            color: #1A1A1A; /* Ensure text within these blocks is dark */
        }

        /* Specific styling for the sidebar and its internal elements */
        [data-testid="stSidebar"] {
            background-color: #2E8B57 !important; /* Force sidebar background color */
            color: white !important; /* Default sidebar text color */
        }
        [data-testid="stSidebarContent"] {
            background-color: #2E8B57 !important; /* Ensure content area also matches */
            color: white !important;
        }

        /* Remove backgrounds from Streamlit components inside the sidebar */
        [data-testid="stSidebarContent"] .element-container,
        [data-testid="stSidebarContent"] .stImage,
        [data-testid="stSidebarContent"] .stMarkdown,
        [data-testid="stSidebarContent"] .stText {
            background-color: transparent !important; /* Make elements within sidebar transparent */
            box-shadow: none !important; /* Remove any shadows */
            border-radius: 0 !important; /* Remove any rounded corners */
        }

        /* Ensure all text within the sidebar is white */
        [data-testid="stSidebarContent"] h1,
        [data-testid="stSidebarContent"] h2,
        [data-testid="stSidebarContent"] h3,
        [data-testid="stSidebarContent"] h4,
        [data-testid="stSidebarContent"] h5,
        [data-testid="stSidebarContent"] h6,
        [data-testid="stSidebarContent"] p,
        [data-testid="stSidebarContent"] label { /* Important for button labels */
            color: white !important;
        }

        /* Styling for sidebar navigation buttons */
        [data-testid="stSidebar"] .stButton > button {
            background-color: transparent !important; /* Inactive: Transparent */
            color: #E0E0E0 !important; /* Inactive: Light grey text */
            border: 1px solid transparent !important; /* No border initially */
            box-shadow: none !important; /* No shadow initially */
            transition: all 0.2s ease-in-out;
            padding-left: 1rem; /* Add some padding for text alignment */
            text-align: left; /* Align text to the left */
        }

        [data-testid="stSidebar"] .stButton > button:hover {
            background-color: rgba(255, 255, 255, 0.1) !important; /* Hover: Subtle white overlay */
            color: white !important; /* Hover: Pure white text */
            border-color: rgba(255, 255, 255, 0.2) !important; /* Subtle white border on hover */
            transform: none !important; /* No lift effect for sidebar buttons */
            box-shadow: none !important; /* No shadow on hover for sidebar buttons */
        }

        /* Active button specific styling (targets the paragraph inside the button) */
        .stButton > button[data-testid*="sidebar"] { /* Generic target for all sidebar buttons */
            font-weight: 400; /* Default font weight */
        }

        .active-nav-button-text {
            color: white !important;
            font-weight: 700 !important; /* Bold active button text */
            background-color: #3C9F63; /* Slightly brighter green background for active button */
            border-radius: 0.5rem;
            padding: 0.75rem 1rem; /* Match button padding */
            display: block; /* Ensures padding/background applies to whole area */
            margin: -0.75rem -1rem; /* Adjust margin to counter padding */
        }


        /* Streamlit general button styles (for main content area) */
        .stButton>button {
            width: 100%;
            border-radius: 0.5rem;
            border: 1px solid #4CAF50; /* Primary green */
            background-color: #4CAF50;
            color: white; /* Button text remains white */
            padding: 0.75rem 1rem;
            font-size: 1rem;
            font-weight: 600;
            transition: all 0.2s ease-in-out;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #45a049; /* Slightly darker green on hover */
            border-color: #45a049;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2); /* More pronounced shadow on hover */
        }
        .stButton>button:active {
            transform: translateY(0);
            box-shadow: none;
        }

        /* Custom styling for metrics (from previous iterations) */
        .stMetric > div > div:nth-child(1) { /* Label */
            color: #2E8B57; /* Darker green for metric labels */
            font-weight: 600; /* Slightly bolder */
        }
        .stMetric > div > div:nth-child(2) { /* Value */
            color: #2E8B57; /* Darker green for metric values */
            font-weight: 700;
            font-size: 2.8rem; /* Slightly larger */
        }

        /* Progress bar (from previous iterations) */
        .stProgress > div > div {
            background-color: #A5D6A7; /* Light green background */
        }
        .stProgress > div > div > div {
            background-color: #2E8B57 !important; /* Darker green fill */
        }

        /* Expander customization */
        .streamlit-expanderHeader {
            background-color: #E8F5E9; /* Very light green for expander header */
            border-radius: 8px;
            padding: 10px 15px;
            font-weight: 600;
            color: #2E8B57; /* Dark green for expander header text */
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            transition: all 0.2s ease-in-out;
        }
        .streamlit-expanderHeader:hover {
            background-color: #DCEDC8; /* Slightly darker light green on hover */
        }
        .streamlit-expanderContent {
            background-color: white; /* White background for expanded content */
            border-bottom-left-radius: 8px;
            border-bottom-right-radius: 8px;
            padding: 15px;
            border-top: 1px solid #E0E0E0;
            box-shadow: 0 4px 8px rgba(0,0,0,0.08);
            color: #1A1A1A; /* Darker text for content inside expanders */
        }
        .stAlert {
            border-radius: 10px;
            color: #1A1A1A; /* Ensure alert text is dark */
        }
        .stAlert div[data-testid="stMarkdownContainer"] { /* Target markdown within alert */
            color: #1A1A1A !important; /* Force dark text for alert content */
        }

        /* Ensure all header types are dark and slightly bolder */
        h1, h2, h3, h4, h5, h6 {
            color: #1A1A1A !important; /* Force dark color for headings */
            font-weight: 700; /* Make headings bolder */
        }
        </style>
    """, unsafe_allow_html=True)

