import csv;
with open('stock_market_dataset.csv') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)

