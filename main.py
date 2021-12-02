import sys, os, time, pandas as pd, matplotlib as plt, numpy as np




# Set of months that will be read
months = {1 : ["January", "February", "March", "April", 50], 
2 : ["February", "March", "April", "May", 60],
3 : ["March", "April", "May", "June", 70], 
4 : ["April", "May", "June", "July", 80], 
5 : ["May", "June", "July", "August", 90],
6 : ["June", "July", "August", "September", 100], 
7 : ["July", "August", "September", "October", 100], 
8 : ["August", "September", "October", "November", 100]}

# Only user input to tell us which set of information is being run
startMonth = 1 #int(input("Which iteration is this: "))

# Read in all Excel files through Pandas given from startMonth -
firstMonth = pd.read_excel(f'{months[startMonth][0]}.xlsx')
secondMonth = pd.read_excel(f'{months[startMonth][1]}.xlsx')
thirdMonth = pd.read_excel(f'{months[startMonth][2]}.xlsx')
fourthMonth = pd.read_excel(f'{months[startMonth][3]}.xlsx')
issuedGroup = pd.read_excel("Saved_Repo.xlsx")

# Check to see if issuedGroup is populated
if issuedGroup.empty:
    pass
    # Look at each month and add the sum of all sum1+2+3 
    
    # Divide the gathered information against actualTotal1 to get the Percentage

    # Look at each month and add the sum of all sum01+02+03
    
    # Divide the gathered information against actualTotal01 to get the Percentage

    # If data falls below threshhold of startMonth[months][-1]

    # Write information to Saved_Repo.xlsx

    #Write information to new Excel file

    #Open new Excel file for view


# If issuedGroup is populated, find all names that are the same and drop rows

# Iterate through all names and create new rows with total1 divided by actualTotal1 and total2 % actualTotal2

# Save to new Excel file with all names of new group. Should not exist!

# Append 'Saved_Repo.xlsx' with dataframe from previous Excel file

# Open files for viewing (Saved_Repo.xlsx and {newExcelFileName}.xlsx)

