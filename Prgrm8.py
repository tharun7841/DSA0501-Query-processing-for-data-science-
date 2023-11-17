import pandas as pd
data = {
    'Item': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C'],
    'Units Sold': [10, 15, 20, 12, 25, 18, 22, 13, 16]
}
sales_data = pd.DataFrame(data)
pivot_table = sales_data.pivot_table(index='Item', values='Units Sold', aggfunc='sum')
pivot_table.columns = ['Total Units Sold']
print(pivot_table)
