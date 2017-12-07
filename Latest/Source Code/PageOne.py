import converter
from converter import *

import functions
from functions import *

import tkinter as tk
from tkinter import ttk

import threading
from queue import Queue
import time

import urllib.request
import json

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        functions.bicoin_amt("USD")
        functions.bicoin_amt("EUR")
        functions.euro_amt()

        label = ttk.Label(self, text="Currency Converter", font=SMALL_FONT)
        label.grid(column=1, row=1)

        label1 = ttk.Label(self, text="Convert ", font=SMALL_FONT)
        label1.grid(column=1, row=2)

        self.amt = tk.StringVar()
        self.entry = ttk.Entry(self, textvariable=self.amt, width=5)
        self.entry.insert(0, 1)
        self.entry.grid(column=2, row=2)

        label3 = ttk.Label(self, text="  ", font=SMALL_FONT)
        label3.grid(column=3, row=2)

        self.combVar = tk.StringVar()
        self.comboBox = ttk.Combobox(self, textvariable=self.combVar, width=10)
        self.comboBox.grid(column=4, row=2)
        self.comboBox['values'] = ('USD', 'Bitcoin(s)', 'Euro(s)')
        self.comboBox.current(0)

        label2 = ttk.Label(self, text=" to ")
        label2.grid(column=5, row=2)

        self.combVar2 = tk.StringVar()
        self.comboBox2 = ttk.Combobox(self, textvariable=self.combVar2, width=10)
        self.comboBox2.grid(column=6, row=2)
        self.comboBox2['values'] = ('USD', 'Bitcoin(s)', 'Euro(s)')
        self.comboBox2.current(0)

        btn1 = ttk.Button(self, text="Convert", command=self.converted)
        btn1.grid(column=7, row=2)

        btn2 = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        btn2.grid(column=1, row=3)

        self.l = tk.StringVar()
        self.l2 = tk.StringVar()
        
    def converted(self):
        if self.combVar.get() == self.combVar2.get():
            popupmsg("Choose two different values")
        elif self.combVar.get() == "USD" and self.combVar2.get() == "Bitcoin(s)":
            functions.bicoin_amt("USD")
            functions.euro_amt()
            total = float(self.amt.get()) / float(converter.lastPrice)
            self.l.set(str(total))
            self.l2.set(" Bicoin(s)")
            label = ttk.Label(self, textvariable=self.l, font=SMALL_FONT)
            label2 = ttk.Label(self, textvariable=self.l2, font=SMALL_FONT)
            #label = ttk.Label(self, text=str(total), font=SMALL_FONT)
            label.grid(column=8, row=2)
            #label2 = ttk.Label(self, text=" Bicoin(s)", font=SMALL_FONT)
            label2.grid(column=9, row=2)
        elif self.combVar.get() == "Bitcoin(s)" and self.combVar2.get() == "USD":
            functions.bicoin_amt("USD")
            total = float(self.amt.get()) * float(converter.lastPrice)
            self.l.set(str(total))
            self.l2.set(" USD")
            label = ttk.Label(self, textvariable=self.l, font=SMALL_FONT)
            label2 = ttk.Label(self, textvariable=self.l2, font=SMALL_FONT)
            label.grid(column=8, row=2)
            label2.grid(column=9, row=2)
        elif self.combVar.get() == "Euro(s)" and self.combVar2.get() == "USD":
            functions.euro_amt()
            total = converter.euro * float(self.amt.get())
            self.l.set(str(total))
            self.l2.set(" USD")
            label = ttk.Label(self, textvariable=self.l, font=SMALL_FONT)
            label2 = ttk.Label(self, textvariable=self.l2, font=SMALL_FONT)
            label.grid(column=8, row=2)
            label2.grid(column=9, row=2)
        elif self.combVar.get() == "USD" and self.combVar2.get() == "Euro(s)":
            functions.euro_amt()
            total = float(self.amt.get()) / converter.euro
            self.l.set(str(total))
            self.l2.set(" Euro(s)")
            label = ttk.Label(self, textvariable=self.l, font=SMALL_FONT)
            label2 = ttk.Label(self, textvariable=self.l2, font=SMALL_FONT)
            label.grid(column=8, row=2)
            label2.grid(column=9, row=2)
        elif self.combVar.get() == "Euro(s)" and self.combVar2.get() == "Bitcoin(s)":
            functions.bicoin_amt("EUR")
            total = (float(self.amt.get())) / float(converter.lastPrice)
            self.l.set(str(total))
            self.l2.set(" Bitcoin(s)")
            label = ttk.Label(self, textvariable=self.l, font=SMALL_FONT)
            label2 = ttk.Label(self, textvariable=self.l2, font=SMALL_FONT)
            label.grid(column=8, row=2)
            label2.grid(column=9, row=2)
        elif self.combVar.get() == "Bitcoin(s)" and self.combVar2.get() == "Euro(s)":
            functions.bicoin_amt("EUR")
            total = (float(self.amt.get())) * float(converter.lastPrice)
            self.l.set(str(total))
            self.l2.set(" Euro(s)")
            label = ttk.Label(self, textvariable=self.l, font=SMALL_FONT)
            label2 = ttk.Label(self, textvariable=self.l2, font=SMALL_FONT)
            label.grid(column=8, row=2)
            label2.grid(column=9, row=2)
        else:
            functions.popupmsg("Not Supported Yet")
 
