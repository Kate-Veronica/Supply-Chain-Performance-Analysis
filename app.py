import streamlit as st
import pandas as pd

st.title("Supply Chain Project Overview")

try:
    data = pd.read_csv("cleaned_data.csv")
    st.success("✅ Data Loaded Successfully")
    st.dataframe(data.head())
except:
    st.warning("Upload cleaned_data.csv")

st.subheader("Basic KPIs")

if 'Sales' in data.columns:
    st.write("Total Sales:", data['Sales'].sum())
    st.write("Total Profit:", data['Order Profit Per Order'].sum())