import csv;
import matplotlib.pyplot as plt;
dates = []
close = []
with open('stock_market_dataset.csv') as file:
    csvFile = csv.reader(file)
    count = 0
    for lines in csvFile:
        if count > 0:
            dates.append(lines[0])
            close.append(lines[4])
        count = count + 1
fig, ax = plt.subplots()
ax.bar(dates, close)
ax.set_xlabel('Date')
ax.set_ylabel('Price')
plt.show()
