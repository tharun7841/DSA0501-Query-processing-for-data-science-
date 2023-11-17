import pandas as pd
data = {
    'Item': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C'],
    'Sale': [100, 150, 200, 120, 250, 180, 220, 130, 160]
}
sales_data = pd.DataFrame(data)
pivot_table = sales_data.pivot_table(index='Item', values='Sale', aggfunc={'Sale': ['max', 'min']})
pivot_table.columns = ['Max Sale', 'Min Sale']
print(pivot_table)
