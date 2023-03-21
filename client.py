from entry import Entry;
from typing import List;
import csv;
import matplotlib.pyplot as plt;
entries = []
with open('stock_market_dataset.csv') as file:
    csvFile = csv.reader(file)
    count = 0
    for lines in csvFile:
        if count > 0:
            temp = lines[4][1:-1]
            entries.append(Entry(lines[0], float(temp)))
        count = count + 1
fig, ax = plt.subplots()
def get_dates(entry_list: List[Entry]):
    dates = []
    for element in entry_list:
        dates.append(element.__get_date())
    return dates

def get_closes(entry_list: List[Entry]) -> List[float]:
    closes: List[float] = []
    for element in entry_list:
        closes.append(element.__get_close())
    return closes

ax.bar(get_dates(entries), get_closes(entries))
ax.set_xlabel('Date')
ax.set_ylabel('Price')
plt.show()
def get_close_difference(entry1: Entry, entry2: Entry):
    return entry2.__get_close() - entry1.__get_close()