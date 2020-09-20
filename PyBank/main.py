import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('Resources', 'budget_data.csv')
#declare variable first
totalPL = []
avgpl = 0
greatestincrease = []
greatestdecrease= []

# open file and read, store contents as text
with open(budget_data) as csvfile:
    #store reference to file and set comma to indicate new row
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip the header row
    header = next(csvreader)
    print(csvreader)

    #Begin output
    print("Financial Analysis")
    print("---------------------------")

    # The total number of months included in the dataset
    # counted number of lines in dataset minuus the header
    totalmonths= len(list(csvreader))
    print("Total Months: " + str(totalmonths))

    # The net total amount of "Profit/Losses" over the entire period       
    for row in csvreader:
        totalPL = totalPL + (int(row['Profit/Losses]']))
        
    print('Total: $' + str(totalPL))
    # The average of the changes in "Profit/Losses" over the entire period
    avgpl = int(totalPL/totalmonths)   
    print("Average Change: $"+ str(avgpl))
    # The greatest increase in profits (date and amount) over the entire period
    #need Max
    print("Greatest Increase in Profits: ")
    # The greatest decrease in losses (date and amount) over the entire period
    #need Min
    print("Greatest Decrease in Profits: ")

#write above to text file
PyBank = output_path = os.path.join("analysis", "PyBank.txt")
#\n creates new line
with open(PyBank,'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % totalmonths)
    file.write("Total Profit/Losses: %d\n" % totalPL)
    file.write("Average Change: %d\n" % avgpl)
    # file.write("Greatest Increase in Profits: %s(%s)\n" % greatestincrease[0],greatestincrease[1])
    # file.write("Greatest Decrease in Profits: %s(%s)\n" % greatestdecrease[0],greatestdecrease[1])
   







