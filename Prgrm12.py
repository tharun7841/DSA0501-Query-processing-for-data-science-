import pandas as pd
import numpy as np
from IPython.display import display, HTML
data = {
    'Column1': np.random.rand(10),
    'Column2': np.random.rand(10),
    'Column3': np.random.rand(10),
    'Column4': np.random.rand(10)
}
df = pd.DataFrame(data)
def highlight(val):
    return 'background-color: black; color: yellow;'
styled_df = df.style.applymap(highlight)
display(HTML(styled_df.render()))
