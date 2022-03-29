from cProfile import label
import tkinter as tk
from tkinter import *
from tkinter import ttk
from unicodedata import decimal
import csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import statistics
from setuptools import Command


def getYearData(year, data_type, value_type):
    filename = 'FinallOneCSV.csv'
    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        yearData = []
        for row in datareader:
            if row[0].find('Average'+str(year)) != -1:
                if(data_type == 'temperature'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[2]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[3]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[4]))
                elif(data_type == 'DewPoint'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[5]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[6]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[7]))
                elif(data_type == 'Humidity'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[8]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[9]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[10]))
                elif(data_type == 'WindSpeed'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[11]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[12]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[13]))
                elif(data_type == 'Pressure'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[14]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[15]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[16]))
    return yearData

    # Max temp of the year
def findMaxValueYear(year_a, data_type):
    maxValueYear=[]
    for year in year_a:
        value_type = 'Maximum'
        year_a_data=getYearData(year, data_type, value_type)
        maxValueYear.append(max(year_a_data))

    return maxValueYear

def findMeanValueYear(year_a, data_type):
    meanValueYear=[]
    for year in year_a:
        value_type = 'Average'
        year_a_data=getYearData(year, data_type, value_type)
        meanValueYear.append(statistics.mean(year_a_data))

    return meanValueYear


# When you insert a year, data type and value type, itll findthe max for u
def findMinValueYear(year_a, data_type):
    minValueYear=[]
    for year in year_a:
        value_type = 'Minimum'
        year_a_data=getYearData(year, data_type, value_type)
        minValueYear.append(min(year_a_data))

    return minValueYear


# before setting maxValues array and years array to something    
def plotMaxValueCom(maxValues, years):
    plt.plot(years,maxValues, '-ok',color='green',linestyle='',markerfacecolor='green')

# before setting meanValues and years to something    
def plotMeanValueCom(meanValues, years):
    plt.plot(years,meanValues, '-ok',color='red',linestyle='',markerfacecolor='red')


# before setting minValues and years to something    
def plotMinValueCom(minValues, years):
    plt.plot(years,minValues, '-ok',color='yellow',linestyle='',markerfacecolor='yellow')


# Call the plot. Data_type = 'temperature'
def makeComPlot(year, data_type):

    maxValuesYear = findMaxValueYear(year, data_type)
    meanValuesYear = findMeanValueYear(year, data_type)
    minValuesYear = findMinValueYear(year, data_type)

    plt.figure(figsize=(12,5))
    plt.grid(axis= 'y')
    plt.xlabel('Years')
    plt.ylabel(data_type)

    plotMaxValueCom(maxValuesYear, year)
    plotMeanValueCom(meanValuesYear, year)
    plotMinValueCom(minValuesYear, year)
    
    plt.show()



years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
# Option 1.2 Function
def op1p2 ():
    op1p2 = Tk()
    op1p2.title("Temperature (Degrees F)")
    op1p2.geometry('500x320')
    op1p2.configure(background="grey")

    ttk.Label(op1p2, text = "Temperature (Degrees F)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)


    #1
    ttk.Label(op1p2, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)  
    # Combobox creation
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(op1p2, width = 27, textvariable = n)
    # Adding combobox drop down list
    yearchoosen1['values'] = years
    yearchoosen1.grid(column = 1, row = 5)
    yearchoosen1.current()

    #2
    ttk.Label(op1p2, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  
    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(op1p2, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.grid(column = 1, row = 7)
    yearchoosen2.current()

    #3
    ttk.Label(op1p2, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 9, padx = 10, pady = 25)  
    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(op1p2, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.grid(column = 1, row = 9)
    yearchoosen3.current()

    def click():
        data_type='temperature'
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen2.get()
        years = [year1, year2, year3]

        makeComPlot(year1,'temperature')


    #addbutton 
    Button(op1p2,text="Submit", width=6, command=click) .grid(row=10,column=1,sticky=W)

    #add exit button
    Button(op1p2,text="Quit", width=6, command=op1p2.destroy) .grid(row=10,column=2,sticky=W)

    op1p2.mainloop()

def op2p2():

    
