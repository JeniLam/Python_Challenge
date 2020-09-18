import os
import csv
# Path to collect data from the Resources folder
election_data = os.path.join('Resources', 'election_data.csv')
# open file and read, store contents as text
with open(election_data, 'r') as text:
    #store reference to file 
    print(text)

    #store text in variable called bank
    poll_data = text.read()
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
print("Election Results")
print("---------------------------")
print("Total Votes: ")
print("---------------------------")
#candidate dictionary or list goes here
print("---------------------------")
print("Winner: ")
print("---------------------------")