import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join('Resources', 'election_data.csv')


# open file and read, store contents as text
with open(election_data) as csvfile:
    #store reference to file 
    csvreader = csv.reader(csvfile, delimiter=',')
     # skip the header row
    header = next(csvreader)

    #store text in variable called poll data
    poll_data = (csvreader)
    print(poll_data)

    #Begin output
    print("Election Results")
    print("---------------------------")

    # The total number of votes cast
    # counted number of lines in dataset minuus the header
    total_votes = len(list(poll_data))-1
    print("Total Votes: " + str(total_votes))
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.


print("---------------------------")
#candidate dictionary or list goes here
print("---------------------------")
print("Winner: ")
print("---------------------------")