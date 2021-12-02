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


startMonth = input("Which iteration is this: ")

firstMonth = pd.read_excel(f'{startMonth[0]}.xslx')
secondMonth = pd.read_excel(f'{startMonth[1]}.xslx')
thirdMonth = pd.read_excel(f'{startMonth[2]}.xslx')
fourthMonth = pd.read_excel(f'{startMonth[3]}.xslx')




