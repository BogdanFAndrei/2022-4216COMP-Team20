#import csv file
#import matplotlib.pyplot as plt

import csv

filename = 'FinallOneCSV.csv'

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    tempmin = []
    counter = 12
    rowCounter = 1
    for row in datareader:
        rowCounter=rowCounter+1 
        if (row[0] == 'Average '):
            tempmin.append(row[2])
            counter= counter-1
            print (tempmin)    
        if (counter== 1):
            break
#Time2020=['January','February','asdad','dadas' ,'dasds','dasddsas','dasfdas','dasdahs','dasdtas','dasdeqas','dastdas','dauksdas']
#Temperature= [tempmin]
#plt.plot(Time2020,tempmin)
#plt.title('Temperature 2020')
#plt.xlabel('Time2020')
#plt.ylabel('Temperature')
#plt.show()


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
    MyLabel=Label(window, text="Look! I clicked on a Button!!")
    MyLabel.pack
#addbutton 
Button(window,text="Submit", width=6, command=click) .grid(row=8,column=1,sticky=W)

#add exit button
Button(window,text="Quit", width=6, command=window.destroy) .grid(row=8,column=2,sticky=W)



window.mainloop()
