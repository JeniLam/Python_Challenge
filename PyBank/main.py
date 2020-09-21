import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('Resources', 'budget_data.csv')
#declare variable first
totalmonths = 0
totalPL = 0
date = []
profitloss = []
greatestincrease = 0
greatestdecrease = 0

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
        # turn date and pl column into list
        date.append(row[0])
        profitloss.append(row[1])
        # zip appended lists together to create tuple to perform max/min features on
        # research on these sites:https://stackoverflow.com/questions/7313157/python-create-list-of-tuples-from-lists/7313188
        # https://www.tutorialspoint.com/python/tuple_max.htm#:~:text=Python%20tuple%20method%20max%20%28%29%20returns%20the,elements%20from%20the%20tuple%20with%20maximum%20value.    
        ziplist = list(zip(date,profitloss))
        #counter for number of lines
        totalmonths += 1
        # how to sum csv column in python https://stackoverflow.com/questions/13517080/sum-a-csv-column-in-python
        totalPL += (int(row[1]))
    #got help from Wei on this equation below
    avgpl = (int(profitloss[0])- int(profitloss[85]))/85
    # print(ziplist) not producing correct date/value??
    greatestincrease = max(ziplist)
    greatestdecrease = min(ziplist)
       
    print("Total Months: " + str(totalmonths))    
    print('Total Net Profit/Losses: $' + str(totalPL))
    print("Average Change: $"+ str(avgpl))
    print("Greatest Increase in Profits: " + str(greatestincrease))
    print("Greatest Decrease in Profits: "+ str(greatestdecrease))

#write above to text file
PyBank = output_path = os.path.join("analysis", "PyBank.txt")
#\n creates new line https://www.geeksforgeeks.org/reading-writing-text-files-python/#:~:text=Reading%20and%20Writing%20to%20text%20files%20in%20Python.,over-written.%20The%20handle%20is%20positioned%20...%20More%20items 
with open(PyBank,'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % totalmonths)
    file.write("Total Net Profit/Losses: $ %d\n" % totalPL)
    file.write("Average Change: %d\n" % avgpl)
    file.write("Greatest Increase in Profits:  %s ($%d)\n" % greatestincrease[0], greatestincrease[1])
    file.write("Greatest Decrease in Profits:  %s ($%d)\n" % greatestdecrease[0], greatestdecrease[1])
   







