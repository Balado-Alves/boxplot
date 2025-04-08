import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col=0)
#print(df)

# Clean data
mask=(df['value']>=df['value'].quantile(0.025)) & (df['value']<=df['value'].quantile(0.975))
df = df[mask]
#print(df)


def draw_line_plot():
    # Draw line plot
    fig=plt.figure(figsize=(15,5),dpi=150)
    plt.plot(df, color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.resample('M').mean()
    df_bar=df_bar.reset_index()
    df_bar['month']=df_bar['date'].dt.month
    df_bar['year']=df_bar['date'].dt.year
    df_bar=df_bar.drop('date', axis=1)
    df_bar['month_name'] = pd.to_datetime(df_bar['month'], format='%m').dt.strftime('%B')
    df_bar=df_bar.drop('month', axis=1)
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
    df_bar['month_name'] = pd.Categorical(df_bar['month_name'], categories=month_order, ordered=True)

    fig=plt.figure(figsize=(10,10),dpi=150)
    sns.barplot(data=df_bar, x='year', y='value', hue='month_name', palette='bright')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['month']=df_box['date'].dt.month
    df_box['year']=df_box['date'].dt.year
    df_box=df_box.drop('date', axis=1)
    df_box['month_name'] = pd.to_datetime(df_box['month'], format='%m').dt.strftime('%b')
    df_box=df_box.drop('month', axis=1)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month_name'] = pd.Categorical(df_box['month_name'], categories=month_order, ordered=True)

    # Draw box plots (using Seaborn)
    plt.figure(figsize=(16, 6))

    plt.subplot(1, 2, 1)
    sns.boxplot(data=df_box, x='year', y='value', hue='year', palette='bright', legend=False)
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.title('Year-wise Box Plot (Trend)')

    plt.subplot(1, 2, 2)
    sns.boxplot(data=df_box, x='month_name', y='value', hue='month_name', palette='muted', legend=False)
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.title('Month-wise Box Plot (Seasonality)')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
