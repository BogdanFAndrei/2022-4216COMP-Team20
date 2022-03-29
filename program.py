from cProfile import label
import tkinter as tk
from tkinter import *
from tkinter import ttk
from unicodedata import decimal
import csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

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
    ml1.place(x=200, y=100)

    btn1 = Button(mai,text="Temperature (Degrees F)", width=20, command=op1)
    btn1.place(x=10, y=100)
   
    #Option 2
    ml2 = ttk.Label(mai, text = "Drew Point",
          background = 'black', foreground ="white",
          font = ("Times New Roman", 15))      
    ml2.place(x=200, y=150)

    btn2 = Button(mai,text="Drew Point (Degrees F)", width=20, command=op2)
    btn2.place(x=10, y=150)

    #Option 3
    ml3 = ttk.Label(mai, text = "Humidity (%)",
          background = 'black', foreground ="white",
          font = ("Times New Roman", 15))      
    ml3.place(x=200, y=200)

    btn3 =Button(mai,text="Humidity (%)", width=20, command=op3)
    btn3.place(x=10, y=200)

    #Option 4
    ml4 = ttk.Label(mai, text = "Wind Speed (mph)",
          background = 'black', foreground ="white",
          font = ("Times New Roman", 15))      
    ml4.place(x=200, y=250)

    ml5 = ttk.Label(mai, text = "One Year",
          background = 'black', foreground ="white",
          font = ("Times New Roman", 15))      
    ml5.place(x=50, y=50)
   
    ml5 = ttk.Label(mai, text = "Two Years",
          background = 'black', foreground ="white",
          font = ("Times New Roman", 15))      
    ml5.place(x=380, y=50)
    btn4 = Button(mai,text="Wind Speed (mph)", width=20, command=op4)
    btn4.place(x=10, y=250)

    btn6 = Button(mai,text="Temperature", width=20, command=TempComp)
    btn6.place(x=350, y=100)

    btn7 = Button(mai,text="Dew Point", width=20, command=DewComp)
    btn7.place(x=350, y=150)

    btn8 = Button(mai,text="Humidity (%)", width=20, command=HumidityComp)
    btn8.place(x=350, y=200)

    btn9 = Button(mai,text="Wind Speed", width=20, command=WindComp)
    btn9.place(x=350, y=250)

    



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
start.mainloop()
