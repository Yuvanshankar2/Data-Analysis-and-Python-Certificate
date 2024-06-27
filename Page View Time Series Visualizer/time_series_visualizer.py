import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=["date"], index_col="date")

# Clean data
df = df[~((df['value']>=df['value'].quantile(0.975)) | (df['value']<=df['value'].quantile(0.025)))]


def draw_line_plot():
    # Draw line plot

    fig = plt.figure()
    plt.plot(df.index.array,df['value'].array,'r')

    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['Year'] = df.index.year
    df['Month'] = df.index.month
    df_group=df.groupby(['Year','Month'])
    df_bar = df_group['value'].mean()
    df_bar = df_bar.unstack()

   
    # Draw bar plot 
    fig, ax = plt.subplots(figsize=(20,20))
    df_bar.plot(kind='bar',legend=True,ax=ax)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(['January','February','March','April','May','June','July','August','September','October','November','December'])




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2,figsize=(14,7))
    sns.boxplot(x=df_box['year'],y=df_box['value'].astype('float'),ax=ax[0])
    sns.boxplot(x=df_box['month'],y=df_box['value'].astype('float'), order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],ax=ax[1])
    
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')

    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
