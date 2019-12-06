import os
import csv

import pandas as pd
import numpy as np


csvpath = os.path.join ('..','PyPoll','election_data.csv')

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
df = pd.read_csv('election_data.csv')
#print(df)

#The total number of votes cast
Votes = df['Voter ID'].nunique()
V = ("Total Votes: " + str(Votes))
print(V)

#The total number of votes each candidate won
group_voter_count = pd.DataFrame(df['Candidate'].value_counts())
#group_voter_count.head()


#group_voter_count.index

#The percentage of votes each candidate won
group_voter_per = pd.DataFrame(df['Candidate'].value_counts(normalize=True).mul(100).round(3).astype(str) + '%')
#group_voter_per.head()

#group_voter_per.index

result = pd.merge(group_voter_per
                 ,group_voter_count
                 , how='left',on=group_voter_per.index)

df_combined = result['key_0'].map(str) + ':  ' + result['Candidate_x'].map(str) + ' (' + result['Candidate_y'].map(str) + ')'  
print (df_combined)

# The winner of the election based on popular vote.
result.sort_values(by='Candidate_x', ascending=False)

 # Election Results
  #Total Votes: 3521001
#  -------------------------
 # Khan: 63.000% (2218231)
 # Correy: 20.000% (704200)
 # Li: 14.000% (492940)
 # O'Tooley: 3.000% (105630)
 # -------------------------
 # Winner: Khan
 # -------------------------

print("Winner: " + result.iloc[0,0])

