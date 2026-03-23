import streamlit as st
import pandas as pd

st.set_page_config(layout = 'wide')
st.title('Supply Chain Profitablity Dashboard')

data = pd.read_csv('cleaned_data.csv')

st.sidebar.header('Filters')

segment = st.sidebar.selectbox('Customer Segment', data['Customer Segment'].unique())
category = st.sidebar.selectbox('Category',data['Category Name'].unique())
market = st.sidebar.selectbox('Market', data['Market'].unique())

filtered = data [
    (data['Customer Segment'] == segment)&
    (data['Category Name'] == category)&
    (data['Market'] == market)
]

total_sales = filtered['Sales'].sum()
total_profit = filtered['Order Profit Per Order'].sum()
margin = (total_profit / total_sales)*100 if total_sales !=0 else 0

col1, col2, col3 = st.columns(3)

col1.metric('Total Sales',round(total_sales, 2))
col2.metric('Total Profit',round(total_profit, 2))
col3.metric('Profit Margin %', round(margin, 2))

st.subheader('Top Customer')
top_customers = filtered.groupby('Customer Id')['Order Profit Per Order'].sum().sort_values(ascending = False).head(10)
st.bar_chart(top_customers)

st.subheader('Top Product')
top_products = filtered.groupby('Product Name')['Order Profit Per Order'].sum().sort_values(ascending = False).head(10)
st.bar_chart(top_products)

st.subheader('Discount vs Profit Margin')
if 'Order Item Discount Rate' in data.columns:
    st.scatter_chart(data[['Order Item Discount Rate', 'Profit Margin']])

st.subheader('Data Preview')
st.dataframe(filtered.head(100))
