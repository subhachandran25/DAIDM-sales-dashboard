import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_data():
    # Get the directory where app.py is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "sales_performance_data.csv")
    
    if not os.path.exists(file_path):
        # List files in the directory to help you debug
        files_in_dir = os.listdir(current_dir)
        st.error(f"File not found: {file_path}. Found these files instead: {files_in_dir}")
        st.stop()
        
    return pd.read_csv(file_path)
