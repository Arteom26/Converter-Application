import PageOne
from PageOne import *

import PageFour
from PageFour import *

import functions
from functions import *

import tkinter as tk
from tkinter import ttk

import threading
from queue import Queue
import time

import urllib.request
import json

import sys

LARGE_FONT = ("Verdana", 20)
MED_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 8)

euro = 0

lastPrice = 0

def quiter():
    sys.exit(1)

class Converter(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="icon.ico")
        tk.Tk.wm_title(self, "Converter")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="About", command=functions.about)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quiter)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Tutorial", command=functions.tutorial)
        menubar.add_cascade(label="Help", menu=helpmenu)

        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (StartPage, PageOne.PageOne, PageTwo, PageThree, PageFour):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Welcome to the Amazing Converter", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        btn1 = ttk.Button(self, text="Currency Converter", command=lambda: controller.show_frame(PageOne.PageOne))
        btn1.pack()

        btn2 = ttk.Button(self, text="Science Converter", command=lambda: controller.show_frame(PageTwo))
        btn2.pack()

        btn3 = ttk.Button(self, text="Weight Converter", command=lambda: controller.show_frame(PageThree))
        btn3.pack()

        btn4 = ttk.Button(self, text="Temperature Converter", command=lambda: controller.show_frame(PageFour))
        btn4.pack()

        btn5 = ttk.Button(self, text="Quit", command=quiter)
        btn5.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Comming Soon", font=MED_FONT)
        label.pack()

        btn1 = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        btn1.pack()

class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Comming Soon", font=MED_FONT)
        label.pack()

        btn1 = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        btn1.pack()

def main():
    app = Converter()
    app.geometry("650x300")
    app.mainloop()

if __name__ == '__main__':
    alert()
