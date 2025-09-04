import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Read data
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')

# Line of best fit for all data
res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
x_pred_all = range(df['Year'].min(), 2051)
y_pred_all = res_all.slope * pd.Series(x_pred_all) + res_all.intercept
plt.plot(x_pred_all, y_pred_all, 'r', label='Best Fit: 1880-2050')

# Line of best fit from year 2000
df_recent = df[df['Year'] >= 2000]
res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
x_pred_recent = range(2000, 2051)
y_pred_recent = res_recent.slope * pd.Series(x_pred_recent) + res_recent.intercept
plt.plot(x_pred_recent, y_pred_recent, 'g', label='Best Fit: 2000-2050')

# Labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Save image
plt.savefig('sea_level_plot.png')
plt.show()