# import modules for OS paths and CSV reading
import os
import csv

# define the csv path, it lives in the PyPoll folder in the workspace
csvpath = os.path.join("PyPoll", "election_data_1.csv")

# open the csv and start reading in the data
with open(csvpath, newline='') as csvfile:

    # Strategy: read line by line, add votes to a dictionary.
    # Dynamically add candidates, since we might not know how many candidates will be on the ballot

    # Skip the first line because it contains the headers.
    next(csvfile)

    # create the reader object to iterate through
    csvreader = csv.reader(csvfile, delimiter=',')

    # Initialize the voting dictionary
    candidates = {}

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
    for candidate in candidates:
        print(f'{candidate}: {round(100*candidates[candidate]/totalVotes,1)}% ({candidates[candidate]})')
    print("-" * 25)
    print(f'Winner: {winner}')
    print("-" * 25)