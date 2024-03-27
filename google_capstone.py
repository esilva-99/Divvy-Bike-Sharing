#importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
import seaborn as sns

#importing all 12 months of data
df1= pd.read_csv('202301-divvy-tripdata.csv')
df2= pd.read_csv('202302-divvy-tripdata.csv')
df3= pd.read_csv('202303-divvy-tripdata.csv')
df4= pd.read_csv('202304-divvy-tripdata.csv')
df5= pd.read_csv('202305-divvy-tripdata.csv')
df6= pd.read_csv('202306-divvy-tripdata.csv')
df7= pd.read_csv('202307-divvy-tripdata.csv')
df8= pd.read_csv('202308-divvy-tripdata.csv')
df9= pd.read_csv('202309-divvy-tripdata.csv')
df10= pd.read_csv('202310-divvy-tripdata.csv')
df11= pd.read_csv('202311-divvy-tripdata.csv')
df12= pd.read_csv('202312-divvy-tripdata.csv')

#Combining into one dataframe 
tripdata_2023 = pd.concat([df1, df2, df3, df4, df5,df6, df7, df8, df9, df10, df11, df12])

#Checking the name of all the series
column_names = tripdata_2023.columns
#print(column_names)

#print(tripdata_2023.head())
#checking number of columns and rows
#print(tripdata_2023.shape[1])
#print(tripdata_2023.shape[0])

#checking the data_types
    #print(tripdata_2023.dtypes)

######################################### Data Cleaning & Transformation ################################

#Idenitfying null values
null_count= tripdata_2023.isnull().sum()
#print(null_count)

#Drop nulls
tripdata_2023= tripdata_2023.dropna()

#null count after removal
#print(tripdata_2023.isnull().sum())

#Checking for duplicate rows--> there are no duplicate rows
nduplicate_rows = tripdata_2023.duplicated().sum()
#print(nduplicate_rows)

#Checking for duplicate ride id's
duplicate_ids= tripdata_2023['ride_id'].duplicated().any()
#print(duplicate_ids)

#On Divvy's website they state that the data has been processed to remove the trips that were 
#taken by staff to inspect and service, as well as any other trip below 60 seconds as potentially false starts. I'm going to double check thhat all were in fact removed.

#print(tripdata_2023['start_station_name'].str.contains('Base|Test|Charging', case=False).sum())
#print(tripdata_2023['end_station_name'].str.contains('Base|Test|Charging', case=False).sum())

#Dropping service trips

tripdata_2023 = tripdata_2023[~tripdata_2023['start_station_name'].str.contains('Base|Test|Charging', case=False)]
tripdata_2023 = tripdata_2023[~tripdata_2023['end_station_name'].str.contains('Base|Test|Charging', case=False)]


#Checking that it removed all the test/service data
#print(tripdata_2023['start_station_name'].str.contains('Base|Test|Charging', case=False).sum())
#print(tripdata_2023['end_station_name'].str.contains('Base|Test|Charging', case=False).sum())

#Checking and removing rides less than 60 seconds
#First I will need to convert started_at and ended_at into datetime format

tripdata_2023['started_at']= pd.to_datetime(tripdata_2023['started_at'], format="%Y-%m-%d %H:%M:%S")
tripdata_2023['ended_at']= pd.to_datetime(tripdata_2023['ended_at'], format="%Y-%m-%d %H:%M:%S")

# Creating a series for trip_duration
tripdata_2023['trip_duration'] = tripdata_2023['ended_at']-tripdata_2023['started_at']
#print(tripdata_2023.head())

#Excluding trips that are negative and are less than 60 seconds
tripdata_2023 = tripdata_2023[tripdata_2023['trip_duration'] > '0 days 00:01:00']

#Excluding trips longer than 24 hrs because by policy it needs to be returned within 24 hrs time-frame
tripdata_2023 = tripdata_2023[tripdata_2023['trip_duration'] <= '1 days 00:00:00']


#Excluding trips that are less than 5 minutes that begin and end in the same station as likely error
tripdata_2023 = tripdata_2023[((tripdata_2023['start_station_id'] != tripdata_2023['end_station_id']) & (tripdata_2023['trip_duration'] > '0 days 00:05:00'))]

# Creating a series for the days of the week to use for analysis. Only need for started_at since all trips = or > 24 hrs were deleted
tripdata_2023['week_day'] = tripdata_2023['started_at'].dt.day_name()
#print(tripdata_2023['week_day'])

#Creating a series which shows if it's a weekday or weekend
def categorize_day(day_name):
    if day_name in ['Saturday', 'Sunday']:
        return 'Weekend'
    else:
        return 'Weekday'

tripdata_2023['weekday_or_weekend'] = tripdata_2023['week_day'].apply(categorize_day)

#checking to see if function worked--> it did
#print(tripdata_2023['weekday_or_weekend'], tripdata_2023['week_day'])

#Creating a series for the month in which rides take place
tripdata_2023['month']=tripdata_2023['started_at'].dt.month_name()

