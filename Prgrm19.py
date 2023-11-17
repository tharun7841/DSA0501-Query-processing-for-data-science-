import pandas as pd
data = {
    'Year': [1986, 1986, 1986, 1986, 1985],
    'WHO region': ['Western Pacific', 'Americas', 'Africa', 'Americas', 'Americas'],
    'Country': ["Viet Nam", "Uruguay", "Cote d'Ivoire", "Colombia", "Saint Kitts"],
    'Beverage Types': ['Wine', 'Other', 'Wine', 'Beer', 'Beer'],
    'Display Value': [0.00, 0.50, 3.62, 4.27, 1.98]
}
df = pd.DataFrame(data)
shape = df.shape
print("Shape of the DataFrame:", shape)
column_names = df.columns
print("Column Names:", column_names) 
