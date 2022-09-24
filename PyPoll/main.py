# import modules
import os
import csv

# create vars

# voter count
voter_count = 0
# create file path
csvpath = os.path.join('Resources','election_data.csv')

# create candidates list
candidates = []
pct_vote = []
count = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip first line
    next(csvreader)

    # loop through rows
    for row in csvreader:

        #add to row count for each month
        voter_count += 1

        # add new candidates to candidates list
        if row[2] not in candidates:
            candidates.append(row[2])

        
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 

    # set vote count list len equal to candidates len 
    count = [0] * len(candidates)   

    # loop through rows of voter data
    for row in csvreader:
        # loop through candidates
        for candidate in candidates:
            # check if candidate in row matches the candidate in list
            if row[2] == candidate:
                count[candidates.index(candidate)] += 1

for candidate in candidates:
    pct_vote.append((count[candidates.index(candidate)]/voter_count))

highest_count = 0
for i in count:
    if  i > highest_count:
        highest_count = i
        winner = candidates[count.index(i)]

print("Election Results")
print("-------------------------")
print(f"Total Votes: {voter_count}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {round((pct_vote[candidates.index(candidate)])*100,3)}% ({count[candidates.index(candidate)]})")
print("-------------------------")
print(f"Winner: {winner}")    
print("-------------------------")
