# Code to paste in to the program
# Needs to have another section after the user selects the data type (e.g. temperature for example)
# so the user can select if they want to compare years or a data type for 1 particular year

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

# Function to get year data
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

# Finding max temp of a year
def findMaxValueYear(year_a, data_type):
    maxValueYear=[]
    for year in year_a:
        value_type = 'Maximum'
        year_a_data=getYearData(year, data_type, value_type)
        maxValueYear.append(max(year_a_data))

    return maxValueYear

# Finding mean temp of a year
def findMeanValueYear(year_a, data_type):
    meanValueYear=[]
    for year in year_a:
        value_type = 'Average'
        year_a_data=getYearData(year, data_type, value_type)
        meanValueYear.append(statistics.mean(year_a_data))

    return meanValueYear


# Finding min temp of a year
def findMinValueYear(year_a, data_type):
    minValueYear=[]
    for year in year_a:
        value_type = 'Minimum'
        year_a_data=getYearData(year, data_type, value_type)
        minValueYear.append(min(year_a_data))

    return minValueYear


# Function to plot all the maxValues
def plotMaxValueCom(maxValues, years):
    plt.plot(years,maxValues, 'dk',markersize = 10, color='blue',linestyle='',markerfacecolor='blue', label="Maximum")

# Function to plot all the meanValues  
def plotMeanValueCom(meanValues, years):
    plt.plot(years,meanValues, 'sk',markersize = 10, color='magenta',linestyle='',markerfacecolor='magenta', label="Mean")


# Function to plot all the minValues   
def plotMinValueCom(minValues, years):
    plt.plot(years,minValues, 'ok', markersize = 10, color='red',linestyle='',markerfacecolor='red', label="Minimum")


# Function to make a single comparison graph. Plots for 1 year.
def makeComPlot(year, data_type):

    maxValuesYear = findMaxValueYear(year, data_type)
    meanValuesYear = findMeanValueYear(year, data_type)
    minValuesYear = findMinValueYear(year, data_type)
    
    plt.figure(figsize=(12,5))
    plt.grid(axis= 'y')
    plt.xlabel('Years')
    
    # Setting the title and y axis labels
    if (data_type=='temperature'):
        measurement="(° F)"
        title=f"Comparing the maximum, mean & minimum temperature values of {year[0]}, {year[1]} & {year[2]}"
    if (data_type=='DewPoint'):
        measurement="(° F)"
        title=f"Comparing the maximum, mean & minimum dew point values of {year[0]}, {year[1]} & {year[2]}"
    if (data_type=='Humidity'):
        measurement="(%)"
        title=f"Comparing the maximum, mean & minimum humidity values of {year[0]}, {year[1]} & {year[2]}"
    if (data_type=='WindSpeed'):
        measurement="(mph)"
        title=f"Comparing the maximum, mean & minimum wind speed values of {year[0]}, {year[1]} & {year[2]}"
    if (data_type=='Pressure'):
        measurement="(Hg)"
        title=f"Comparing the maximum, mean & minimum pressure values of {year[0]}, {year[1]} & {year[2]}"
    plt.title(title)
    plt.ylabel(data_type + " " + measurement)
    
    # Adding vertical lines
    plt.vlines(x=year, ymin=minValuesYear, ymax=[maxValuesYear], colors='black', ls='-', lw=2)

    # Plotting and adding a legend
    plotMaxValueCom(maxValuesYear, year)
    plotMeanValueCom(meanValuesYear, year)
    plotMinValueCom(minValuesYear, year)
    plt.legend(bbox_to_anchor=(1.1, 1.05))
    plt.show()



years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']


