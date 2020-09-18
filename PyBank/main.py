import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('Resources', 'budget_data.csv')

# open file and read, store contents as text
with open(budget_data, 'r') as text:
    #store reference to file 
    print(text)

    #store text in variable called bank
    bank = text.read()




# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
#The below will be commented out until I figure out the above
print("Financial Analysis")
print("---------------------------")
print("Total Months: ") 
print("Total: ")
print("Average Change: ")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")