import pandas as pd
data = {'Column1': ['apple', 'banana', 'cherry', 'date', 'elderberry']}
df = pd.DataFrame(data)
substring = 'erry'
index_of_substring = df['Column1'].str.find(substring)
df['Index_of_Substring'] = index_of_substring
print(df)
