'''
PART 1: EXTRACT WEATHER AND TRANSIT DATA

Pull in data from two dataset
1. Weather data from visualcrossing's weather API (https://www.visualcrossing.com/weather-api)
- You will need to sign up for a free account to get an API key
-- You only get 1000 rows free per day, so be careful to build your query correctly up front
-- Though not best practice, include your API key directly in your code for this assignment
- Write code below to get weather data for Chicago, IL for the date range 10/1/2024 - 10/31/2025
- The default data fields should be sufficient
2. Daily transit ridership data for the Chicago Transit Authority (CTA)
- Here is the URL: ttps://data.cityofchicago.org/api/views/6iiy-9s97/rows.csv?accessType=DOWNLOAD"

Load both as CSVs into /data
- Make sure your code is line with the standards we're using in this class 
'''

#Write your code below
import csv
import codecs
import urllib.request
import urllib.error
import sys
import os

def extract_weather_data():
    # Define the API key and parameters
    ApiKey = 'ARR7YAWSVJ28SV36QN7HRS73S'
    Location = 'Chicago,IL'
    StartDate = '2024-10-01'
    EndDate = '2025-10-31'
    UnitGroup = 'metric'
    ContentType = 'csv'
    Include = 'days'

    # Construct the API query
    BaseURL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
    ApiQuery = f"{BaseURL}{Location}/{StartDate}/{EndDate}"
    ApiQuery += f"?unitGroup={UnitGroup}&contentType={ContentType}&include={Include}&key={ApiKey}"

    try:
        print('Running query URL: ', ApiQuery)
        response = urllib.request.urlopen(ApiQuery)
        csv_bytes = response.read()
        csv_text = csv.reader(csv_bytes.decode('utf-8').splitlines())

        # Save to /data folder
        os.makedirs('data', exist_ok=True)
        with open('data/weather_data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for row in csv_text:
                writer.writerow(row)

        print('Weather data saved to data/weather_data.csv')

    except urllib.error.HTTPError as e:
        ErrorInfo = e.read().decode()
        print('Error code: ', e.code, ErrorInfo)
        sys.exit()
    except urllib.error.URLError as e:
        ErrorInfo = str(e.reason)
        print('Network error: ', ErrorInfo)
        sys.exit()



# Extract CTA transit ridership data
def extract_transit_data():
    url = 'https://data.cityofchicago.org/api/views/6iiy-9s97/rows.csv?accessType=DOWNLOAD'
    
    try:
        print('Downloading CTA transit data...')
        response = urllib.request.urlopen(url)
        csv_bytes = response.read()
        csv_text = csv.reader(csv_bytes.decode('utf-8').splitlines())
        
        os.makedirs('data', exist_ok=True)
        with open('data/transit_data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for row in csv_text:
                writer.writerow(row)
        
        print('Transit data saved to data/transit_data.csv')
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code, e.read().decode())
        sys.exit()
    except urllib.error.URLError as e:
        print('Network error: ', str(e.reason))
        sys.exit()