import pandas as pd
import numpy as np

budget_data = pd.read_csv('budget_data.csv')

total_months = len(budget_data)
total = budget_data['Profit/Losses'].sum()

budget_data['Change'] = budget_data['Profit/Losses'].diff()
budget_data['Change'] = budget_data['Change'].fillna(0)
budget_data['Change'] = budget_data['Change'].astype('int64')

avg_change = round(budget_data['Change'].mean(), 2)
greatest_inc = budget_data.iloc[budget_data['Change'].argmax()]
greatest_dec = budget_data.iloc[budget_data['Change'].argmin()]

#print(budget_data)
print('Financial Analysis \n')
print('---------------------------- \n')
print('Total Months: {} \n'.format(total_months))
print('Total: ${} \n'.format(total))
print('Average Change: ${} \n'.format(avg_change))
print('Greatest Increase in Profits: {} \n'.format(greatest_inc))
print('Greatest Decrease in Profits: {} \n'.format(greatest_dec))

file = open('results.txt', 'w')
file.write('Financial Analysis \n' + '---------------------------- \n' + 'Total Months: {} \n'.format(total_months) + 'Total: ${} \n'.format(total) + 'Average Change: ${} \n'.format(avg_change) + 'Greatest Increase in Profits: {} \n'.format(greatest_inc) + 'Greatest Decrease in Profits: {} \n'.format(greatest_dec))
file.close()
