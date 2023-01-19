import csv
import os
file_to_load = os.path.join("Resources", "budget_data.csv")
months_total = 0
pandl = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)
    first_row = next(reader)
    months_total += 1
    pandl += int(first_row[1])
    prev_net = int(first_row[1])
    
    for row in reader:
        months_total += 1
        pandl += int(row[1])
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

net_average = sum(net_change_list) / len(net_change_list)

output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months_total}\n"
    f"Total: ${pandl}\n"
    f"Average Change: {net_average:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
print(output)
