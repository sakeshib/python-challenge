import os
import csv

# Path to CSV file
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Creating lists to store data
months = []
dates = []
pro_loss = []
profit_loss_change = []

# Set variables to 0 for formula
total_months = 0
total_profit_loss = 0
greatest_increase = 0
greatest_decrease = 9999999999999

# Open CSV file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Read header row
    next(csvreader)

    # Variable to store first row of data
    first_row = next(csvreader)
    total_months += 1
    total_profit_loss += int(first_row[1])
    prev_net = int(first_row[1])

    # Read each row after header
    for row in csvreader:

        # Split date into months and dates
        split_date = row[0].split("-")
        months.append(split_date[0])
        dates.append(split_date[1])

        # Total number of months included in dataset
        total_months += 1
        # print(total_months)

        # Net total amount of profit and losses
        profit_loss = int(row[1])
        total_profit_loss += profit_loss
        # print(total_profit_loss)

        # Changes in profit and loss
        net_change = profit_loss - prev_net
        prev_net = profit_loss
        profit_loss_change.append(net_change)

        # Track the months per greatest increase and decrease
        if net_change > greatest_increase:
            greatest_increase = net_change
            inc_month = row[0]

        if net_change < greatest_decrease:
            greatest_decrease = net_change
            dec_month = row[0]

    # Calculate the average
    average_change = sum(profit_loss_change) / len(profit_loss_change)
    #print(average_change)

    # Calculate greatest increase in profits
    max_change = max(profit_loss_change)
    # print(max_change)
 
    # Calculate greatest decrease in profits
    min_change = min(profit_loss_change)
    # print(min_change)

# Print results
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit_loss}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {inc_month} (${max_change})')
print(f'Greatest Decrease in Profits: {dec_month} (${min_change})')    

# File path and write data as text file
analysis_path = os.path.join('Analysis', 'PyBank.text')
with open(analysis_path, 'w') as file:
    file.write('Financial Analysis\n')
    file.write('----------------------------\n')
    file.write(f'Total Months: {total_months}\n')
    file.write(f'Total: ${total_profit_loss}\n')
    file.write(f'Average Change: ${average_change:.2f}\n')
    file.write(f'Greatest Increase in Profits: {inc_month} (${max_change})\n')
    file.write(f'Greatest Decrease in Profits: {dec_month} (${min_change})\n')    




