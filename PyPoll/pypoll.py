# import modules for OS paths and CSV reading
import os
import csv

# Strategy: read line by line, add votes to a dictionary.
# Dynamically add candidates, since we might not know how many candidates will be on the ballot

# Initialize the voting dictionary globally, since we need to write it to a file later
candidates = {}

# define the csv path, it lives in the PyPoll folder in the workspace
csvpath = os.path.join("PyPoll", "election_data_2.csv")

# open the csv and start reading in the data
with open(csvpath, newline='') as csvfile:

    # Skip the first line because it contains the headers.
    next(csvfile)

    # create the reader object to iterate through
    csvreader = csv.reader(csvfile, delimiter=',')


    # Loop through the rows of the csv
    for row in csvreader:
        # Pull the candidate name for the row
        candidate = row[2]

        # If there are no votes for the candidate, add to the dictionary with 1 vote
        if candidate not in candidates:
            candidates[candidate] = 1
        # Else increment the votes by 1    
        else:
            numvotes = 1 + candidates[candidate]
            candidates[candidate] = numvotes
        
    # Loop through candidates dictionary to get total number of votes
    # Additionally, add a dummy variable to compute the winner from the maximum number of votes
    totalVotes = 0
    maxVotes = 0

    for person in candidates:
        totalVotes += candidates[person]
        if candidates[person] > maxVotes:
            winner = person
            maxVotes = candidates[person]

    # Print the results
    print("Election Results")
    print("-" * 25)
    print(f'Total Votes: {totalVotes}')
    print("-" * 25)
    # Use a loop since we're printing data on each element in the candidate dictionary
    for candidate in candidates:
        print(f'{candidate}: {round(100*candidates[candidate]/totalVotes,1)}% ({candidates[candidate]})')
    print("-" * 25)
    print(f'Winner: {winner}')
    print("-" * 25)

# Define the file name for printing the election results
output_file = os.path.join('PyPoll','election_results.txt')

# Open the document so we can write to it
with open(output_file, "w", newline='') as datafile:

    # Write the results to the txt file
    print("Election Results", file = datafile)
    print("-" * 25, file = datafile)
    print(f'Total Votes: {totalVotes}', file = datafile)
    print("-" * 25, file = datafile)
    # Use a loop since we're writing data on each element in the candidate dictionary
    for candidate in candidates:
        print(f'{candidate}: {round(100*candidates[candidate]/totalVotes,1)}% ({candidates[candidate]})', file = datafile)
    print("-" * 25, file = datafile)
    print(f'Winner: {winner}', file = datafile)
    print("-" * 25, file = datafile)