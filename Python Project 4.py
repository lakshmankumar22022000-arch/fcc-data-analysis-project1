import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import the data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean the data: remove days in the top or bottom 2.5% of page views
low = df['value'].quantile(0.025)
high = df['value'].quantile(0.975)
df_clean = df[(df['value'] >= low) & (df['value'] <= high)]

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(15,5))  # Good width for time series
    ax.plot(df_clean.index, df_clean['value'], color='red', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.tight_layout()
    plt.close(fig)
    return fig

def draw_bar_plot():
    # Prepare data for bar chart
    df_bar = df_clean.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    # Pivot to year & months for mean aggregation
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    # Month order for display
    months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    # Ensure order (some groupbys show only months present