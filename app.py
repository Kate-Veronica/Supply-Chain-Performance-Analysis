import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.title('Supply Chain Profitability Dashboard')

uploaded_file = st.file_uploader("Upload your cleaned_data.csv", type=["csv"])
if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file, encoding='latin1')
        data.columns = data.columns.str.strip()  
        st.success("✅ Data Loaded Successfully")
        st.dataframe(data.head())
    except Exception as e:
        st.error(f"Error loading CSV: {e}")
        st.stop()
else:
    st.info("Please upload your cleaned_data.csv to view the dashboard.")
    st.stop()

st.sidebar.header('Filters')
segment = st.sidebar.selectbox('Customer Segment', data['Customer Segment'].unique())
category = st.sidebar.selectbox('Category', data['Category Name'].unique())
market = st.sidebar.selectbox('Market', data['Market'].unique())

filtered = data[
    (data['Customer Segment'] == segment) &
    (data['Category Name'] == category) &
    (data['Market'] == market)
]

total_sales = filtered['Sales'].sum()
profit_col = 'Order Profit Per Order'
total_profit = filtered[profit_col].sum()
profit_margin = (total_profit / total_sales) * 100 if total_sales != 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric('Total Sales', f"${round(total_sales, 2):,}")
col2.metric('Total Profit', f"${round(total_profit, 2):,}")
col3.metric('Profit Margin %', f"{round(profit_margin, 2)}%")

st.subheader('Top Customers')
top_customers = filtered.groupby('Customer Id')[profit_col].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_customers)

st.subheader('Top Products')
top_products = filtered.groupby('Product Name')[profit_col].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_products)

st.subheader('Discount Rate vs Profit Margin')
if 'Order Item Discount Rate' in filtered.columns and 'Profit Margin' in filtered.columns:
    st.scatter_chart(filtered[['Order Item Discount Rate', 'Profit Margin']])

st.subheader('Data Preview')
st.dataframe(filtered.head(100))