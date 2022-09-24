# import modules
import os
import csv

# create file path
csvpath = os.path.join('Resources','budget_data.csv')

#establish vars

#month count
month_count = 0

#total profit
total_profit = 0

# greatest increase
increase = 0

#greatest decrease
decrease = 0

prior_value = 0
#establish emtpy lists
diffs = []

# use csv mod to read the file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip first line
    next(csvreader)

    # loop through rows
    for row in csvreader:

        #add to row count for each month
        month_count += 1

        #sum profits
        total_profit +=int(row[1])
        diff = int(row[1]) - prior_value
        if diff > increase:
            increase = diff
            inc_date = row[0]
        if diff < decrease:
            decrease = diff
            dec_date = row[0]
        diffs.append(diff)
        prior_value = int(row[1])
    average = sum(diffs[1:]) / len(diffs[1:])

# print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${round(average, 2)}")
print(f"Greatest Increase in Profits: {inc_date} (${increase})")
print(f"Greatest Decrease in Profits: {dec_date} (${decrease})")