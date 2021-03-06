from unicodedata import decimal
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import csv
import itertools


filename = 'FinallOneCSV.csv'

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
                elif(data_type == 'dew'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[5]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[6]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[7]))
                elif(data_type == 'humidity'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[8]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[9]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[10]))
                elif(data_type == 'wind'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[11]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[12]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[13]))
                elif(data_type == 'pressure'):
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
    


#function for submit button
    def click1():
        year_a = yearchoosen.get()
        value_type = typevalue.get()
        data_type='temperature'
       
        
        makePlot(year_a,data_type,value_type)
        
    def click2():
        year_a = yearchoosen.get()
        value_type = typevalue.get()
        data_type='DewPoint'
       
        
        makePlot(year_a,data_type,value_type)




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
