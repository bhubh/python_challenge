#PyBank Python challenge
#importing os and csv modules
import os
import csv

#give csv path 
csvpath = os.path.join('Resources','election_data.csv')

# creating empty lists to store data

Ballot_ID = []
County = []
Candidate = []



#Reading CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Read csv header row first
    csv_header = next(csvreader)
    
    #Reading each row and adding to the lists
    for row in csvreader:
        Ballot_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])



#to calculate total number of votes
Total_votes = len(Ballot_ID)
print(f"Total Votes:  {Total_votes}")

#defining election results as dictionary with candidates as key
Election_results = {}

#using for loop to count the votes
for vote in Candidate:
    if vote in Election_results.keys():
        Election_results[vote] = 1+ Election_results[vote]
    else:
        Election_results[vote] = 1


#calculating percentage of votes obtained



# printing total votes count for each candidate
   
for key in Election_results.keys():
    Percentage_vote = 100*Election_results[key]/Total_votes
    Percentage_vote = round(Percentage_vote,2)
    print(f"{key}:{Election_results[key]} ({Percentage_vote}%)")