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