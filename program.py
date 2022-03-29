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
   
def maketwoPlots( year_a, year_b, data_type, value_type):

    year_a_data = getYearData(year_a, data_type, value_type)
    year_b_data = getYearData(year_b, data_type, value_type)

    month_labels =['January','February','March','April' ,'May','June','July','August','September','October','November','December']
    plt.figure(figsize=(12,5))

    plt.plot(month_labels,year_a_data, '-ok',color='green',linestyle='dashed',markerfacecolor='green')
    plt.plot(month_labels,year_b_data, '-ok',color='blue',linestyle='dashed',markerfacecolor='blue')
    plt.grid(axis= 'y')
    plt.title(str(year_a) + " - " + str(year_b))
    plt.xlabel('Month')
    plt.ylabel(data_type + " " + value_type)
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
    

    btn1 = Button(mai,text="Temperature (Degrees F)", width=20, command=op1)
    btn1.place(x=10, y=100)
   
    #Option 2
  

    btn2 = Button(mai,text="Drew Point (Degrees F)", width=20, command=op2)
    btn2.place(x=10, y=150)

    #Option 3
  
    btn3 =Button(mai,text="Humidity (%)", width=20, command=op3)
    btn3.place(x=10, y=200)

    #Option 4
    

    ml5 = ttk.Label(mai, text = "One Year",
          background = 'black', foreground ="white",
          font = ("Times New Roman", 15))      
    ml5.place(x=50, y=50)
   
    ml5 = ttk.Label(mai, text = "Two Years",
          background = 'black', foreground ="white",
          font = ("Times New Roman", 15))      
    ml5.place(x=200, y=50)

    
    ml5 = ttk.Label(mai, text = "Three years",
          background = 'black', foreground ="white",
          font = ("Times New Roman", 15))      
    ml5.place(x=380, y=50)

    btn4 = Button(mai,text="Wind Speed (mph)", width=20, command=op4)
    btn4.place(x=10, y=250)

    btn6 = Button(mai,text="Temperature", width=20, command=TempComp)
    btn6.place(x=180, y=100)

    btn7 = Button(mai,text="Dew Point", width=20, command=DewComp)
    btn7.place(x=180, y=150)

    btn8 = Button(mai,text="Humidity (%)", width=20, command=HumidityComp)
    btn8.place(x=180, y=200)

    btn9 = Button(mai,text="Wind Speed", width=20, command=WindComp)
    btn9.place(x=180, y=250)

    btn10 = Button(mai,text="Temperature (Degrees F)", width=20, command=op1p2)
    btn10.place(x=350, y=100)
    
    #Option 2

    btn11 = Button(mai,text="Drew Point (Degrees F)", width=20, command=op2p2)
    btn11.place(x=350, y=150)
    #Option 3


    btn12 =Button(mai,text="Humidity (%)", width=20, command=op3p2)
    btn12.place(x=350, y=200)
    #Option 4
    
    btn13 = Button(mai,text="Wind Speed (mph)", width=20, command=op4p2)
    btn13.place(x=350, y=250)
    #Option 5
    
  



    



#Adding Function for start Button
bntStart1 = Button(start,text="Click to start", width=15, command=main)
bntStart1.place(x=180, y=285)

#Option 1 Function
def op1 ():
    op1 = Tk()
    op1.title("Temperature (Degrees F)")
    op1.geometry('500x320')
    op1.configure(background="grey")

    ttk.Label(op1, text = "Temperature (Degrees F)",
          background = 'black', foreground ="white",
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)

