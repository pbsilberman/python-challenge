import os
import csv

# Pull in the csv
csvpath = os.path.join("PyBank", "budget_data_1.csv")

with open(csvpath, newline='') as csvfile:
    # Skip the first line because it contains the headers.
    next(csvfile)

    csvreader = csv.reader(csvfile, delimiter=',')

    # Initialize all the variables for tracking
    counter = 0
    revenue = []
    months = []
    revChange = []


    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))
    
    # create a list for change in revenue
    for i in range(len(revenue)-1):
        thismonth = revenue[i]
        nextmonth = revenue[i+1]
        revChange.append(nextmonth-thismonth)

    totalRevenue = sum(revenue)

    maxDecrease = min(revChange)
    maxDecIndex = revChange.index(maxDecrease)
    maxDecMonth = months[maxDecIndex + 1]   # have to add one since the revchange list is one month ahead

    maxIncrease = max(revChange)
    maxIncIndex = revChange.index(maxIncrease)
    maxIncMonth = months[maxIncIndex]   # have to add one since the revchange list is one month ahead

    avgChange = round(sum(revChange)/float(len(revChange)), 0)
        


print("Financial Analysis")
print("-" * 20)
print(f'Total Months: {len(months)}')
print(f'Total Revenue: ${totalRevenue}')
print(f'Average Revenue Change: ${avgChange}')
print(f'Greatest Increase in Revenue: {maxIncMonth} (${maxIncrease})')
print(f'Greatest Decrease in Revenue: {maxDecMonth} (${maxDecrease})')