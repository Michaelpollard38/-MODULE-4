import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Open the CSV file
filename = 'sitka_weather_2014.csv'

# Lists to store dates and high temperatures
dates = []
highs = []

# Reading the CSV file and extracting data
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  

    for row in reader:
        # Extracting date and high temperature
        date = datetime.strptime(row[0], "%Y-%m-%d")
        high_temp = int(row[1])

        # Appending to the lists
        dates.append(date)
        highs.append(high_temp)

# Plotting the data
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(dates, highs, c='red', label='High Temperature')

# Formatting the plot
ax.set_title('Daily High Temperatures - Sitka, Alaska (2014)', fontsize=18)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Temperature (F)', fontsize=12)
ax.legend()
fig.autofmt_xdate() 
# Show the plot
plt.show()
