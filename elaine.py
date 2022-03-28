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



print ('-------------------------------------------- 2010')



#2010 maximum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2010'):
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
plt.title('Maximum Temperature 2010')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2010 average temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempavg2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2010'):
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
plt.title('Average Temperature 2010')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2010 minimum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2010'):
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
plt.title('Minimum Temperature 2010')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

print ('-------------------------------------------- DewPoint 2010')
#2010 maximum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2010'):
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
plt.title('Maximum Dew Point 2010')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2010 average dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2010'):
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
plt.title('Average Dew Point 2010')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2010 minimum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2010'):
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

#2010 maximum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2010'):
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
plt.title('Maximum Dew Point 2010')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2010 average humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2010'):
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
plt.title('Average Humidity 2010')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2010 minimum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2010'):
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
plt.title('Minimum Humidity 2010')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2010 maximum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2010'):
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
plt.title('Maximum Wind Speed 2010')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2010 average wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2010'):
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
plt.title('Average Wind Speed 2010')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2010 minimum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2010'):
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
plt.title('Minimum Wind Speed 2010')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2010 maximum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2010'):
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
plt.title('Maximum Pressure 2010')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2010 average pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2010'):
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
plt.title('Average Pressure 2010')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2010 minimum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2010'):
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
plt.title('Minimum Pressure 2010')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()



print ('-------------------------------------------- 2011')



#2011 maximum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2011'):
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
plt.title('Maximum Temperature 2011')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2011 average temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempavg2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2011'):
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
plt.title('Average Temperature 2011')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2011 minimum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2011'):
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
plt.title('Minimum Temperature 2011')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

print ('-------------------------------------------- DewPoint 2011')
#2011 maximum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2011'):
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
plt.title('Maximum Dew Point 2011')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2011 average dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2011'):
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
plt.title('Average Dew Point 2011')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2011 minimum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2011'):
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

#2011 maximum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2011'):
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
plt.title('Maximum Dew Point 2011')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2011 average humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2011'):
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
plt.title('Average Humidity 2011')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2011 minimum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2011'):
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
plt.title('Minimum Humidity 2011')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2011 maximum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2011'):
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
plt.title('Maximum Wind Speed 2011')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2011 average wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2011'):
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
plt.title('Average Wind Speed 2011')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2011 minimum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2011'):
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
plt.title('Minimum Wind Speed 2011')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2011 maximum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2011'):
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
plt.title('Maximum Pressure 2011')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2011 average pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2011'):
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
plt.title('Average Pressure 2011')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2011 minimum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2011'):
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
plt.title('Minimum Pressure 2011')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()


print ('-------------------------------------------- 2012')



#2012 maximum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2012'):
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
plt.title('Maximum Temperature 2012')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2012 average temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempavg2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2012'):
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
plt.title('Average Temperature 2012')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2012 minimum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2012'):
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
plt.title('Minimum Temperature 2012')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

print ('-------------------------------------------- DewPoint 2012')
#2012 maximum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2012'):
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
plt.title('Maximum Dew Point 2012')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2012 average dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2012'):
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
plt.title('Average Dew Point 2012')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2012 minimum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2012'):
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

#2012 maximum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2012'):
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
plt.title('Maximum Dew Point 2012')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2012 average humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2012'):
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
plt.title('Average Humidity 2012')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2012 minimum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2012'):
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
plt.title('Minimum Humidity 2012')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2012 maximum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2012'):
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
plt.title('Maximum Wind Speed 2012')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2012 average wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2012'):
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
plt.title('Average Wind Speed 2012')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2012 minimum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2012'):
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
plt.title('Minimum Wind Speed 2012')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2012 maximum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2012'):
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
plt.title('Maximum Pressure 2012')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2012 average pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2012'):
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
plt.title('Average Pressure 2012')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2012 minimum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2012'):
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
plt.title('Minimum Pressure 2012')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()


print ('-------------------------------------------- 2013')



