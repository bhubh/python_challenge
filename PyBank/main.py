# Importing os and csv modules
import os
import csv

#give csv path
csvpath = os.path.join('Resources', 'budget_data.csv')

# creating lists to storre data
date = []   #variable to store date :row [0]
profit_loss = []  # variable to store profit/loss: row[1]
change = []       # variable to store change in profit/loss each month


#Reading CSV file

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    #Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #Reading each row of data after the header
    for row in csvreader:
        #add date
        date.append(row[0])
        profit_loss.append(row[1])
        
        

#calculating months
months_total = len(date)  #total no of rows in date 
print("Financial Analysis")
print("-------------------------------------------")
print(f"Total Months: {months_total}")


#calculate total profit/loss

# initialize variable for total profit/loss
profit_loss_total = 0
#using for Loop
for i in range(len(profit_loss)):
    
    profit_loss_total = profit_loss_total + int(profit_loss[i])
    
#printing total profit or loss       
print(f"Total Profit/Loss: {profit_loss_total}")


# using for loop to calculate changes in profit/losses

for i in range(len(profit_loss)-1):
     
    change.append(int(profit_loss[i+1])-int(profit_loss[i]))


# Calculating the average, maximum and minimum value of change in profit/loss  
Average_change = sum(change)/len(change)
Max_change = max(change)
Min_change = min(change)

#finding the index for maximum profit and maximum loss change
Index_Profit_change = change.index(Max_change)
Index_Loss_change = change.index(Min_change)

#finding corresponding date
date_Max_Profit_change = date[Index_Profit_change+1]
date_Max_Loss_change = date[Index_Loss_change+1]

#ptinting Maximum change in profit, Max change in loss and average change
print(f"Greatest increase in Profit: {date_Max_Profit_change} ({Max_change})")
print(f"Greatest decrease in profit: {date_Max_Loss_change} ({Min_change})")
print(f"Average Change: {Average_change}")




