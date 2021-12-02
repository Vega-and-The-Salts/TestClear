import sys, os, time, pandas as pd, matplotlib as plt, numpy as np
#"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
months = {1 : ["January", "February", "March", "April", "May"],
2 : ["February", "March", "April", "May", "June"],
3 : ["March", "April", "May", "June", "July"],
4 : ["April", "May", "June", "July", "August"],
5 : ["May", "June", "July", "August", "September"],
6 : ["June", "July", "August", "September", "October"],
7 : ["July", "August", "September", "October", "November"],
8 : ["August", "September", "October", "November", "December"]}



startMonth = input("Which iteration is this: ")

dataFirstMonth = pd.read_excel("AprilData.xlsx")





