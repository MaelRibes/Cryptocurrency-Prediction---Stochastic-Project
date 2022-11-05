import pandas as pd
import matplotlib.pyplot as plt
from os import listdir
import seaborn as sb
import numpy as np

# Get the csv files in the output folder
crypto_list = [file for file in listdir('./output')]

# Joins all dataframes into one
data = pd.DataFrame()
for crypto in crypto_list:
    df = pd.read_csv(f'./output/{crypto}', parse_dates=['timestamp'])[['timestamp', 'close']]
    df.set_index('timestamp', inplace=True)
    df = df.add_suffix(f"_{crypto.split('-')[0]}")
    rows = df[df[f"close_{crypto.split('-')[0]}"] == 0].index # Check for rows with empty closes values
    df.drop(rows, inplace=True)
    if data.empty: 
        data = df
    else:
        data = data.join(df, how='inner')

# Calculate the percent change per day and the correlation matrix
data_pct_change = data.pct_change()[1:]
correlation = data_pct_change.corr()
correlation = correlation.round(2)

# Shows the correlation matrix as a heatmap
f, ax = plt.subplots(figsize=(len(correlation), len(correlation)))
mask = np.triu(np.ones_like(correlation, dtype=bool))
sb.heatmap(correlation, annot=True, mask = mask)
plt.title('Correlation between each cryptocurrencies')
plt.show()