# Option 1.2 Function
def op1p2 ():

    # Creating the layout
    op1p2 = Tk()
    op1p2.title("Comparing Yearly Temperature (° F)")
    op1p2.geometry('500x320')
    op1p2.configure(background="grey")

    ttk.Label(op1p2, text = "Comparing Yearly Temperature (° F)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)

    # Year Selection 1 by creating labels, comboboxes & combobox drop down lists
    ttk.Label(op1p2, text = "Select Year 1 :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)     
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(op1p2, width = 27, textvariable = n)
    yearchoosen1['values'] = years
    yearchoosen1.grid(column = 1, row = 5)
    yearchoosen1.current()

    # Year Selection 2 by creating labels, comboboxes & combobox drop down lists
    ttk.Label(op1p2, text = "Select Year 2 :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  
    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(op1p2, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.grid(column = 1, row = 7)
    yearchoosen2.current()

    # Year Selection 3 by creating labels, comboboxes & combobox drop down lists
    ttk.Label(op1p2, text = "Select Year 3 :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 9, padx = 10, pady = 25)  
    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(op1p2, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.grid(column = 1, row = 9)
    yearchoosen3.current()

    # Submit button function to make ComPlot
    def clickop1p2():
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        yearSelections = [year1, year2, year3]

        makeComPlot(yearSelections,'temperature')

    #Adding submit & exit buttons
    Button(op1p2,text="Submit", width=6, command=clickop1p2) .grid(row=10,column=1,sticky=W)
    Button(op1p2,text="Quit", width=6, command=op1p2.destroy) .grid(row=10,column=2,sticky=W)

    op1p2.mainloop()




# Option 2.2 function
def op2p2 ():

    # Creating the layout
    op2p2 = Tk()
    op2p2.title("Comparing Yearly Dew Point (° F)")
    op2p2.geometry('500x320')
    op2p2.configure(background="grey")

    ttk.Label(op2p2, text = "Comparing Yearly Dew Point (° F)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)

    # Year Selection 1 by creating labels, comboboxes & combobox drop down lists
    ttk.Label(op2p2, text = "Select Year 1 :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)     
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(op2p2, width = 27, textvariable = n)
    yearchoosen1['values'] = years
    yearchoosen1.grid(column = 1, row = 5)
    yearchoosen1.current()

    # Year Selection 2 by creating labels, comboboxes & combobox drop down lists
    ttk.Label(op2p2, text = "Select Year 2 :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  
    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(op2p2, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.grid(column = 1, row = 7)
    yearchoosen2.current()

    # Year Selection 3 by creating labels, comboboxes & combobox drop down lists
    ttk.Label(op2p2, text = "Select Year 3 :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 9, padx = 10, pady = 25)  
    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(op2p2, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.grid(column = 1, row = 9)
    yearchoosen3.current()

    # Submit button function to make ComPlot
    def clickop2p2():
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        yearSelections = [year1, year2, year3]

        makeComPlot(yearSelections,'DewPoint')

    #Adding submit & exit buttons
    Button(op2p2,text="Submit", width=6, command=clickop2p2) .grid(row=10,column=1,sticky=W)
    Button(op2p2,text="Quit", width=6, command=op2p2.destroy) .grid(row=10,column=2,sticky=W)

    op2p2.mainloop()



# Option 3.2 Function
def op3p2 ():

    # Creating the layout
    op3p2 = Tk()
    op3p2.title("Comparing Yearly Humidity (%)")
    op3p2.geometry('500x320')
    op3p2.configure(background="grey")

    ttk.Label(op3p2, text = "Comparing Yearly Humidity (%)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)

    # Year Selection 1 by creating labels, comboboxes & combobox drop down lists
    ttk.Label(op3p2, text = "Select Year 1 :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)     
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(op3p2, width = 27, textvariable = n)
    yearchoosen1['values'] = years
    yearchoosen1.grid(column = 1, row = 5)
    yearchoosen1.current()

    # Year Selection 2 by creating labels, comboboxes & combobox drop down lists
    ttk.Label(op3p2, text = "Select Year 2 :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  
    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(op3p2, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.grid(column = 1, row = 7)
    yearchoosen2.current()

    # Year Selection 3 by creating labels, comboboxes & combobox drop down lists
    ttk.Label(op3p2, text = "Select Year 3 :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 9, padx = 10, pady = 25)  
    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(op3p2, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.grid(column = 1, row = 9)
    yearchoosen3.current()

    # Submit button function to make ComPlot
    def clickop3p2():
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        yearSelections = [year1, year2, year3]

        makeComPlot(yearSelections,'Humidity')

    #Adding submit & exit buttons
    Button(op3p2,text="Submit", width=6, command=clickop3p2) .grid(row=10,column=1,sticky=W)
    Button(op3p2,text="Quit", width=6, command=op3p2.destroy) .grid(row=10,column=2,sticky=W)

    op3p2.mainloop()


# Option 4.2 Function
def op4p2 ():

    # Creating the layout
    op4p2 = Tk()
    op4p2.title("Comparing Yearly WindSpeed (mph)")
    op4p2.geometry('500x320')
    op4p2.configure(background="grey")

    ttk.Label(op4p2, text = "Comparing Yearly WindSpeed (mph)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)

    # Year Selection 1 by creating labels, comboboxes & combobox drop down lists
    ttk.Label(op4p2, text = "Select Year 1 :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)     
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(op4p2, width = 27, textvariable = n)
    yearchoosen1['values'] = years
    yearchoosen1.grid(column = 1, row = 5)
    yearchoosen1.current()

    # Year Selection 2 by creating labels, comboboxes & combobox drop down lists
    ttk.Label(op4p2, text = "Select Year 2 :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  
    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(op4p2, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.grid(column = 1, row = 7)
    yearchoosen2.current()

    # Year Selection 3 by creating labels, comboboxes & combobox drop down lists
    ttk.Label(op4p2, text = "Select Year 3 :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 9, padx = 10, pady = 25)  
    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(op4p2, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.grid(column = 1, row = 9)
    yearchoosen3.current()

    # Submit button function to make ComPlot
    def clickop4p2():
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        yearSelections = [year1, year2, year3]

        makeComPlot(yearSelections,'WindSpeed')

    #Adding submit & exit buttons
    Button(op4p2,text="Submit", width=6, command=clickop4p2) .grid(row=10,column=1,sticky=W)
    Button(op4p2,text="Quit", width=6, command=op4p2.destroy) .grid(row=10,column=2,sticky=W)

    op4p2.mainloop()


# Option 5.2 Function
def op5p2 ():

    # Creating the layout
    op5p2 = Tk()
    op5p2.title("Comparing Yearly Pressure (Hg)")
    op5p2.geometry('500x320')
    op5p2.configure(background="grey")

    ttk.Label(op5p2, text = "Comparing Yearly Pressure (Hg)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)

    # Year Selection 1 by creating labels, comboboxes & combobox drop down lists
    ttk.Label(op5p2, text = "Select Year 1 :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)     
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(op5p2, width = 27, textvariable = n)
    yearchoosen1['values'] = years
    yearchoosen1.grid(column = 1, row = 5)
    yearchoosen1.current()

    # Year Selection 2 by creating labels, comboboxes & combobox drop down lists
    ttk.Label(op5p2, text = "Select Year 2 :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  
    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(op5p2, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.grid(column = 1, row = 7)
    yearchoosen2.current()

    # Year Selection 3 by creating labels, comboboxes & combobox drop down lists
    ttk.Label(op5p2, text = "Select Year 3 :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 9, padx = 10, pady = 25)  
    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(op5p2, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.grid(column = 1, row = 9)
    yearchoosen3.current()

    # Submit button function to make ComPlot
    def clickop5p2():
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        yearSelections = [year1, year2, year3]

        makeComPlot(yearSelections,'Pressure')

    #Adding submit & exit buttons
    Button(op5p2,text="Submit", width=6, command=clickop5p2) .grid(row=10,column=1,sticky=W)
    Button(op5p2,text="Quit", width=6, command=op5p2.destroy) .grid(row=10,column=2,sticky=W)

    op5p2.mainloop()

start.mainloop()