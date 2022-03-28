from unicodedata import decimal
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import csv
import itertools


filename = 'FinallOneCSV.csv'

print ('-------------------------------------------- 2020')



#2020 maximum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2020'):
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
plt.title('Maximum Temperature 2020')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2020 average temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempavg2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2020'):
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
plt.title('Average Temperature 2020')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2020 minimum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2020'):
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
plt.title('Minimum Temperature 2020')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

print ('-------------------------------------------- DewPoint 2020')
#2020 maximum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2020'):
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
plt.title('Maximum Dew Point 2020')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2020 average dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2020'):
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
plt.title('Average Dew Point 2020')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2020 minimum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2020'):
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

#2020 maximum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2020'):
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
plt.title('Maximum Dew Point 2020')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2020 average humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2020'):
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
plt.title('Average Humidity 2020')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2020 minimum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2020'):
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
plt.title('Minimum Humidity 2020')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2020 maximum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2020'):
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
plt.title('Maximum Wind Speed 2020')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2020 average wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2020'):
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
plt.title('Average Wind Speed 2020')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2020 minimum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2020'):
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
plt.title('Minimum Wind Speed 2020')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2020 maximum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2020'):
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
plt.title('Maximum Pressure 2020')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2020 average pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2020'):
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
plt.title('Average Pressure 2020')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2020 minimum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2020'):
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
plt.title('Minimum Pressure 2020')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

print ('------------------------------------------------------------------------------------------------------- 2019')



#2019 maximum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2019'):
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
plt.title('Maximum Temperature 2019')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2019 average temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempavg2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2019'):
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
plt.title('Average Temperature 2019')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2019 minimum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2019'):
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
plt.title('Minimum Temperature 2019')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

print ('-------------------------------------------- DewPoint 2019')
#2019 maximum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2019'):
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
plt.title('Maximum Dew Point 2019')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2019 average dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2019'):
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
plt.title('Average Dew Point 2019')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2019 minimum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2019'):
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

#2019 maximum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2019'):
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
plt.title('Maximum Dew Point 2019')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2019 average humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2019'):
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
plt.title('Average Humidity 2019')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2019 minimum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2019'):
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
plt.title('Minimum Humidity 2019')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2019 maximum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2019'):
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
plt.title('Maximum Wind Speed 2019')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2019 average wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2019'):
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
plt.title('Average Wind Speed 2019')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2019 minimum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2019'):
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
plt.title('Minimum Wind Speed 2019')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2019 maximum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2019'):
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
plt.title('Maximum Pressure 2019')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2019 average pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2019'):
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
plt.title('Average Pressure 2019')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2019 minimum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2019'):
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
plt.title('Minimum Pressure 2019')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()



#menu 
import tkinter as tk
from tkinter import *
from tkinter import ttk

# Creating tkinter window
window = Tk()
window.title("Climate and Weather Team 20")
window.geometry('500x320')
window.configure(background="darkgrey")

ttk.Label(window, text = "Climate and weather Team 20", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)

# label max/average/min
ttk.Label(window, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)  
# Combobox creation
n = tk.StringVar()
yearchoosen = ttk.Combobox(window, width = 27, textvariable = n)
# Adding combobox drop down list
yearchoosen['values'] = (' 2013',
                         ' 2014',
                         ' 2015',
                          ' 2016',
                          ' 2017',
                          ' 2018',
                          ' 2019',
                          ' 2020',
                          ' 2021',)
yearchoosen.grid(column = 1, row = 5)
yearchoosen.current()



# label month
ttk.Label(window, text = "Select the Month :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 6, padx = 10, pady = 25)
# Combobox creation month
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)
  
# Adding combobox drop down list
monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')
  
monthchoosen.grid(column = 1, row = 6)
monthchoosen.current()

# label year
ttk.Label(window, text = "Select the  :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  
# Combobox creation
n = tk.StringVar()
typevalue = ttk.Combobox(window, width = 27, textvariable = n)
# Adding combobox drop down list
typevalue['values'] = (' Minimum ', 
                          ' Average ',
                          ' Maximum ')
typevalue.grid(column = 1, row = 7)
typevalue.current()


#Submitbutton function
def click ():
    def save_info ():
    value=typevalue.get()
    value2=yearchoosen.get()
    if value == " Minimum" and value2==" 2020":
        with open(filename, 'r') as csvfile:
            datareader = csv.reader(csvfile)
            tempmin2020 = []
           
    
            for row in datareader:
                
                if (row[0] == 'Average2020'):
                    tempmin2020.append(float(row[2]))
                   
                    print (tempmin2020)    
         
    plt.figure(figsize=(12,5))
    Time2020=['January','February','March','April' ,'May','June','July','August','September','October','November','December']
    Temperature= [tempmin2020]
    plt.plot(Time2020,tempmin2020, '-ok',color='green',linestyle='dashed',markerfacecolor='blue')
    plt.grid(axis= 'y')
    plt.title('Maximum Temperature 2020')
    plt.xlabel('Month')
    plt.ylabel('Value')
    plt.show()
#addbutton 
Button(window,text="Submit", width=6, command=click) .grid(row=8,column=1,sticky=W)

#add exit button
Button(window,text="Quit", width=6, command=window.destroy) .grid(row=8,column=2,sticky=W)



window.mainloop()
