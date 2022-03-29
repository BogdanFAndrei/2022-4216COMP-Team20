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
    # Max temp of the year
def findMaxValueYear(year_a, data_type):
    maxValueYear=[]
    for year in year_a:
        print(year)
        value_type = 'Maximum'
        year_a_data=getYearData(year, data_type, value_type)
        print(year_a_data)
        maxValueYear.append(max(year_a_data))
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

# before setting maxValues array and years array to something    
def plotMaxValueCom(maxValues, years):
    plt.plot(years,maxValues, '-ok',color='green',linestyle='',markerfacecolor='green')
# before setting meanValues and years to something    
def plotMeanValueCom(meanValues, years):
    plt.plot(years,meanValues, '-ok',color='red',linestyle='',markerfacecolor='red')
# before setting minValues and years to something    
def plotMinValueCom(minValues, years):
    plt.plot(years,minValues, '-ok',color='yellow',linestyle='',markerfacecolor='yellow')

years = ['2014', '2015']
print(findMaxValueYear('2010', 'temperature'))
print(findMaxValueYear('2016', 'temperature'))
makeComPlot(years, 'temperature')



