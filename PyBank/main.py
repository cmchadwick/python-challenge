import os
import csv

budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

total_months = 0
total_profit_losses = 0
change_profit_losses = 0
list_profit_losses = []
prev_profit_losses_row = 0
avg_change_profit_losses = 0

with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)


    
    for row in csvreader:   

        total_months = total_months + 1

        total_profit_losses = total_profit_losses + int(row[1])

        change_profit_losses = int(row[1]) - prev_profit_losses_row
        prev_profit_losses_row = int(row[1])

        list_profit_losses.append(change_profit_losses)
    
    avg_change_profit_losses = sum(list_profit_losses) / len(list_profit_losses)

greatest_increase = max(change_profit_losses)
greatest_decrease = min(change_profit_losses)


print("Financial Analysis")
print("------------------------")
print("Total Months: {total_months}")
print("Total Profit/Losses: ${total_profit_losses}")
print("Average Change: ${avg_change_profit_losses}")
print("Greatest Increase: ${greatest_increase}")
print("Greatest Decrease: ${greatest_decrease}")


with open("analysis.txt") as file:
    print("Financial Analysis")
    print("------------------------")
    print("Total Months: {total_months}")
    print("Total Profit/Losses: ${total_profit_losses}")
    print("Average Change: ${avg_change_profit_losses}")
    print("Greatest Increase: ${greatest_increase}")
    print("Greatest Decrease: ${greatest_decrease}")

