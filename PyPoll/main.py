import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join('Resources', 'election_data.csv')

# dictionary to store candidate and vote data 
candidates = {}
totalvotes = 0
winner = 0
# open file and read, store contents as text
with open(election_data) as csvfile:
    #store reference to file 
    csvreader = csv.reader(csvfile, delimiter=',')
     # skip the header row
    header = next(csvreader)
    print(csvreader)

    
    # counted number of lines in dataset minuus the header
    for row in csvreader:
        # iterate through csv and create dictionary containing unique candidate names and their total votes
        # name is Key, row 2 says which row index we want to iterate through
        name = row[2]
        # https://www.w3schools.com/python/python_dictionaries.asp had the tutor help me with this portion
        if name in candidates:
            candidates[name] = candidates[name] +1
        else:
            candidates[name] = 1
        # The total number of votes cast taken from pyBank portion of homework
        totalvotes +=1
    #Begin print output
    # print(candidates)
    print("Election Results")
    print("---------------------------")
    print("Total Votes: " + str(totalvotes))
    print("---------------------------")

    # loop through dictionary to gather candidate and vote information, use formula within iteration to get percentage. https://tutorialdeep.com/knowhow/loop-through-dictionary-elements-python/#Print_Both_Keys_and_Values_of_Python_Dictionaries
    # get to 3 decimal places - https://www.codespeedy.com/print-floats-to-a-specific-number-of-decimal-points-in-python/
    for candidate, vote in candidates.items():
        print(f"{candidate}: {vote/totalvotes*100:.3f}% ({vote})")         
    print("---------------------------")

    # The winner of the election based on popular vote.


PyPoll = output_path = os.path.join("Analysis", "PyPoll.txt")

with open(PyPoll,'w') as file:
    file.write("Election Results\n")
    file.write("---------------------\n")
    file.write(f"Total Votes:  {totalvotes}\n")
    file.write("---------------------\n")
    for candidate, vote in candidates.items():
        file.write(f"{candidate}: {vote/totalvotes*100:.3f}% ({vote})\n") 
    file.write("---------------------\n")