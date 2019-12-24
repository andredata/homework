import pandas as pd
import numpy as np

election_data = pd.read_csv('election_data.csv')
              
total_votes = len(election_data)
received_votes = election_data['Candidate'].unique()

#print(election_data)
print('Election Results \n')
print('------------------------- \n')
print('Candidates Who Received Votes: {} \n'.format(received_votes))
print('------------------------- \n')
print('Total Votes: {} \n'.format(total_votes))

winner = ''
prev_percent = 0

text = ''

for name in received_votes:
    votes = len(election_data[election_data['Candidate'] == name])
    percent = round(votes / total_votes * 100, 2)
    print('{}: {}% ({})'.format(name, percent, votes))
    text = text + '\n {}: {}% ({}) \n '.format(name, percent, votes)
    
    if percent >= prev_percent:
        winner = name
          
    prev_percent = percent

print('------------------------- \n')

print('Winner: {} \n'.format(winner))
print('------------------------- \n')

file = open('results.txt', 'w')
file.write('Election Results \n' + '------------------------- \n' + 'Candidates Who Received Votes: {} \n'.format(received_votes) + '------------------------- \n' + 'Total Votes: {} \n'.format(total_votes) + text + '------------------------- \n' + 'Winner: {} \n'.format(winner) + '------------------------- \n')
file.close()
