import pandas as pd
import numpy as np
data = {'A': [1, 2, None, 4, 5],
        'B': [None, 2, 3, None, 5],
        'C': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
value_to_replace = -1
df_filled = df.fillna(value_to_replace)
print(df_filled)
