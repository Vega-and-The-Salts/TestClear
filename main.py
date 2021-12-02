import sys, os, time, pandas as pd, matplotlib as plt, numpy as np

## This is how we will work through with minimal user intervention to reduce error
months = {1 : ["January", "February", "March", "April"], 
2 : ["February", "March", "April", "May"],
3 : ["March", "April", "May", "June"], 
4 : ["April", "May", "June", "July"], 
5 : ["May", "June", "July", "August"],
6 : ["June", "July", "August", "September"], 
7 : ["July", "August", "September", "October"], 
8 : ["August", "September", "October", "November"]}


startMonth = 1#int(input("Which iteration is this: "))

firstMonth = pd.read_excel(f'{months[startMonth][0]}.xlsx')
secondMonth = pd.read_excel(f'{months[startMonth][1]}.xlsx')
thirdMonth = pd.read_excel(f'{months[startMonth][2]}.xlsx')
fourthMonth = pd.read_excel(f'{months[startMonth][3]}.xlsx')




