import pandas as pd
import matplotlib.pyplot as plt
import os

data = pd.read_csv('cleaned_data.csv', encoding='latin1') 
data.columns = data.columns.str.strip()  

os.makedirs('images', exist_ok=True)

total_sales = data['Sales'].sum()
total_profit_col = 'Order Profit Per Order'  
total_profit = data[total_profit_col].sum()
profit_margin = (total_profit / total_sales) * 100

print('\n--- KPI Overview ---')
print('Total Sales:', round(total_sales, 2))
print('Total Profit:', round(total_profit, 2))
print('Profit Margin:', round(profit_margin, 2))

if 'Order Date' in data.columns:
    data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')
    monthly = data.groupby(data['Order Date'].dt.to_period('M')).sum().reset_index()

    plt.figure()
    plt.plot(monthly['Order Date'].astype(str), monthly['Sales'], label='Sales')
    plt.plot(monthly['Order Date'].astype(str), monthly[total_profit_col], label='Profit')
    plt.xticks(rotation=45)
    plt.legend()
    plt.title('Monthly Trend')
    plt.tight_layout()
    plt.savefig('images/monthly_trend.png')
    plt.close()

top_products = data.groupby('Product Name')[total_profit_col].sum().sort_values(ascending=False).head(10)
plt.figure()
top_products.plot(kind='barh')
plt.title('Top Products by Profit')
plt.tight_layout()
plt.savefig('images/top_products.png')
plt.close()

top_customers = data.groupby('Customer Id')[total_profit_col].sum().sort_values(ascending=False).head(10)
plt.figure()
top_customers.plot(kind='barh')
plt.title('Top Customers by Profit')
plt.tight_layout()
plt.savefig('images/top_customers.png')
plt.close()

if 'Order Item Discount Rate' in data.columns and 'Profit Margin' in data.columns:
    plt.figure()
    plt.scatter(data['Order Item Discount Rate'], data['Profit Margin'])
    plt.xlabel('Discount Rate')
    plt.ylabel('Profit Margin')
    plt.title('Discount vs Profit')
    plt.tight_layout()
    plt.savefig('images/discount_vs_margin.png')
    plt.close()

if 'Market' in data.columns:
    market = data.groupby('Market')[total_profit_col].sum()
    plt.figure()
    market.plot(kind='bar')
    plt.title('Profit by Market')
    plt.tight_layout()
    plt.savefig('images/market_profit.png')
    plt.close()

print('\n Analysis Completed. \n Charts saved in images.')