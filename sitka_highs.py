import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename, 'r') as f:
	reader = csv.reader(f)
	header_row = next(reader)

	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[5])
		low = int(row[6])
		dates.append(current_date)
		highs.append(high)
		lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', linewidth=1)
ax.plot(dates, lows, c='blue', linewidth=1)

# fill space between 2 y-values (highs and lows)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily high temperatures, 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() #draws date labels diagonally
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.ylim([0, 120])

plt.show()