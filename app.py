# app.py
import streamlit as st
import pandas as pd
import os

# -----------------------------
# Get current directory of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct path to CSV file
csv_path = os.path.join(BASE_DIR, "lead.csv")

# Load CSV
try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    st.error(f"CSV file not found at {csv_path}")
    st.stop()

# -----------------------------
# Streamlit app
st.title("Lead Probability Engine")

st.write("Here is your data:")
st.dataframe(df)

# Example: Show summary
st.write("Summary statistics:")
st.write(df.describe())
