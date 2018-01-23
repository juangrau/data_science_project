# -*- coding: utf-8 -*-
"""
@author: juang_000
"""
#Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import random

# Load and check data files
traffic_per_day = pd.read_csv("C:/Users/juang_000/Documents/Personal/VanHack/trafficdata.csv")
traffic_per_day.shape
traffic_per_day.head(5)
traffic_per_day.describe()

country_codes_data = pd.read_csv("C:/Users/juang_000/Documents/Personal/VanHack/country_codes_data.csv")
country_codes_data.shape
country_codes_data.head(5)
country_codes_data.describe()

cities_per_country = pd.read_csv("C:/Users/juang_000/Documents/Personal/VanHack/cities_per_country.csv")
cities_per_country.shape
cities_per_country.head(5)
cities_per_country.describe()d

# function to get a random datetime based on a start date
def get_random_time(start_date):
    #86400 seconds in a day
    seconds=random.randint(0, 86400)
    return start_date + datetime.timedelta(0, seconds)


# A combination of fake web traffic data, countries and cities is made
traffic_per_minute = pd.DataFrame(columns=['datetime', 'city', 'country'])
for index, row in traffic_per_day.iterrows():
    year = int(str(row['date'])[0:4])
    month = int(str(row['date'])[4:6])
    day = int(str(row['date'])[6:8])
    this_date = datetime.datetime(year, month, day, 0, 0, 0)
    num_logs = row['daily_hits']
    country_code = row['country']
    country = country_codes_data.loc[country_codes_data['Code'] == country_code, 'Name'].item()
    for x in range(num_logs):
        radom_datetime = get_random_time(this_date)        
        random_datetime_str = radom_datetime.strftime("%Y-%m-%d %H:%M")
        cities  = cities_per_country.loc[cities_per_country['Country'] == country_code.lower(), 'City'].tolist()
        if(len(cities)==0):
            random_city = country
        else:
            random_city = cities[random.randint(0, len(cities)-1)]
        traffic_row = [random_datetime_str, random_city, country]
        traffic_per_minute.loc[len(traffic_per_minute)] = traffic_row
        
# Save the result to a csv file for further analysis        
traffic_per_minute.to_csv("C:/Users/juang_000/Documents/Personal/VanHack/traffic_per_minute.csv")             
