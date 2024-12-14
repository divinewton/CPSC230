import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

MatData = pd.read_csv('MatTesting.csv')  # reads MatTesting.csv file within current directory
type(MatData)

def BoxPlot(): # function for the boxplot
   sns.boxplot(data = MatData, 
      x = 'shape', 
      y = 'MaxIndex', 
      hue = 'cycle')
   plt.show(block=False)

def Scatter(): # function for the scatter plot
    plt.scatter(MatData['cycle'], MatData['MaxLoad'], c ="red")
    plt.show(block=False)

def RelPlot(): # function for the relplot
    sns.relplot(data = MatData, 
        x = 'shape', 
        y = 'MaxExt', 
        hue = 'spacing')
    plt.show(block=False)

layout = [[sg.Button('BoxPlot'), sg.Button('Scatter'), sg.Button('RelPlot'), sg.Button('Quit')]] # sets layout with 4 buttons

window = sg.Window('Choose your Plot', layout) # defines the window with the layout in it

while True: # while loop to show window
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':  # if quit, breaks the loop
        break
    elif event == 'BoxPlot': # if boxplot, runs that function
        BoxPlot()
    elif event == 'Scatter': # if scatter, runs that function
        Scatter()
    elif event == 'RelPlot': # if relplot, runs that function
        RelPlot()
window.close() # closes the window