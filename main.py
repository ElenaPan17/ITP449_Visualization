""" Elena Pan
    ITP-449
    Assignment 5
    Avocados
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates
from datetime import datetime

def main():
    # import the avocado file and read as a dataframe
    file = 'avocado.csv'
    df = pd.read_csv(file)

    # select Date, AveragePrice, Total Volume columns from dataframe
    df = df[['Date', 'AveragePrice', 'Total Volume']]

    # convert the Date column to a timestamp using datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # dataframe is sorted by Date
    df.sort_values(by='Date', inplace=True)

    # create a new column called TotalRevenue = AveragePrice*Total Volume
    df['TotalRevenue'] = df['AveragePrice']*df['Total Volume']

    # group the dataframe with selected column by date and aggregate with a sum
    data_group = df.groupby(by = ['Date']).sum()
    
    # recalculate the AveragePrice
    data_group['AveragePrice'] = data_group['TotalRevenue']/data_group['Total Volume']

    # 2x3 subplot grid
    fig, ax = plt.subplots(2, 3, sharex = True)
    plt.xticks(rotation = '90')

    # plot the Average Price vs Time
    ax[0,0].scatter(df['Date'], df['AveragePrice'], s = 10)
    ax[0,0].set(title='Raw', ylabel='Average Price ($USD)')
    # plot the Total Volume vs Time
    ax[1,0].scatter(df['Date'], df['Total Volume'], s = 10)
    ax[1,0].set(ylabel='Total Volume (millions)')
    for item in ax[1,0].axes.get_xticklabels():
        item.set_rotation(90)
    
    # Plot the aggregated AveragePrice vs Time
    ax[0,1].plot(data_group['AveragePrice'], marker = 'o', linestyle = '-', markersize = 2)
    ax[0,1].set(title='Aggregated')
    # Plot the aggregated Total Volume vs Time
    ax[1,1].plot(data_group['Total Volume'], marker = 'o', linestyle = '-', markersize = 2)
    for item in ax[1,1].axes.get_xticklabels():
        item.set_rotation(90)

    # Plot the smoothed aggregated AveragePrice vs Time
    ax[0,2].plot(data_group['AveragePrice'].rolling(20).mean(), marker = 'o', linestyle = '-', markersize = 3)
    ax[0,2].set(title='Smoothed')
    # Plot the smoothed aggregated Total Volume vs Time
    ax[1,2].plot(data_group['Total Volume'].rolling(20).mean(), marker = 'o', linestyle = '-', markersize = 3)
    for item in ax[1,1].axes.get_xticklabels():
        item.set_rotation(90)

    # share x labels
    plt.setp(ax[-1:,], xlabel = 'Time')
    
    # tight layout
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])

    # suptitle and save the figuer 
    plt.suptitle('Avocado Prices and Volume Time Series')
    plt.savefig('Figuer 1.png')


if __name__ == '__main__':
    main()
