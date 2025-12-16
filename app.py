import streamlit as st
import pandas as pd
from scoring import calculate_score

st.set_page_config(page_title="Lead Probability Engine", layout="wide")

st.title("🧪 3D In-Vitro Lead Generation Dashboard")
st.write("AI-assisted prioritization of high-intent scientific decision makers")

# Load data
df = pd.read_csv("C:\Users\misbah uddin\OneDrive\Desktop\lead probability engine\lead.csv")
df["Probability"] = df.apply(calculate_score, axis=1)

# Ranking
df = df.sort_values(by="Probability", ascending=False)
df.insert(0, "Rank", range(1, len(df) + 1))

# Search
search = st.text_input("🔍 Search by name, title, company, location")

if search:
    df = df[df.apply(
        lambda row: search.lower() in row.astype(str).str.lower().to_string(),
        axis=1
    )]

# Display
st.dataframe(
    df,
    use_container_width=True
)

# Export
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    "⬇ Download as CSV",
    csv,
    "ranked_leads.csv",
    "text/csv"

)
