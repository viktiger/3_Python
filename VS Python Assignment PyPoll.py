# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("PyPoll", "election_data.csv")
# print(csvpath)

# Set variable to check if we found the file
found = False

# Open the CSV and read to contents
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    # Total vote counts
    count = 0 
    # Total votes
    total = 0 
    # Total candidates in election
    candidates = []
    # Total votes per candidate in election
    votes = []
    # Total votes percentage per candidate in election
    votes_percentage = []

    for row in csvreader:
        # print (row) # Testing data is printing 
        # print (row[1]) # Testing data is printing amounts
        # print (int(row[1])) # Converting amounts into integers from strings

        count = count +1

        if row[2] not in candidates:
            candidates.append(row[2])
            candidates_index = candidates.index(row[2])
            votes.append(1)
        else:
            candidates_index = candidates.index(row[2])
            votes[candidates_index] += 1

    # Calculating & formatting the votes percentage 
    for votes_total in votes:
        percentage = (votes_total/count) * 100
        
        format_percentage = "{:.3%}".format(percentage/100)
        votes_percentage.append(format_percentage)
    
    # Election winner has the maximum number of votes
    winner = max(votes)
    winner_index = votes.index(winner)
    winning_candidate = candidates[winner_index]

    # Poll summary
    print("--------------------")
    print("Election Results")
    print("--------------------")
    # Total votes
    print("Total Votes: ", count)
    print("--------------------")
    # Poll results
    print(candidates[0],votes_percentage[0],votes[0])
    print(candidates[1],votes_percentage[1],votes[1])
    print(candidates[2],votes_percentage[2],votes[2])
    # Poll winner
    print("--------------------")
    print(winning_candidate)
    print("--------------------")

# Exporting a text file
output = open("output_pypoll.txt", "w")

line1 = "--------------------"
line2 = "Election Results"
line3 = "--------------------"
line4 = str(f"Total Votes: {str(count)}")
line5 = "--------------------"
line6 = str(f"{candidates[0],votes_percentage[0],votes[0]}")
line7 = str(f"{candidates[1],votes_percentage[1],votes[1]}")
line8 = str(f"{candidates[2],votes_percentage[2],votes[2]}")
line9 = "--------------------"
line10 = str(f"Winner: {winning_candidate}")
line11 = "--------------------"

output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4,line5,line6,line7,line8,line9,line10,line11))