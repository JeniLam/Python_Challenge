import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('Resources', 'budget_data.csv')

# open file and read, store contents as text
with open(budget_data) as csvfile:
    #store reference to file 
    csvreader = csv.reader(csvfile, delimiter=',')

    #store text in variable called bank
    bank = (csvreader)
    print(bank)
    #Begin output
    print("Financial Analysis")
    print("---------------------------")
    # The total number of months included in the dataset
    # counted number of lines in dataset minuus the header
    Totalmonths= len(list(bank))-1
    print("Total Months: " + str(Totalmonths))
        


# net_amount = 0
# average_change = 0
# greatest_increase = 0
# greatest_decrease = 0




# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period



print("Total: ")
print("Average Change: ")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")