import pandas as pd

data = pd.read_csv('APL_Logistics.csv', encoding = 'latin1')

data = data[(data['Sales']>0)&(data['Order Profit Per Order'] !=0 )]

if 'Order Date' in data.columns:
    data['Order Date'] = pd.to_datetime(data['Order Date'], errors = 'coerce')

data = data.dropna()

data['Profit Margin'] = (data['Order Profit Per Order']/data['Sales']) * 100

data.reset_index(drop = True, inplace = True)

data.to_csv('cleaned_data.csv', index = False)

print('Data cleaned Successfully')