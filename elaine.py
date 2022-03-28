from unicodedata import decimal
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import csv
import itertools


filename = 'FinallOneCSV.csv'

print ('-------------------------------------------- 2009')



#2009 maximum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2009'):
            tempmin2020.append(float(row[2]))
            counter= counter-1
            print (tempmin2020)    
        if (counter== 12): 
            break 
plt.figure(figsize=(12,5))
Time2020=['January','February','March','April' ,'May','June','July','August','September','October','November','December']
Temperature= [tempmin2020]
plt.plot(Time2020,tempmin2020, '-ok',color='green',linestyle='dashed',markerfacecolor='blue')
plt.grid(axis= 'y')
plt.title('Maximum Temperature 2009')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2009 average temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempavg2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2009'):
            tempavg2020.append(float(row[3]))
            counter= counter-1
            print (tempavg2020)    
        if (counter== 12): 
            break 
plt.figure(figsize=(12,5))
Time2020=['January','February','March','April' ,'May','June','July','August','September','October','November','December']
Temperature= [tempavg2020]
plt.plot(Time2020,tempmin2020, '-ok',color='green',linestyle='dashed',markerfacecolor='blue')
plt.grid(axis= 'y')
plt.title('Average Temperature 2009')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2009 minimum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2009'):
            tempmin2020.append(float(row[4]))
            counter= counter-1
            print (tempmin2020)    
        if (counter== 12): 
            break 
plt.figure(figsize=(12,5))
Time2020=['January','February','March','April' ,'May','June','July','August','September','October','November','December']
Temperature= [tempmin2020]
plt.plot(Time2020,tempmin2020, '-ok',color='green',linestyle='dashed',markerfacecolor='blue')
plt.grid(axis= 'y')
plt.title('Minimum Temperature 2009')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

print ('-------------------------------------------- DewPoint 2009')
#2009 maximum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2009'):
            tempmin2020.append(float(row[5]))
            counter= counter-1
            print (tempmin2020)    
        if (counter== 12): 
            break 
plt.figure(figsize=(12,5))
Time2020=['January','February','March','April' ,'May','June','July','August','September','October','November','December']
Temperature= [tempmin2020]
plt.plot(Time2020,tempmin2020, '-ok',color='green',linestyle='dashed',markerfacecolor='blue')
plt.grid(axis= 'y')
plt.title('Maximum Dew Point 2009')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2009 average dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2009'):
            tempmin2020.append(float(row[6]))
            counter= counter-1
            print (tempmin2020)    
        if (counter== 12): 
            break 
plt.figure(figsize=(12,5))
Time2020=['January','February','March','April' ,'May','June','July','August','September','October','November','December']
Temperature= [tempmin2020]
plt.plot(Time2020,tempmin2020, '-ok',color='green',linestyle='dashed',markerfacecolor='blue')
plt.grid(axis= 'y')
plt.title('Average Dew Point 2009')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2009 minimum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2009'):
            tempmin2020.append(float(row[7]))
            counter= counter-1
            print (tempmin2020)    
        if (counter== 12): 
            break 
plt.figure(figsize=(12,5))
Time2020=['January','February','March','April' ,'May','June','July','August','September','October','November','December']
Temperature= [tempmin2020]
plt.plot(Time2020,tempmin2020, '-ok',color='green',linestyle='dashed',markerfacecolor='blue')
plt.grid(axis= 'y')
plt.title('Minimum Temperature 2020')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2009 maximum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2009'):
            tempmin2020.append(float(row[8]))
            counter= counter-1
            print (tempmin2020)    
        if (counter== 12): 
            break 
plt.figure(figsize=(12,5))
Time2020=['January','February','March','April' ,'May','June','July','August','September','October','November','December']
Temperature= [tempmin2020]
plt.plot(Time2020,tempmin2020, '-ok',color='green',linestyle='dashed',markerfacecolor='blue')
plt.grid(axis= 'y')
plt.title('Maximum Dew Point 2009')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2009 average humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2009'):
            tempmin2020.append(float(row[9]))
            counter= counter-1
            print (tempmin2020)    
        if (counter== 12): 
            break 
