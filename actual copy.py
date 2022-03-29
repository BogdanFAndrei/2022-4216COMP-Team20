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
def makePlot( year_a, data_type, value_type):

    year_a_data = getYearData(year_a, data_type, value_type)
    

    month_labels =['January','February','March','April' ,'May','June','July','August','September','October','November','December']
    plt.figure(figsize=(12,5))

    plt.plot(month_labels,year_a_data, '-ok',color='green',linestyle='dashed',markerfacecolor='green')
    plt.grid(axis= 'y')
    plt.title(str(year_a))
    plt.xlabel('Month')
    plt.ylabel(data_type + " " + value_type)
    plt.show()
    
    # Max temp of the year
    # Max temp of the year
def findMaxValueYear(year_a, data_type):
    maxValueYear=[]
    for year in year_a:

        value_type = 'Maximum'

        year_a_data=getYearData(year, data_type, value_type)

        maxValueYear.append(max(year_a_data))
        print(maxValueYear)

    return maxValueYear

def findMeanValueYear(year_a, data_type):
    meanValueYear=[]
    for year in year_a:
        print(year)
        value_type = 'Average'

        year_a_data=getYearData(year, data_type, value_type)
        print(year_a_data)

        meanValueYear.append(statistics.mean(year_a_data))

    return meanValueYear


