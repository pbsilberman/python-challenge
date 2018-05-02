# Import the necessary modules
import os
import csv

# Designate the CSV file path
csvpath = os.path.join("PyBank", "budget_data_2.csv")

# Start reading in the CSV
with open(csvpath, newline='') as csvfile:
    # Skip the first line because it contains the headers, then define our reader
    next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=',')

    # Initialize all the variables for tracking
    # Strategy: store the revenue and months in lists, since we need to know change from month-to-month
    # Then we can easily perform the necessary computation using these lists
    revenue = []
    months = []
    revChange = []

    # Read in the data line by line from the CSV to fill our lists
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))
    
    # Using the revenue list, calculate the month to month revenue change
    # note that we do this one less than the length of our CSV
    for i in range(len(revenue)-1):
        rev_change = revenue[i+1] - revenue[i]
        revChange.append(rev_change)

    # We can easily calculate the total revenue by summing over the revenue list
    totalRevenue = sum(revenue)

    # We can grab the largest decrease easily from the revChange list
    # Then we grab the index from that list in order to find the corresponding month
    # We have to add one since the revchange list is one month ahead
    maxDecrease = min(revChange)
    maxDecIndex = revChange.index(maxDecrease)
    maxDecMonth = months[maxDecIndex + 1]   

    # Similarly, we grab the largest increase, as above
    maxIncrease = max(revChange)
    maxIncIndex = revChange.index(maxIncrease)
    maxIncMonth = months[maxIncIndex + 1]

    # Compute the average change over the revChange list
    avgChange = int(sum(revChange)/float(len(revChange)))

# Print the results to the terminal        
print("Financial Analysis")
print("-" * 25)
print(f'Total Months: {len(months)}')
print(f'Total Revenue: ${totalRevenue}')
print(f'Average Revenue Change: ${avgChange}')
print(f'Greatest Increase in Revenue: {maxIncMonth} (${maxIncrease})')
print(f'Greatest Decrease in Revenue: {maxDecMonth} (${maxDecrease})')

# Define the output file path for the results
output_file = os.path.join('PyBank','financial_analysis.txt')

# Open the output file
with open(output_file, "w", newline='') as datafile:

    # Write the results to the file
    print("Financial Analysis", file = datafile)
    print("-" * 25, file = datafile)
    print(f'Total Months: {len(months)}', file = datafile)
    print(f'Total Revenue: ${totalRevenue}', file = datafile)
    print(f'Average Revenue Change: ${avgChange}', file = datafile)
    print(f'Greatest Increase in Revenue: {maxIncMonth} (${maxIncrease})', file = datafile)
    print(f'Greatest Decrease in Revenue: {maxDecMonth} (${maxDecrease})', file = datafile)
