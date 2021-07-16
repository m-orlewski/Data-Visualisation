import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)
	dates, prpc = [], []

	for row in reader:
		date = datetime.strptime(row[2], '%Y-%m-%d')
		rain = float(row[3])
		dates.append(date)
		prpc.append(rain)

plt.style.use('seaborn')
fig, ax = plt.subplots()

plt.title('Daily rainfall in Sitka 2018', fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Rainfall', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

ax.plot(dates, prpc)
plt.show()




	