# When you insert a year, data type and value type, itll findthe max for u
def findMinValueYear(year_a, data_type):
    minValueYear=[]
    for year in year_a:
        print(year)
        value_type = 'Minimum'

        year_a_data=getYearData(year, data_type, value_type)
        print(year_a_data)

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
    ml1 = ttk.Label(mai, text = "Temperature", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15))      
    ml1.place(x=200, y=50)

    btn1 = Button(mai,text="Temperature (Degrees F)", width=20, command=op1)
    btn1.place(x=10, y=50)
    #Option 2
    ml2 = ttk.Label(mai, text = "Drew Point", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15))      
    ml2.place(x=200, y=100)

    btn2 = Button(mai,text="Drew Point (Degrees F)", width=20, command=op2)
    btn2.place(x=10, y=100)
    #Option 3
    ml3 = ttk.Label(mai, text = "Humidity (%)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15))      
    ml3.place(x=200, y=150)

    btn3 =Button(mai,text="Humidity (%)", width=20, command=op3)
    btn3.place(x=10, y=150)
    #Option 4
    ml4 = ttk.Label(mai, text = "Wind Speed (mph)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15))      
    ml4.place(x=200, y=200)
    
    btn4 = Button(mai,text="Wind Speed (mph)", width=20, command=op4)
    btn4.place(x=10, y=200)
    #Option 5
    ml5 = ttk.Label(mai, text = "Pressure (Hg)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15))      
    ml5.place(x=200, y=250)
    
    btn5 = Button(mai,text="Pressure (Hg)", width=20, command=op5)
    btn5.place(x=10, y=250)
    
    mai.mainloop()

#Adding Function for start Button
bntStart1 = Button(start,text="Click to start", width=15, command=main)
bntStart1.place(x=180, y=285)
years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
def op1 ():
    op1 = Tk()
    op1.title("Temperature (Degrees F)")
    op1.geometry('500x320')
    op1.configure(background="grey")

    ttk.Label(op1, text = "Temperature (Degrees F)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)


    #1
    ttk.Label(op1, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)  
    # Combobox creation
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(op1, width = 27, textvariable = n)
    # Adding combobox drop down list
    yearchoosen1['values'] = years
    yearchoosen1.grid(column = 1, row = 5)
    yearchoosen1.current()

    #2
    ttk.Label(op1, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  
    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(op1, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.grid(column = 1, row = 7)
    yearchoosen2.current()

    #3
    ttk.Label(op1, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 9, padx = 10, pady = 25)  
    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(op1, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.grid(column = 1, row = 9)
    yearchoosen3.current()

    def click():
        data_type='temperature'
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        years = [year1, year2, year3]

        makeComPlot(years,'temperature')

    #addbutton 
    Button(op1,text="Submit", width=6, command=click) .grid(row=10,column=1,sticky=W)

    #add exit button
    Button(op1,text="Quit", width=6, command=op1.destroy) .grid(row=10,column=2,sticky=W)

    op1.mainloop()

#Option 2 Function
def op2 ():
    op2 = Tk()
    op2.title("Drew Point (Degrees F)")
    op2.geometry('500x320')
    op2.configure(background="grey")

    ttk.Label(op2, text = "Drew Point (Degrees F)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 2)

    ttk.Label(op2, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)  

    n = tk.StringVar()
    yearchoosen = ttk.Combobox(op2, width = 27, textvariable = n)

    yearchoosen['values'] = ('2013',
                         '2014',
                         '2015',
                          '2016',
                          '2017',
                          '2018',
                          '2019',
                          '2020')
    yearchoosen.grid(column = 1, row = 5)
    yearchoosen.current()

    ttk.Label(op2, text = "Select the value :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  

    n = tk.StringVar()
    typevalue = ttk.Combobox(op2, width = 27, textvariable = n)

    typevalue['values'] = ('Minimum', 
                          ' Average',
                          'Maximum')
    typevalue.grid(column = 1, row = 7)
    typevalue.current()

    def click2():
        year_a = yearchoosen.get()
        value_type = typevalue.get()
        data_type='DewPoint'
       
        makePlot(year_a,data_type,value_type)
    Button(op2,text="Submit", width=6, command=click2) .grid(row=8,column=1,sticky=W)
    Button(op2,text="Quit", width=6, command=op2.destroy) .grid(row=8,column=2,sticky=W)

    op2.mainloop()

#Option 3 Function
def op3 ():
    op3 = Tk()
    op3.title("Humidity (%)")
    op3.geometry('500x320')
    op3.configure(background="grey")
    ttk.Label(op3, text = "Humidity (%)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 3)

    ttk.Label(op3, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)  

    n = tk.StringVar()
    yearchoosen = ttk.Combobox(op3, width = 27, textvariable = n)
    yearchoosen['values'] = ('2013',
                         '2014',
                         '2015',
                          '2016',
                          '2017',
                          '2018',
                          '2019',
                          '2020')
    yearchoosen.grid(column = 1, row = 5)
    yearchoosen.current()

    ttk.Label(op3, text = "Select the value :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  

    n = tk.StringVar()
    typevalue = ttk.Combobox(op3, width = 27, textvariable = n)

    typevalue['values'] = ('Minimum', 
                          'Average',
                          'Maximum')
    typevalue.grid(column = 1, row = 7)
    typevalue.current()

    def click3():
        year_a = yearchoosen.get()
        value_type = typevalue.get()
        data_type='Humidity'
       
        makePlot(year_a,data_type,value_type)

    Button(op3,text="Submit", width=6, command=click3) .grid(row=8,column=1,sticky=W)
    Button(op3,text="Quit", width=6, command=op3.destroy) .grid(row=8,column=2,sticky=W)
    
    op3.mainloop()

#Option 4 Function
def op4 ():
    op4 = Tk()
    op4.title("Wind Speed (mph)")
    op4.geometry('500x320')
    op4.configure(background="grey")

    ttk.Label(op4, text = "Wind Speed (mph)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 4)
    ttk.Label(op4, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)  
    n = tk.StringVar()
    yearchoosen = ttk.Combobox(op4, width = 27, textvariable = n)
    yearchoosen['values'] = ('2013',
                         '2014',
                         '2015',
                          '2016',
                          '2017',
                          '2018',
                          '2019',
                          '2020')
    yearchoosen.grid(column = 1, row = 5)
    yearchoosen.current()
    ttk.Label(op4, text = "Select the value :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  

    n = tk.StringVar()
    typevalue = ttk.Combobox(op4, width = 27, textvariable = n)

    typevalue['values'] = ('Minimum', 
                          'Average',
                          'Maximum')
    typevalue.grid(column = 1, row = 7)
    typevalue.current()

    def click4():
        year_a = yearchoosen.get()
        value_type = typevalue.get()
        data_type='WindSpeed'
       
        makePlot(year_a,data_type,value_type)

    Button(op4,text="Submit", width=6, command=click4) .grid(row=8,column=1,sticky=W)

    Button(op4,text="Quit", width=6, command=op4.destroy) .grid(row=8,column=2,sticky=W)
    
    op4.mainloop()

#Option 1 Function
def op5 ():
    op5 = Tk()
    op5.title("Pressure (Hg)")
    op5.geometry('500x320')
    op5.configure(background="grey")

    ttk.Label(op5, text = "Pressure (Hg)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 5)

    ttk.Label(op5, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)  

    n = tk.StringVar()
    yearchoosen = ttk.Combobox(op5, width = 27, textvariable = n)

    yearchoosen['values'] = ('2013',
                         '2014',
                         '2015',
                          '2016',
                          '2017',
                          '2018',
                          '2019',
                          '2020')
    yearchoosen.grid(column = 1, row = 5)
    yearchoosen.current()

    ttk.Label(op5, text = "Select the value :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  

    n = tk.StringVar()
    typevalue = ttk.Combobox(op5, width = 27, textvariable = n)

    typevalue['values'] = ('Minimum', 
                          'Average',
                          'Maximum')
    typevalue.grid(column = 1, row = 7)
    typevalue.current()

    #Submitbutton function
    def click5():
        year_a = yearchoosen.get()
        value_type = typevalue.get()
        data_type='Pressure'
       
        
        makePlot(year_a,data_type,value_type)

    Button(op5,text="Submit", width=6, command=click5) .grid(row=8,column=1,sticky=W)

    Button(op5,text="Quit", width=6, command=op5.destroy) .grid(row=8,column=2,sticky=W)
    
    op5.mainloop()

start.mainloop()