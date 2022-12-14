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

# prior value
prior_value = 0

#create list to hold differences between rows
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

        #calc diff between prior row's value and current row's value
        diff = int(row[1]) - prior_value

        # check if greatest increase
        if diff > increase:
            # if yes, set new greatest increae
            increase = diff
            # and record date
            inc_date = row[0]
         # check if greatest decrease
        if diff < decrease:
            # if yes, set new greatest increae
            decrease = diff
             # and record date
            dec_date = row[0]

        #add differences between rows to differences' list
        diffs.append(diff)

        # set new prior value
        prior_value = int(row[1])
    
    # calc avg, start from second item to omit first row
    average = sum(diffs[1:]) / len(diffs[1:])

# print results
print(f"""Financial Analysis
----------------------------
Total Months: {month_count}
Total: ${total_profit}
Average Change: ${round(average, 2)}
Greatest Increase in Profits: {inc_date} (${increase})
Greatest Decrease in Profits: {dec_date} (${decrease})""")

# write to new text file
with open('Financial_Analysis.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("-------------------------\n")
    f.write(f"Total Months: {month_count}\n")
    f.write(f"Total: ${total_profit}\n")    
    f.write(f"Average Change: ${round(average, 2)}\n")
    f.write(f"Greatest Increase in Profits: {inc_date} (${increase})\n")
    f.write(f"Greatest Decrease in Profits: {dec_date} (${decrease})\n")