# import modules
import os
import csv

# create vars

# voter count
voter_count = 0
# create file path
csvpath = os.path.join('Resources','election_data.csv')

# create candidates lists
candidates = []
pct_vote = []
count = []

# iterate through the list to get total vote count and all candidates
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

# iterate through list again to get vote count by candidate
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
                # if it matches, add to that candidates relative value in the vote list
                count[candidates.index(candidate)] += 1

# calculate each candidates percentage of the vote and then add to their relative index in the pct vote list
for candidate in candidates:
    pct_vote.append((count[candidates.index(candidate)]/voter_count))

# check for winner
# declare var for comparison
highest_count = 0

# loop through count list to check for the highest value
for i in count:
    # check if candidates vote is the highest
    if  i > highest_count:
        # if highest, set it as the new benchmark
        highest_count = i
        # and set 'winner' equal to that vote count's candidate
        winner = candidates[count.index(i)]

# print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {voter_count}")
print("-------------------------")
# loop through the candidates list and prints their relative index
for candidate in candidates:
    print(f"{candidate}: {round((pct_vote[candidates.index(candidate)])*100,3)}% ({count[candidates.index(candidate)]})")
print("-------------------------")
print(f"Winner: {winner}")    
print("-------------------------")

# write txt file - use \n to write to a new line
with open('Election_Results.txt', 'w') as election_results:
    election_results.write("Election Results\n")
    election_results.write("-------------------------\n")
    election_results.write(f"Total Votes: {voter_count}\n")
    election_results.write("-------------------------\n")
    # loop through the candidates list and prints their relative index
    for candidate in candidates:
        election_results.write(f"{candidate}: {round((pct_vote[candidates.index(candidate)])*100,3)}% ({count[candidates.index(candidate)]})\n")
    election_results.write("-------------------------\n")
    election_results.write(f"Winner: {winner}\n")    
    election_results.write("-------------------------\n")