plt.figure(figsize=(12,5))
Time2020=['January','February','March','April' ,'May','June','July','August','September','October','November','December']
Temperature= [tempmin2020]
plt.plot(Time2020,tempmin2020, '-ok',color='green',linestyle='dashed',markerfacecolor='blue')
plt.grid(axis= 'y')
plt.title('Average Humidity 2009')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2009 minimum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2009'):
            tempmin2020.append(float(row[10]))
            counter= counter-1
            print (tempmin2020)    
        if (counter== 12): 
            break 
plt.figure(figsize=(12,5))
Time2020=['January','February','March','April' ,'May','June','July','August','September','October','November','December']
Temperature= [tempmin2020]
plt.plot(Time2020,tempmin2020, '-ok',color='green',linestyle='dashed',markerfacecolor='blue')
plt.grid(axis= 'y')
plt.title('Minimum Humidity 2009')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2009 maximum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2009'):
            tempmin2020.append(float(row[11]))
            counter= counter-1
            print (tempmin2020)    
        if (counter== 12): 
            break 
plt.figure(figsize=(12,5))
Time2020=['January','February','March','April' ,'May','June','July','August','September','October','November','December']
Temperature= [tempmin2020]
plt.plot(Time2020,tempmin2020, '-ok',color='green',linestyle='dashed',markerfacecolor='blue')
plt.grid(axis= 'y')
plt.title('Maximum Wind Speed 2009')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2009 average wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2009'):
            tempmin2020.append(float(row[12]))
            counter= counter-1
            print (tempmin2020)    
        if (counter== 12): 
            break 
plt.figure(figsize=(12,5))
Time2020=['January','February','March','April' ,'May','June','July','August','September','October','November','December']
Temperature= [tempmin2020]
plt.plot(Time2020,tempmin2020, '-ok',color='green',linestyle='dashed',markerfacecolor='blue')
plt.grid(axis= 'y')
plt.title('Average Wind Speed 2009')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2009 minimum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2009'):
            tempmin2020.append(float(row[13]))
            counter= counter-1
            print (tempmin2020)    
        if (counter== 12): 
            break 
plt.figure(figsize=(12,5))
Time2020=['January','February','March','April' ,'May','June','July','August','September','October','November','December']
Temperature= [tempmin2020]
list1, list2 = zip(*sorted(zip(Time2020, Temperature)))
plt.plot(Time2020,tempmin2020, '-ok',color='green',linestyle='dashed',markerfacecolor='blue')
plt.grid(axis= 'y')
plt.title('Minimum Wind Speed 2009')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2009 maximum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2009'):
            tempmin2020.append(float(row[14]))
            counter= counter-1
            print (tempmin2020)    
        if (counter== 12): 
            break 
plt.figure(figsize=(12,5))
Time2020=['January','February','March','April' ,'May','June','July','August','September','October','November','December']
Temperature= [tempmin2020]
plt.plot(Time2020,tempmin2020, '-ok',color='green',linestyle='dashed',markerfacecolor='blue')
plt.grid(axis= 'y')
plt.title('Maximum Pressure 2009')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2009 average pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2009'):
            tempmin2020.append(float(row[15]))
            counter= counter-1
            print (tempmin2020)    
        if (counter== 12): 
            break 
plt.figure(figsize=(12,5))
Time2020=['January','February','March','April' ,'May','June','July','August','September','October','November','December']
Temperature= [tempmin2020]
plt.plot(Time2020,tempmin2020, '-ok',color='green',linestyle='dashed',markerfacecolor='blue')
plt.grid(axis= 'y')
plt.title('Average Pressure 2009')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2009 minimum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2009'):
            tempmin2020.append(float(row[16]))
            counter= counter-1
            print (tempmin2020)    
        if (counter== 12): 
            break 
plt.figure(figsize=(12,5))
Time2020=['January','February','March','April' ,'May','June','July','August','September','October','November','December']
Temperature= [tempmin2020]
plt.plot(Time2020,tempmin2020, '-ok',color='green',linestyle='dashed',markerfacecolor='blue')
plt.grid(axis= 'y')
plt.title('Minimum Pressure 2009')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()