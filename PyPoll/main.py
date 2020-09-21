import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join('Resources', 'election_data.csv')

#Begin print output
print("Election Results")
print("---------------------------")
#define function for percentages and accept candidate_data as sole parameter

def percentages(candidate_data):
    #delare variables in candidate_data
    votes = int(candidate_data[0])
    candidates = str(candidate_data[2])
   
    
    
winner = 0
totalvotes = 0
# open file and read, store contents as text
with open(election_data) as csvfile:
    #store reference to file 
    csvreader = csv.reader(csvfile, delimiter=',')
     # skip the header row
    header = next(csvreader)
    print(csvreader)

    # The total number of votes cast
    # counted number of lines in dataset minuus the header
    for row in csvreader:
        totalvotes +=1

    print("Total Votes: " + str(totalvotes))
    print("---------------------------")
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote.


# print("---------------------------")
# #candidate dictionary or list goes here
# print("---------------------------")
# print("Winner: ")
# print("---------------------------")

PyPoll = output_path = os.path.join("Analysis", "PyPoll.txt")

with open(PyPoll,'w') as file:
    file.write("Election Results\n")
    file.write("---------------------\n")
    file.write("Total Votes: %d\n" % totalvotes)
    file.write("---------------------\n")