# label max/average/min
    ttk.Label(op1, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    yearchoosen = ttk.Combobox(op1, width = 27, textvariable = n)

# Adding combobox drop down list
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



# label year
    ttk.Label(op1, text = "Select the value :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    typevalue = ttk.Combobox(op1, width = 27, textvariable = n)

# Adding combobox drop down list
    typevalue['values'] = ('Minimum',
                          'Average',
                          'Maximum')
    typevalue.grid(column = 1, row = 7)
    typevalue.current()

#Submitbutton function +++++ Function for finding data
    def click():
        year_a = yearchoosen.get()
        value_type = typevalue.get()
        data_type='temperature'
       
       
        makePlot(year_a,data_type,value_type)

#addbutton
    Button(op1,text="Submit", width=6, command=click) .grid(row=8,column=1,sticky=W)

#add exit button
    Button(op1,text="Quit", width=6, command=op1.destroy) .grid(row=8,column=2,sticky=W)

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

# label max/average/min
    ttk.Label(op2, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    yearchoosen = ttk.Combobox(op2, width = 27, textvariable = n)

# Adding combobox drop down list
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



# label year
    ttk.Label(op2, text = "Select the value :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    typevalue = ttk.Combobox(op2, width = 27, textvariable = n)

# Adding combobox drop down list
    typevalue['values'] = ('Minimum',
                          ' Average',
                          'Maximum')
    typevalue.grid(column = 1, row = 7)
    typevalue.current()

#Submitbutton function
    def click2():
        year_a = yearchoosen.get()
        value_type = typevalue.get()
        data_type='DewPoint'
       
       
        makePlot(year_a,data_type,value_type)

#addbutton
    Button(op2,text="Submit", width=6, command=click2) .grid(row=8,column=1,sticky=W)

#add exit button
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

# label max/average/min
    ttk.Label(op3, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    yearchoosen = ttk.Combobox(op3, width = 27, textvariable = n)

# Adding combobox drop down list
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



# label year
    ttk.Label(op3, text = "Select the value :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    typevalue = ttk.Combobox(op3, width = 27, textvariable = n)

# Adding combobox drop down list
    typevalue['values'] = ('Minimum',
                          'Average',
                          'Maximum')
    typevalue.grid(column = 1, row = 7)
    typevalue.current()

#Submitbutton function
    def click3():
        year_a = yearchoosen.get()
        value_type = typevalue.get()
        data_type='Humidity'
       
       
        makePlot(year_a,data_type,value_type)

#addbutton
    Button(op3,text="Submit", width=6, command=click3) .grid(row=8,column=1,sticky=W)

#add exit button
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

# label max/average/min
    ttk.Label(op4, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    yearchoosen = ttk.Combobox(op4, width = 27, textvariable = n)

# Adding combobox drop down list
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



# label year
    ttk.Label(op4, text = "Select the value :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    typevalue = ttk.Combobox(op4, width = 27, textvariable = n)

# Adding combobox drop down list
    typevalue['values'] = ('Minimum',
                          'Average',
                          'Maximum')
    typevalue.grid(column = 1, row = 7)
    typevalue.current()

#Submitbutton function
    def click4():
        year_a = yearchoosen.get()
        value_type = typevalue.get()
        data_type='WindSpeed'
       
       
        makePlot(year_a,data_type,value_type)

#addbutton
    Button(op4,text="Submit", width=6, command=click4) .grid(row=8,column=1,sticky=W)

#add exit button
    Button(op4,text="Quit", width=6, command=op4.destroy) .grid(row=8,column=2,sticky=W)
   
    op4.mainloop()

def TempComp ():
    TempComp = Tk()
    TempComp.title("Drew Point (Degrees F)")
    TempComp.geometry('500x320')
    TempComp.configure(background="grey")
def DewComp ():
    DewComp = Tk()
    DewComp.title("Drew Point (Degrees F)")
    DewComp.geometry('500x320')
    DewComp.configure(background="grey")
def HumidityComp ():
    HumidityComp = Tk()
    HumidityComp.title("Drew Point (Degrees F)")
    HumidityComp.geometry('500x320')
    HumidityComp.configure(background="grey")
def WindComp ():
    WindComp = Tk()
    WindComp.title("Drew Point (Degrees F)")
    WindComp.geometry('500x320')
    WindComp.configure(background="grey")

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
