import os
import csv

csvpath = os.path.join("Instructions", "PyBank", "Resources", "budget_data.csv")

# Open the CSV
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    row_count = 0

    print ("Financial Analysis")
    print (f'Total months : {row_count}')

    sum_profit = 0
    sum_loss = 0
    totalpl = 0
    profit = 0

    for row in csvreader:
        row_count += 1
        profit = int(row[1])
        print (profit)
        if profit > 0:
            sum_profit = sum_profit + profit
        else:
            sum_loss = sum_loss + profit
    totalpl = sum_profit - sum_loss
    print (f"total : {totalpl}")

