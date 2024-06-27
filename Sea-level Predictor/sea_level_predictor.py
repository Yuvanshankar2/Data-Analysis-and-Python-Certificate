import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    sea_level = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(sea_level['Year'].array, sea_level['CSIRO Adjusted Sea Level'].array)

    # Create first line of best fit
    fit = linregress(sea_level['Year'].array, sea_level['CSIRO Adjusted Sea Level'].array)
    x= pd.Series(year for year in range(1880,2051))
    y = fit.slope * x + fit.intercept
    plt.plot(x,y,'blue')

    # Create second line of best fit
    sea_level_new = sea_level[sea_level['Year']>=2000]
    secondfit = linregress(sea_level_new['Year'].array, sea_level_new['CSIRO Adjusted Sea Level'].array)
    x1= pd.Series(year for year in range(2000,2051))
    y1 = secondfit.slope * x1 + secondfit.intercept
    plt.plot(x1,y1,'red')
     

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')   
    plt.title('Rise in Sea Level') 
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()