#2013 maximum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2013'):
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
plt.title('Maximum Temperature 2013')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2013 average temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempavg2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2013'):
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
plt.title('Average Temperature 2013')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2013 minimum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2013'):
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
plt.title('Minimum Temperature 2013')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

print ('-------------------------------------------- DewPoint 2013')
#2013 maximum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2013'):
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
plt.title('Maximum Dew Point 2013')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2013 average dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2013'):
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
plt.title('Average Dew Point 2013')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2013 minimum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2013'):
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

#2013 maximum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2013'):
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
plt.title('Maximum Dew Point 2013')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2013 average humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2013'):
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
plt.title('Average Humidity 2013')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2013 minimum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2013'):
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
plt.title('Minimum Humidity 2013')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2013 maximum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2013'):
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
plt.title('Maximum Wind Speed 2013')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2013 average wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2013'):
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
plt.title('Average Wind Speed 2013')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2013 minimum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2013'):
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
plt.title('Minimum Wind Speed 2013')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2013 maximum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2013'):
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
plt.title('Maximum Pressure 2013')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2013 average pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2013'):
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
plt.title('Average Pressure 2013')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2013 minimum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2013'):
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
plt.title('Minimum Pressure 2013')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()


print ('-------------------------------------------- 2014')



#2014 maximum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2014'):
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
plt.title('Maximum Temperature 2014')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2014 average temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempavg2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2014'):
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
plt.title('Average Temperature 2014')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2014 minimum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2014'):
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
plt.title('Minimum Temperature 2014')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

print ('-------------------------------------------- DewPoint 2014')
#2014 maximum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2014'):
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
plt.title('Maximum Dew Point 2014')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2014 average dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2014'):
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
plt.title('Average Dew Point 2014')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2014 minimum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2014'):
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

#2014 maximum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2014'):
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
plt.title('Maximum Dew Point 2014')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2014 average humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2014'):
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
plt.title('Average Humidity 2014')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2014 minimum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2014'):
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
plt.title('Minimum Humidity 2014')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2014 maximum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2014'):
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
plt.title('Maximum Wind Speed 2014')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2014 average wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2014'):
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
plt.title('Average Wind Speed 2014')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2014 minimum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2014'):
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
plt.title('Minimum Wind Speed 2014')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2014 maximum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2014'):
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
plt.title('Maximum Pressure 2014')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2014 average pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2014'):
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
plt.title('Average Pressure 2014')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2014 minimum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2014'):
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
plt.title('Minimum Pressure 2014')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()


print ('-------------------------------------------- 2015')



#2015 maximum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2015'):
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
plt.title('Maximum Temperature 2015')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2015 average temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempavg2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2015'):
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
plt.title('Average Temperature 2015')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2015 minimum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2015'):
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
plt.title('Minimum Temperature 2015')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

print ('-------------------------------------------- DewPoint 2015')
#2015 maximum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2015'):
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
plt.title('Maximum Dew Point 2015')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2015 average dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2015'):
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
plt.title('Average Dew Point 2015')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2015 minimum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2015'):
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

#2015 maximum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2015'):
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
plt.title('Maximum Dew Point 2015')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2015 average humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2015'):
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
plt.title('Average Humidity 2015')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2015 minimum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2015'):
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
plt.title('Minimum Humidity 2015')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2015 maximum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2015'):
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
plt.title('Maximum Wind Speed 2015')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2015 average wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2015'):
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
plt.title('Average Wind Speed 2015')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2015 minimum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2015'):
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
plt.title('Minimum Wind Speed 2015')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2015 maximum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2015'):
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
plt.title('Maximum Pressure 2015')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2015 average pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2015'):
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
plt.title('Average Pressure 2015')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2015 minimum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2015'):
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
plt.title('Minimum Pressure 2015')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()


print ('-------------------------------------------- 2016')



#2016 maximum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2016'):
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
plt.title('Maximum Temperature 2016')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2016 average temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempavg2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2016'):
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
plt.title('Average Temperature 2016')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2016 minimum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2016'):
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
plt.title('Minimum Temperature 2016')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

