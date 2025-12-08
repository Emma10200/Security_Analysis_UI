import streamlit as st
import polars as pl
from pathlib import Path

# 1. Initialize the app configuration (Wide mode)
st.set_page_config(
    page_title="Security Analysis UI",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Apply a strict "Black/Green" terminal style (CSS)
st.markdown(
    """
    <style>
    /* Global background and font */
    .stApp {
        background-color: #000000;
        color: #00FF00;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #00FF00 !important;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Metrics */
    div[data-testid="stMetricValue"] {
        color: #00FF00 !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #008800 !important;
    }
    
    /* Remove default padding/margins for density */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Scan data/*.parquet
data_dir = Path("data")
parquet_files = list(data_dir.glob("*.parquet"))
ticker_count = len(parquet_files)

# 4. Display a simple metric
st.title("SECURITY ANALYSIS TERMINAL")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.metric(label="SYSTEM STATUS", value="ONLINE")

with col2:
    st.metric(label="TICKERS CONNECTED", value=str(ticker_count))

# 5. Stop. Do nothing else.
