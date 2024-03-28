
This project is part of my Google Data Analytics Certificate. The project features data from Divvy Bikes, a bike-sharing company, and aims to understand the distinction between the company's casual riders (those without an annual membership) and members (those who have an annual membership). The objective is to leverage these insights to create a successful marketing strategy to convert casual riders into members.

I utilized Python to prepare, clean, analyze, and visualize the data.

Data Cleaning:

Initially, the data contained many entries with null values. The series with null values were station names, station IDs, latitude, and longitude. At first, I tried to use other rows with similar latitudes and longitudes to match them with rows missing station names and IDs. However, since the coordinates are rounded to differing degrees of accuracy, and coordinates need to be rounded to at least four decimal places to distinguish one station from another, I could not proceed. Without more information provided, I had to drop all nulls from the dataset for it to be usable. Because the dataset is so large compared to the number of null rows, deleting the null entries did not have significant impact on data integrity. 

Cleaning the data also involved removing entries not representative of actual trips. I removed trips which were less than 60 seconds or greater than 24 hours, as well as those for testing/service purposes. Additionally, I removed trips beginning and ending in the same station which were shorter than five minutes, as they were likely not actual rides.

Lastly, I extracted the days of the week (categorizing it into weekday and weekend) and months from the started_at series so I could use it later for analysis.

Data Analysis:

I initiated the analysis by finding the ratio of rides that were from members vs. casual riders. In the year of 2023, approximately 63% of rides were made by members, while 37% were by casual riders.

I looked at multiple variables to identify how these two groups differed in the way they used Divvy's bikes. Casual riders, on average, have longer ride times (24 minutes) compared to members (14 minutes). Moreover, casual riders favor riding on Fridays, Saturdays, and Sundays, whereas members ride the most Tuesday through Thursday. Riding patterns are quite similar for both groups across the months, with the summer months being the peak riding season. Additionally, Divvy offers two types of bikes to its customers: electric and classic. While both casual and members both use classic bikes the most, electric bikes are the most popular with casual riders.

Data Visualization:

I created the graphs for this project using tableau libraries Seaborn and Matplotlib. The graphs are attached as separate files in this repository.

Conclusions:

Based on these insights, I propose several marketing strategies for Divvy to enhance conversion rates from casual riders to yearly members.
Firstly, is to focus advertising efforts in the summer months, given it's the season when most casual riders are using Divvy's services. Secondly, Divvy should consider introducing a new yearly membership designed specifically for those riding on weekends. These memberships would be cheaper than regular memberships by providing users with limited rides during weekdays and unlimited rides during the weekend. This approach capitalizes on locking casual riders into yearly contracts while aligning with their usage patterns to provide cheaper membership fees.
Most casual riders aren't riding during the week so capping the number of weekday rides would not interfere greatly with Divvy's current weekday demand. Another option would be to create seasonal memberships, targeted towards casual riders who only ride in a specific season, so an annual membership would not be good value for their money. These customers would never sign up for an annual membership, but a seasonal membership would be a more attractive offer. These memberships could be especially profitable if they automatically renewed every season. Auto-renewal would prolong customer retention resulting in increased profitability.

To conclude, the findings from this analysis provide valuable insights for Divvy Bikes to refine their marketing strategies. By understanding the distinct behaviors and preferences of casual riders and members, Divvy can tailor its memberships to better cater to to its customers, thereby increasing profitability. 




