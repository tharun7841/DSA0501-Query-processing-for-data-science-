import pandas as pd
import numpy as np
data = {
    'Column1': np.random.uniform(-1, 1, 10),
    'Column2': np.random.uniform(-1, 1, 10),
    'Column3': np.random.uniform(-1, 1, 10),
    'Column4': np.random.uniform(-1, 1, 10)
}

df = pd.DataFrame(data)
def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'
styled_df = df.style.applymap(color_negative_red)
styled_df
