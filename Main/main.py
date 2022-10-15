# from Class.Car import Car
from Class.DB import DBAccess as DB
from Class.Car import Car
from tkinter import *
import tkinter as tk
import tkinter.font as font
import sys

class Application:
    def __init__(self): 
        self.police = "corbel 15"
        self.title = "Bamboo Concess"
        self.main()

    def ShowStock(self, frameResults):
        for widget in frameResults.winfo_children(): 
            widget.destroy()
        carList = Car.CarListStock()
        listboxStock = tk.Listbox(frameResults)
        listboxStock.pack(expand = True, fill = "both")
        for car in carList:
            listboxStock.insert(END, "Prix : {}. Type : {}. Motor : {}. Brand : {}. Promotion : {}. In stock since : {}. Next Control : {}" \
                .format(car.prixCar, car.nameType, car.nameMotor, car.nameBrand, car.promoCar, car.dateStockCar, car.dateTechControlCar))
                
    def ShowHistory(self, frameResults):
        self.ShowStock(frameResults)

    def MakeReservation(self):
        pass

    def MakeDeal(self):
        pass

    def AddCar(self):
        pass

    def main(self):

        window = tk.Tk()
        window.title(self.title)
        window.attributes('-fullscreen', True)
        window.option_add("*Font", self.police)

        window.columnconfigure(0, weight = 2)
        window.columnconfigure(1, weight = 3)
        window.columnconfigure(2, weight = 1)
        window.columnconfigure(3, weight = 1)

        for i in range(6):
            window.rowconfigure(i, weight = 1)
        window.rowconfigure(7, weight = 2)

        frameButtons = tk.Frame(window, highlightthickness=2, highlightbackground = "black")
        frameButtons.grid(column = 0, row = 1, rowspan = 5, sticky = "wesn")
        for i in range(5):
            frameButtons.rowconfigure(i, weight = 1)
        frameButtons.columnconfigure(0, weight = 1)

        buttonStock = tk.Button(frameButtons, text = "Display Stock", command = lambda : self.ShowStock(frameDisplay), state = "disabled")
        buttonStock.grid(column = 0, row = 0, sticky = "wesn")
        buttonHistory = tk.Button(frameButtons, text = "Display History", command = lambda : self.ShowHistory(frameDisplay))
        buttonHistory.grid(column = 0, row = 1, sticky = "wesn")
        buttonReservation = tk.Button(frameButtons, text = "Make a reservation", command = self.MakeReservation)
        buttonReservation.grid(column = 0, row = 2, sticky = "wesn")
        buttonDeal = tk.Button(frameButtons, text = "Make a deal", command = self.MakeDeal)
        buttonDeal.grid(column = 0, row = 3, sticky = "wesn")
        buttonAddCar = tk.Button(frameButtons, text = "Add a car", command = self.AddCar)
        buttonAddCar.grid(column = 0, row = 4, sticky = "wesn")


        frameTitle = tk.Frame(window, highlightthickness=2, highlightbackground = "yellow")
        frameTitle.grid(column = 1, row = 0, sticky = "wesn")
        labelTitle = tk.Label(frameTitle, text = self.title)
        labelTitle.pack()

        frameSort = tk.Frame(window, highlightthickness = 2, highlightbackground = "blue")
        frameSort.grid(column = 1, row = 1, sticky = "wesn")

        frameDisplay = tk.Frame(window, highlightthickness=2, highlightbackground = "pink")
        frameDisplay.grid(column = 1, row = 2, rowspan=6, sticky="wesn")

        frameOnClick = tk.Frame(window, highlightthickness=2, highlightbackground = "purple")
        frameOnClick.grid(column = 2, row = 1, rowspan = 7, columnspan = 2, sticky ="wesn")

        frameExit = tk.Frame(window)
        frameExit.grid(column = 2, row = 0, columnspan = 2, sticky = "wesn")
        frameExit.rowconfigure(0, weight = 1)
        frameExit.columnconfigure(0, weight = 1)
        buttonExit = tk.Button(frameExit, text = "Exit", command = window.destroy, relief='raised', font=font.Font(family='Helvetica', size=15, weight='bold'))
        buttonExit.grid(column = 0, row = 0, sticky = "wesn")

        self.ShowStock(frameDisplay)

        window.mainloop()

Application()