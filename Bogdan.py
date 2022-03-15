import pandas as pd
#import linecache
import matplotlib.pyplot as plt

import csv

filename = 'FinallOneCSV.csv'

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin = []
    for row in datareader:
        if (row[0] == 'Average '):
            tempmin.append(row[2])
    print (tempmin)    

Time2020=['January','February','asdad','dadas' ,'dasds','dasddsas','dasfdas','dasdahs','dasdtas','dasdeqas','dastdas','dauksdas']
Temperature= [tempmin]
plt.plot(Time2020,tempmin)
plt.title('Temperature 2020')
plt.xlabel('Time2020')
plt.ylabel('Temperature')
plt.show()
