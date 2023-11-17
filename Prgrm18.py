import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 22, 24, 23, 25],
        'School Code': ['S001', 'S002', 'S001', 'S003', 'S002'],
        'Class': ['A', 'B', 'A', 'C', 'B']}
df = pd.DataFrame(data)
grouped = df.groupby(['School Code', 'Class'])
for group, group_df in grouped:
    print("Group:", group)
    print(group_df)
