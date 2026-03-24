# Customer, Product, and Profitability Performance Analysis in Supply Chain Operations: A Case Study of APL Logistics

### DataSet:
[https://drive.google.com/file/d/1Q9jaN5fup2ieiLH4arzzLbduI2oljCXu/view?usp=drive_link]

### Live Dashboard:
[https://supply-chain-performance-analysis-aeskuqpkhtwa9fp5crzewm.streamlit.app/]

### Report Paper:
[https://docs.google.com/document/d/1OfMF00uoMlAowwR9I4V2YFWHcZqpnn3R5cT-Fy-J030/edit?usp=drive_link]

## Project Overview
This project seeks to analyze the performance of customers, products, and the market in the operations of the supply chain with the aim of identifying profitability and areas of inefficiency. This is particularly aimed at finding areas where high sales do not necessarily mean high profitability.

## Objective
- Evaluate revenue and profit performance
- Identify high-value customers
- Analyze product and category profitability
- Understand the impact of discounts on margins
- Build an interactive dashboard for insights

## Tech Stack
- Python
- Pandas
- Matplotlib
- Streamlit

## Project Structure
```
├── data_cleaning.py        # Data preprocessing and feature engineering
├── analysis.py             # EDA and visualization
├── dashboard.py            # Basic Streamlit dashboard
├── app.py                  # Advanced Streamlit app with file upload
├── create_zip.py           # Utility for dataset packaging
├── requirements.txt        # Dependencies
├── runtime.txt             # Python version
├── cleaned_data.csv/zip    # Processed dataset
├── images/                 # Generated charts

```

## Key Features
- Data cleaning and validation
- Computation of KPIs (Sales, Profit, Margin)
- Customer and product profitability analysis
- Visualization of the impact of discounts
- Interactive dashboard with filters

## Key Insights
- High revenue is not necessarily equal to high profit
- Discounts have a significant impact on profit margins
- Profit is concentrated in a few customers
- There are markets that are rich in revenue but poor in profit

## How to Run
# 1. Install Dependencies
```
pip install -r requirements.txt
```
# Run the Application
```
streamlit run app.py
```

## Dashboard Features
- KPI Overview (Sales, Profit, Margin)
- Top customers and products
- Discount vs Profit Margin analysis
Filters:
- Customer Segment
- Category
- Market

## Use Cases
- Business Performance analysis
- Pricing Strategy optimization
- Customer segmentation
- Supply Chain decision-making

## Author 
Kate Veronica Theetla
