
# coding: utf-8

# Lets load the libraries
import pandas as pd
import datetime
import matplotlib.pyplot as plt

# Loading the data file we created with the previous script
traffic_df = pd.read_csv("traffic_per_minute.csv", encoding = "ISO-8859-1")

# just to make sure what we have
traffic_df.shape

traffic_df.head(5)

# Lets convert the datetime columne to the right type
traffic_df['datetime']=pd.to_datetime(traffic_df['datetime'])

# In order to make a simpler graph, lets create a date column that doesn't have 
# the time, this way is easier to group
traffic_df['date_minus_time'] = traffic_df['datetime'].apply(lambda traffic_df : datetime.datetime(year=traffic_df.year, month=traffic_df.month, day=traffic_df.day))

# now we take a look
traffic_df.head()

# now lets count the hits by date and plot it
traffic_day = pd.DataFrame(traffic_df['date_minus_time'].value_counts().reset_index())
traffic_day.columns = ['date', 'count']
traffic_day = traffic_day.sort_values(by='date', ascending=True)
plt.plot(traffic_day['date'], traffic_day['count'])


# we can also see the top countries that are looking at the site
traffic_country = pd.DataFrame(traffic_df['country'].value_counts().reset_index())
traffic_country.columns = ['country', 'count']
traffic_country = traffic_country.sort_values(by='count', ascending=False)
traffic_country_top15 = traffic_country.head(15)
plt.barh(traffic_country_top15['country'], traffic_country_top15['count'])


# as well as the top cities reaching the site
traffic_city = pd.DataFrame(traffic_df['city'].value_counts().reset_index())
traffic_city.columns = ['city', 'count']
traffic_city = traffic_city.sort_values(by='count', ascending=False)
traffic_city_top15 = traffic_city.head(15)
plt.barh(traffic_city_top15['city'], traffic_city_top15['count'])