import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 22, 24, 23, 25],
        'School Code': ['S001', 'S002', 'S001', 'S003', 'S002']}
df = pd.DataFrame(data)
result = df.groupby('School Code')['Age'].agg(['mean', 'min', 'max'])
result = result.rename(columns={'mean': 'Mean Age', 'min': 'Min Age', 'max': 'Max Age'})
print(result)