####################################### Analyzing and Visualizing Data ########################################

#how many riders are casual vs members
count_member_type = tripdata_2023['member_casual'].value_counts()
#print(count_member_type)

#Pie chart of casual vs member riders
#plt.pie(count_member_type, labels=count_member_type.index, autopct='%1.1f%%', startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle
#plt.axis('equal')

# Display the plot
#plt.show()

#Finding average ride_length
#First need to convert to seconds
trip_duration_seconds= tripdata_2023['trip_duration'].dt.total_seconds()
mean_trip_duration_s = trip_duration_seconds.mean()
#print(mean_trip_duration_s)

#how do average ride lengths differ between members and non-members
avg_group_ride_len_m = tripdata_2023.groupby('member_casual')['trip_duration'].mean().dt.total_seconds()/60
#print(avg_group_ride_len_s)

#Round the average to the nearest second
rounded_avg_ride_len = round(avg_group_ride_len_m)
#print(rounded_avg_ride_len)

#Converting back to timedelta format????????????????????????
#rounded_avg_trip_len_timedelta = pd.to_timedelta(rounded_avg_ride_len, unit='s')
#group_avg_len = rounded_avg_trip_len_timedelta
#print(group_avg_len)

#------Analyzing number of rides acorss weekdays
weekday_rides = tripdata_2023.groupby('member_casual')['week_day'].value_counts()

#Pivot the weekdayrides data so it is more clear to read
weekday_rides= weekday_rides.unstack()

#Melt the pivoted DataFrame to create a barplot
melted_data = weekday_rides.reset_index().melt(id_vars='member_casual', var_name='week_day', value_name='count')
#print(melted_data)

days_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Create the grouped bar chart
plt.figure(figsize=(12,6))
sns.set(style="whitegrid")
sns.barplot(x='week_day', y='count', hue='member_casual', data=melted_data, order=days_order, dodge=True)
plt.title('Week Day Counts by Member Type')
#plt.show()

#What are the most popular start_stations and end_stations
start_station_count= tripdata_2023['start_station_id'].value_counts().nlargest(10)
#print(start_station_count)
end_station_count= tripdata_2023['start_station_id'].value_counts().nlargest(10)
#print(end_station_count)

#viz of most popular stations

# Create a bar plot for start stations
plt.figure(figsize=(12, 6))
sns.barplot(x=start_station_count.index, y=start_station_count.values)
plt.title('Top 10 Start Stations')
plt.xlabel('Station ID')
plt.ylabel('Count')
plt.xticks(rotation=90)
#plt.show()

# Create a bar plot for end stations
plt.figure(figsize= (12, 6))
sns.barplot(x=end_station_count.index, y=end_station_count.values, color='orange')
plt.title('Top 10 End Stations')
plt.xlabel('Station ID')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
#plt.show()

#-----------------Finding the most popular months to ride
#Analyzing number of riders across different months (monthly)
monthly_count= tripdata_2023['month'].value_counts

#Analyzing rider type across different months
member_type_monthly_cnt= tripdata_2023.groupby('member_casual')['month'].value_counts()
#print(member_type_monthly_cnt)

#Pivoting the rider type across different months
pivoted_data_monthly_cnt= member_type_monthly_cnt.unstack()
#print(pivoted_data_monthly_cnt)

#melt the data
melted_monthly = pivoted_data_monthly_cnt.reset_index().melt(id_vars='member_casual', var_name='month', value_name='count')

#Viz for rider type across different months
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

plt.figure(figsize=(12, 6))
sns.barplot(x='month', y='count', hue='member_casual', data= melted_monthly, order=months_order)
plt.title('Monthly Distribution of Bike usage Based on Membership Status')
plt.xlabel('Month')
plt.ylabel('Count')
#plt.show()

#------is a certain type of bike rented more during a certain period of the week 
bike_count_type = tripdata_2023['rideable_type'].value_counts()
#print(bike_count_type)

#pie chart
plt.figure()
plt.pie(bike_count_type, labels= bike_count_type.index, autopct='%1.1f%%')
plt.title('Share of Bike Types Available')
#plt.show()

#Bike type distribution acorss different membership status
biketype_memberstatus= tripdata_2023.groupby('member_casual')['rideable_type'].value_counts()

# Pivot the data to create a DataFrame suitable for plotting
biketype_memberstatus_pivoted = biketype_memberstatus.unstack()

# Plotting the stacked bar plot
from matplotlib.ticker import FuncFormatter
ax= biketype_memberstatus_pivoted.plot(kind='bar', stacked=True, figsize=(10, 6))
def format_yticks(y, pos):
    return '{:.0f}K'.format(y / 1000)

ax.yaxis.set_major_formatter(FuncFormatter(format_yticks))
# Add labels and title
plt.xlabel('Member Status')
plt.ylabel('Count')
plt.title('Count of Bike Types Used by Customers of Different Membership Status')

#Rotate the labels from vertical to horizontal
plt.xticks(rotation=0)

# Show plot
plt.show()










