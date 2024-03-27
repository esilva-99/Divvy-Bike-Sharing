This project is part of my Google Data Analytics Certificate. The project features data from Divvy Bikes, a bike-sharing company. The project aims to understand how the company's casual riders (those without an annual membership) differ from those who are members (those who have a annual membership). The goal is to use this knowledge to create a successful marketing strategy to convert casual riders into members. 

I utilized Python to prepare, clean, analyze, and visualize the data. 

1. Cleaning The Data
To begin with the data had many entries with nulls. The series with null values where station names, station id, latitude, and longitude. At first I tried to use other rows with similar latitudes and longitudes to match it with rows missing station names and id's. However, sionce the coordinates are in rounded to differing degrees of accuracy, and coordinates need to be rounded to at least four decimal places to be able to ditinguish one station from the other, I could not proceed. Without more informnation provided I had to drop all nulls from the dataset for it to be usable. Beacuse the dataset is so large compared the number of null rows, deleting the null entries will not significantly skew the data.

Cleaning the data also included removing entries that were not actual trips. I removed trips which were less than 60 seconds, greater than 24 hours, and that were for testing/service purposes. Additionally, I removed trips beginning and ending in the same station which were shorter than five minutes, as it was likely not an actual ride.  

Lastly I extracted the days of the week (categorizing it into weekday and weekend) and months from the started_at series so I could use it later for analysis.

2. Analyzing the Data
I initiated the analysis by finding the ratio of rides that were from members vs. casual riders. In the year of 2023 approximately 63% of rides were made by members and 37% from casual riders.

I looked at multiple variables to identify how these two groups differed in the way they used Divvy's bikes. Casual riders on average have longer ride times (24 minutes) compared to members (14 minutes). Additionally casual riders' most popular days of the week to ride are on Friday, Saturday, and Sunday, whereas members ride the most on Tuesday through Thursday and the least on the weekends. Riding patterns are quite similar for both groups across the months, with the summer months being the most popular to ride in. Divvy offers two types of bikes to its customers: electric and classic. While both casual and members both use classic bikes the most, electric bikes are the most poular with casual riders. 

3. Data Visualization
I created the graphs for this project using tableau libraries Seaborn and Matplot. The graphs are attached as separate files in this repository.

4. Analysis and Conclusions
