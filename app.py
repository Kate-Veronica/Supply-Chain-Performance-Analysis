import streamlit as st
import pandas as pd
import zipfile
import io

st.set_page_config(layout='wide')
st.title("Supply Chain Profitability Dashboard")

uploaded_file = st.file_uploader("Upload cleaned_data.zip or cleaned_data.csv", type=["zip", "csv"])

data = None
if uploaded_file:
    if uploaded_file.name.endswith(".zip"):
        with zipfile.ZipFile(uploaded_file) as zf:
            with zf.open("cleaned_data.csv") as f:
                data = pd.read_csv(f, encoding='latin1')
    else:
        data = pd.read_csv(uploaded_file, encoding='latin1')

    data.columns = data.columns.str.strip()  
    st.success("Data Loaded Successfully")
    st.dataframe(data.head())

if data is not None:
    st.subheader("Basic KPIs")

    if 'Sales' in data.columns and 'Order Profit Per Order' in data.columns:
        total_sales = data['Sales'].sum()
        total_profit = data['Order Profit Per Order'].sum()
        margin = (total_profit / total_sales) * 100 if total_sales != 0 else 0

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Sales", round(total_sales, 2))
        col2.metric("Total Profit", round(total_profit, 2))
        col3.metric("Profit Margin %", round(margin, 2))

    st.sidebar.header("Filters")
    if 'Customer Segment' in data.columns:
        segment = st.sidebar.selectbox("Customer Segment", data['Customer Segment'].unique())
    else:
        segment = None
    if 'Category Name' in data.columns:
        category = st.sidebar.selectbox("Category", data['Category Name'].unique())
    else:
        category = None
    if 'Market' in data.columns:
        market = st.sidebar.selectbox("Market", data['Market'].unique())
    else:
        market = None

    filtered = data.copy()
    if segment:
        filtered = filtered[filtered['Customer Segment'] == segment]
    if category:
        filtered = filtered[filtered['Category Name'] == category]
    if market:
        filtered = filtered[filtered['Market'] == market]

    st.subheader("Top Customers")
    if 'Customer Id' in filtered.columns and 'Order Profit Per Order' in filtered.columns:
        top_customers = filtered.groupby('Customer Id')['Order Profit Per Order'].sum().sort_values(ascending=False).head(10)
        st.bar_chart(top_customers)

    st.subheader("Top Products")
    if 'Product Name' in filtered.columns and 'Order Profit Per Order' in filtered.columns:
        top_products = filtered.groupby('Product Name')['Order Profit Per Order'].sum().sort_values(ascending=False).head(10)
        st.bar_chart(top_products)

    st.subheader("Discount vs Profit Margin")
    if 'Order Item Discount Rate' in filtered.columns and 'Profit Margin' in filtered.columns:
        st.scatter_chart(filtered[['Order Item Discount Rate', 'Profit Margin']])

    st.subheader("Data Preview")
    st.dataframe(filtered.head(100))