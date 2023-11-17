import pandas as pd
import numpy as np
data = {'A': [1, 2, None, 4, None],
        'B': [None, 2, 3, None, None],
        'C': [1, 2, None, None, 5]}

df = pd.DataFrame(data)
threshold = 2
filtered_df = df.dropna(thresh=threshold)
print(filtered_df)
