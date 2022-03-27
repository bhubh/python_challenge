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

#giving path for text print to file
path = os.path.join("PyPoll.txt")
with open(path, "w+") as file:

    message1 = "Election Results"
    file.write(f"{message1}\n")
    print("message1")
    print("--------------------------------------")
    message2 = f"Total Votes:  {Total_votes}"
    print(message2)
    file.write(f"{message2}\n")
    print("--------------------------------------")
    
    #calculating percentage votes and printing results
    for key in Election_results.keys():
        Percentage_vote = 100*Election_results[key]/Total_votes
        Percentage_vote = round(Percentage_vote,2)
        message3 = f"{key}:{Election_results[key]} ({Percentage_vote}%)"
        print(message3)
        file.write(f"{message3}\n")


    #Defining a funciton to find the winner from the dictionary with maximum votes
    def keywithmaxval(d):
        """ a) create a list of the dict's keys and values; 
            b) return the key with the max value"""  
        v=list(d.values())
        k=list(d.keys())
        return k[v.index(max(v))]


    #printing winner
    print("------------------------------------------")
    message4 = f"Winner: {keywithmaxval(Election_results)}"
    print(message4)
    file.write(f"{message4}\n")
    print("-------------------------------------------")