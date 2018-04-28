import os
import csv

# Pull in the csv
csvpath = os.path.join("PyBank", "budget_data_1.csv")

with open(csvpath, newline='') as csvfile:
    # Skip the first line because it contains the headers.
    next(csvfile)

    csvreader = csv.reader(csvfile, delimiter=',')

    totalRevenue = 0

    for row in csvreader:
        totalRevenue = totalRevenue + int(row[1])

print(f'Total Revenue: ${totalRevenue}')