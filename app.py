import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Set page config must be the first Streamlit command
st.set_page_config(layout="wide", page_title="Sales Intelligence Dashboard")

@st.cache_data
def load_data():
    # Ensure the file is in the same directory as app.py
    return pd.read_csv("sales_performance_data.csv")

# Load the data
try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# --- DASHBOARD UI ---
st.title("📊 Sales Intelligence Dashboard")
st.sidebar.header("Hierarchy Drill-Down")

# Filters
region = st.sidebar.selectbox("Region", df['Region'].unique())
auh = st.sidebar.selectbox("Area Head", df[df['Region'] == region]['AUH_Name'].unique())
sm = st.sidebar.selectbox("Senior Manager", df[df['AUH_Name'] == auh]['Senior_Manager_Name'].unique())
mgr = st.sidebar.selectbox("Sales Manager", df[df['Senior_Manager_Name'] == sm]['Sales_Manager_Name'].unique())

filtered_df = df[df['Sales_Manager_Name'] == mgr]

st.write(f"Displaying data for Sales Manager: {mgr}")
st.dataframe(filtered_df.head())