print ('-------------------------------------------- DewPoint 2016')
#2016 maximum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2016'):
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
plt.title('Maximum Dew Point 2016')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2016 average dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2016'):
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
plt.title('Average Dew Point 2016')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2016 minimum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2016'):
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

#2016 maximum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2016'):
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
plt.title('Maximum Dew Point 2016')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2016 average humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2016'):
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
plt.title('Average Humidity 2016')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2016 minimum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2016'):
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
plt.title('Minimum Humidity 2016')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2016 maximum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2016'):
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
plt.title('Maximum Wind Speed 2016')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2016 average wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2016'):
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
plt.title('Average Wind Speed 2016')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2016 minimum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2016'):
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
plt.title('Minimum Wind Speed 2016')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2016 maximum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2016'):
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
plt.title('Maximum Pressure 2016')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2016 average pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2016'):
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
plt.title('Average Pressure 2016')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2016 minimum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2016'):
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
plt.title('Minimum Pressure 2016')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()


print ('-------------------------------------------- 2017')



#2017 maximum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2017'):
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
plt.title('Maximum Temperature 2017')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2017 average temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempavg2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2017'):
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
plt.title('Average Temperature 2017')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2017 minimum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2017'):
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
plt.title('Minimum Temperature 2017')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

print ('-------------------------------------------- DewPoint 2017')
#2017 maximum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2017'):
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
plt.title('Maximum Dew Point 2017')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2017 average dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2017'):
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
plt.title('Average Dew Point 2017')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2017 minimum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2017'):
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

#2017 maximum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2017'):
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
plt.title('Maximum Dew Point 2017')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2017 average humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2017'):
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
plt.title('Average Humidity 2017')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2017 minimum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2017'):
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
plt.title('Minimum Humidity 2017')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2017 maximum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2017'):
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
plt.title('Maximum Wind Speed 2017')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2017 average wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2017'):
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
plt.title('Average Wind Speed 2017')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2017 minimum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2017'):
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
plt.title('Minimum Wind Speed 2017')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2017 maximum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2017'):
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
plt.title('Maximum Pressure 2017')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2017 average pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2017'):
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
plt.title('Average Pressure 2017')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2017 minimum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2017'):
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
plt.title('Minimum Pressure 2017')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()


print ('-------------------------------------------- 2018')



#2018 maximum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2018'):
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
plt.title('Maximum Temperature 2018')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2018 average temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempavg2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2018'):
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
plt.title('Average Temperature 2018')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

#2018 minimum temperature
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2018'):
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
plt.title('Minimum Temperature 2018')
plt.xlabel('Month')
plt.ylabel('Temperature (° F)')
plt.show()

print ('-------------------------------------------- DewPoint 2018')
#2018 maximum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2018'):
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
plt.title('Maximum Dew Point 2018')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2018 average dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2018'):
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
plt.title('Average Dew Point 2018')
plt.xlabel('Month')
plt.ylabel('Dew Point (° F)')
plt.show()

#2018 minimum dew point
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2018'):
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

#2018 maximum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2018'):
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
plt.title('Maximum Dew Point 2018')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2018 average humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2018'):
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
plt.title('Average Humidity 2018')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2018 minimum humidity
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2018'):
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
plt.title('Minimum Humidity 2018')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.show()

#2018 maximum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2018'):
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
plt.title('Maximum Wind Speed 2018')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2018 average wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2018'):
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
plt.title('Average Wind Speed 2018')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2018 minimum wind speed
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2018'):
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
plt.title('Minimum Wind Speed 2018')
plt.xlabel('Month')
plt.ylabel('Wind Speed (mph)')
plt.show()

#2018 maximum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2018'):
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
plt.title('Maximum Pressure 2018')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2018 average pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2018'):
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
plt.title('Average Pressure 2018')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()

#2018 minimum pressure
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin2020 = []
    counter = 0
    rowCounter = 1
    
    for row in datareader:
        rowCounter=rowCounter+1
        if (row[0] == 'Average2018'):
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
plt.title('Minimum Pressure 2018')
plt.xlabel('Month')
plt.ylabel('Pressure (Hg)')
plt.show()