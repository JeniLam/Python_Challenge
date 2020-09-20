import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('Resources', 'budget_data.csv')
#declare variable first
totalmonths = 0
totalPL = 0
avgpl = 0
greatestincrease = []
greatestdecrease = []

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
    # totalmonths= len(list(csvreader)) placing this first read through CSV and stopped. need to treat all like a list and do all before getting out
    # The net total amount of "Profit/Losses" over the entire period      
    # The average of the changes in "Profit/Losses" over the entire period
    for row in csvreader:
        #counter for number of lines
        totalmonths +=1
        totalPL += (int(row[1]))
        avgpl = int(totalPL/totalmonths)
        # list comprehension?
        greatestincrease = (float(max(row[0,1])))
        greatestdecrease = (float(min(row[0,1])))
    print("Total Months: " + str(totalmonths))    
    print('Total: $' + str(totalPL))
    print("Average Change: $"+ str(avgpl))
    # The greatest increase in profits (date and amount) over the entire period
    print("Greatest Increase in Profits: " + greatestincrease)
    # The greatest decrease in losses (date and amount) over the entire period
    #need Min
    print("Greatest Decrease in Profits: "+ greatestdecrease)

#write above to text file
PyBank = output_path = os.path.join("analysis", "PyBank.txt")
#\n creates new line
with open(PyBank,'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % totalmonths)
    file.write("Total Profit/Losses: %d\n" % totalPL)
    file.write("Average Change: %d\n" % avgpl)
    file.write("Greatest Increase in Profits: %s(%s)\n" % greatestincrease[0],greatestincrease[1])
    file.write("Greatest Decrease in Profits: %s(%s)\n" % greatestdecrease[0],greatestdecrease[1])
   







