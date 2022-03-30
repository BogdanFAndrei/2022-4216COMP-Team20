# Testing on actual program by using it on the sections already made.
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

# Function to make a single comparison graph. 
def makeComPlot(year, data_type):

    # Getting max, mean and min values to plot
    maxValuesYear = findMaxValueYear(year, data_type)
    meanValuesYear = findMeanValueYear(year, data_type)
    minValuesYear = findMinValueYear(year, data_type)
    
    # Gathering better y axis labels that includes the measurements
    if (data_type=='temperature'):
        ylabel="Temperature (° F)"
    if (data_type=='DewPoint'):
        ylabel="Dew Point (° F)"
    if (data_type=='Humidity'):
        ylabel="Humidity (%)"
    if (data_type=='WindSpeed'):
        ylabel="Wind Speed (mph)"
    if (data_type=='Pressure'):
        ylabel="Pressure (Hg)"

    # Creating a figure and adding a title, y and x labels and a grid
    plt.figure(figsize=(12,5))
    plt.title(f"Comparing the maximum, mean & minimum pressure values of {year[0]}, {year[1]} & {year[2]}")
    plt.ylabel(ylabel)
    plt.xlabel('Years')
    plt.grid(axis= 'y')

    # Adding vertical lines between the points 
    plt.vlines(x=year, ymin=minValuesYear, ymax=[maxValuesYear], colors='black', ls='-', lw=2)

    # Plotting 
    plt.plot(year,maxValuesYear, 'dk',markersize = 10, color='blue',linestyle='',markerfacecolor='blue', label="Maximum")
    plt.plot(year,meanValuesYear, 'sk',markersize = 10, color='magenta',linestyle='',markerfacecolor='magenta', label="Mean")
    plt.plot(year,minValuesYear, 'ok', markersize = 10, color='red',linestyle='',markerfacecolor='red', label="Minimum")

    # Adding a legend
    plt.legend(bbox_to_anchor=(1.1, 1.05))

    plt.show()



#Create Intro Menu
start = Tk()
start.title("Climate and Weather Team 20")
start.geometry('500x350')
start.configure(background="grey")

#Creates Headline for Intro
start1 = ttk.Label(start, text = "Welcome to Weather + Climate", 
          background = 'grey', foreground ="white", 
          font = ("Times New Roman", 15))
start1.place(x = 150, y = 10)

start2 = ttk.Label(start, text = "This system is designed to provide data on the weather and climate in Liverpool." 
+ "\r\n" + 
"This was designed and created by:"
+ "\r\n" +
"Ryan Hacine-Bacha"
+ "\r\n" +
"Bogdan-Florin Andrei"
+ "\r\n" +
"Eoin Boyle"
+ "\r\n" +
"Lukas Holba"
+ "\r\n" +
"Elaine Wong"
+ "\r\n" +
"Xiao Long Qi Andrei"
+ "\r\n" +
"Once you hit the start button you will be able to pick out our many features. ",
          background = 'grey', foreground ="Black", 
          font = ("Times New Roman", 10))
start2.place(x = 40, y = 35)

#Function for start button
def main ():
    mai = Tk()
    mai.title("Main Menu")
    mai.geometry('500x320')
    mai.configure(background="grey")
    start.destroy()

    #Label for Main Menu
    mainlabel = ttk.Label(mai, text = "Main Menu", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15))      
    mainlabel.place(x=200, y=10)


    #Option 1
    ml1 = ttk.Label(mai, text = "Temperature (° F)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15))      
    ml1.place(x=200, y=50)

    btn1 = Button(mai,text="Temperature (° F)", width=20, command=op1p2)
    btn1.place(x=10, y=50)


    #Option 2
    ml2 = ttk.Label(mai, text = "Dew Point (° F)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15))      
    ml2.place(x=200, y=100)

    btn2 = Button(mai,text="Dew Point (° F)", width=20, command=op2p2)
    btn2.place(x=10, y=100)


    #Option 3
    ml3 = ttk.Label(mai, text = "Humidity (%)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15))      
    ml3.place(x=200, y=150)

    btn3 =Button(mai,text="Humidity (%)", width=20, command=op3p2)
    btn3.place(x=10, y=150)


    #Option 4
    ml4 = ttk.Label(mai, text = "Wind Speed (mph)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15))      
    ml4.place(x=200, y=200)
    
    btn4 = Button(mai,text="Wind Speed (mph)", width=20, command=op4p2)
    btn4.place(x=10, y=200)
    
    mai.mainloop()

#Adding Function for start Button
bntStart1 = Button(start,text="Click to start", width=15, command=main)
bntStart1.place(x=180, y=285)


years = ['2009','2010','2011','2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']


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


start.mainloop()