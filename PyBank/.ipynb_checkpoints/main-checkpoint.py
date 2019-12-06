import os
import csv

import pandas as pd
import numpy as np


csvpath = os.path.join ('..','PyBank','budget_data.csv')

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csvreader:
        #print(row)
        
#print(csvpath)
df = pd.read_csv('budget_data.csv')

#df['Date']
#df.columns
#df[['Date','Profit/Losses']]

#df.iloc[5]

#Number of unique elements
TotalMonths = df['Date'].nunique()
TM = ("Total Months = " + str(TotalMonths))

sum = df['Profit/Losses'].sum()
T = "Total: $" + str(sum)

#The average of the changes in "Profit/Losses" over the entire period
pl_diff = df['Profit/Losses'].diff()
#print(pl_diff)

#OR
#pl - pl.shift(1)

#OR
#pl = df['Profit/Losses']


avg_change = pl_diff.mean()  
AC = "Average Change: $" + str(round(avg_change,2))

#To get the percent change
#pl.pct_change()

#The greatest increase in profits (date and amount) over the entire period
#Greatest Increase in Profits: Feb-2012 ($1926159)

pl_max = int(pl_diff.max())

pl_max_index = pl_diff[pl_diff == pl_diff.max()].index.values
#print(pl_max_index)
pl_max_index_data = df[df.index == pl_max_index[0]]
max_date = pl_max_index_data.iloc[0,0]

GI = "Greatest Increase in Profits: " + max_date + " ($"+ str(pl_max) + ")"



#The greatest decrease in losses (date and amount) over the entire period
#Greatest Decrease in Profits: Sep-2013 ($-2196167)
pl_min = int(pl_diff.min())

pl_min_index = pl_diff[pl_diff == pl_diff.min()].index.values
#print(pl_max_index)
pl_min_index_data = df[df.index == pl_min_index[0]]
min_date = pl_min_index_data.iloc[0,0]

GD = "Greatest Decrease in Profits: " + min_date + " ($"+ str(pl_min) + ")"

print("Financial Analysis")
print("----------------------------")
print(TM)
print(T)
print(AC)
print(GI)
print(GD)


f = open('PyBank_HW.txt', 'w')

with open('PyBank_HW.txt', 'w') as f:
    f.write("Financial Analysis\n----------------------------\n")
    f.write(f"{TM}\n")
    f.write(f"{T}\n")
    f.write(f"{AC}\n")
    f.write(f"{GI}\n")
    f.write(f"{GD}\n")
