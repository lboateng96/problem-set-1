'''
PART 2: Merge and transform the data
- Read in the two datasets from /data into two separate dataframes
- Profile, clean, and standardize date fields for both as needed
- Merge the two dataframe for the date range 10/1/2024 - 10/31/2025
- Conduct EDA to understand the relationship between weather and transit ridership over time
-- Create a line plot of daily transit ridership and daily average temperature over the whole time period
-- For February 2025, create a scatterplot of daily transit ridership vs. precipitation
-- Create a correlation heatmap of all numeric features in the merged dataframe
-- Load the merged dataframe as a CSV into /data
-- In a print statement, summarize any interesting trends you see in the merged dataset

'''

#Write your code below
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def transform_load():

    # Read dataframe
    weather_df = pd.read_csv('data/weather_data.csv')
    transit_df = pd.read_csv('data/transit_data.csv')

    # Convert date format into YYYY-MM-DD 
    transit_df['service_date'] = pd.to_datetime(transit_df['service_date'])
    weather_df['datetime'] = pd.to_datetime(weather_df['datetime'])

    # Rename Transit date column from 'service_date' to 'datetime'
    transit_df = transit_df.rename(columns={'service_date': 'datetime'})

    # Filter transit data range 10/1/2024 - 10/31/2025
    transit_df = transit_df[(transit_df['datetime'] >= '2024-10-01') & (transit_df['datetime'] <= '2025-10-31')]

    # Merge df
    merged_df = pd.merge(weather_df, transit_df, on='datetime')

    # Line plot: daily ridership and avg temperature
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(merged_df['datetime'], merged_df['total_rides'], color='blue', label='Total Rides')
    ax1.set_ylabel('Total Rides', color='blue')
    ax2 = ax1.twinx()
    ax2.plot(merged_df['datetime'], merged_df['temp'], color='red', label='Avg Temp')
    ax2.set_ylabel('Temperature (C)', color='red')
    plt.title('Daily Transit Ridership and Average Temperature')
    plt.savefig('data/line_plot.png')
    plt.close()

    # Feb 2025 df and scatterplot
    feb2025_df = merged_df[(merged_df['datetime'] >= '2025-02-01') & (merged_df['datetime'] <= '2025-02-28')]
    plt.figure(figsize=(8, 6))
    plt.scatter(feb2025_df['precip'], feb2025_df['total_rides'])
    plt.xlabel('Precipitation')
    plt.ylabel('Total Rides')
    plt.title('February 2025: Ridership vs Precipitation')
    plt.savefig('data/scatter_plot.png')
    plt.close()

    # Correlation heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(merged_df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap of All Numeric Features')
    plt.savefig('data/heatmap.png')
    plt.close()

    # Merge df as CSV to /data
    merged_df.to_csv('data/merged_data.csv', index=False)

    # Print statement
    print("Trends: Ridership and temperature follow similar seasonal patterns with dips in winter months. " \
    "In February 2025, most days had low precipitation with consistently high ridership. " \
    "On higher precipitation days, ridership tended to decrease, suggesting extreme weather results in lower transit use. " \
    "The heatmap shows that weather variables are strongly correlated with each other, and transit variables (bus, rail, total rides) are strongly correlated with each other, but weather and transit variables do not show a strong correlation overall.")