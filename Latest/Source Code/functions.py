import converter

import tkinter as tk
from tkinter import ttk

import threading
from queue import Queue
import time

import urllib.request
import json

LARGE_FONT = ("Verdana", 20)
MED_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 8)

def about():
    root = tk.Tk()
    label = ttk.Label(root, text="This program was coded by Arteom Katkov\n", font=MED_FONT)
    label = ttk.Label(root, text="Thanks to fixer.io for euro price\n", font=MED_FONT)
    label = ttk.Label(root, text="Thanks to coindesk.com for bicoin price\n", font=MED_FONT)
    label.pack()
    root.mainloop()

def quiter():
    quit()

def popupmsg(what):
    root = tk.Tk()
    label = ttk.Label(root, text=what, font=MED_FONT)
    label.pack()
    root.mainloop()

def euro_amt():
    try:
        def callback():
            global euro
            while True:
                amt = urllib.request.urlopen('https://api.fixer.io/latest')
                amt = amt.read().decode("utf-8")
                j_obj = json.loads(amt)
                converter.euro = j_obj['rates']['USD']

        t = threading.Thread(target=callback)
        t.daemon = True
        t.start()
    except Exception as e:
        print(e)
        root = tk.Tk()
        label = ttk.Label(root, text="Error", font=LARGE_FONT)
        label.pack()
        root.mainloop()

def bicoin_amt(what):
    try:
        global lastPrice
        def callback():
            global lastPrice
            amt = urllib.request.urlopen('https://api.coindesk.com/v1/bpi/currentprice.json')
            amt = amt.read().decode("utf-8")
            j_obj = json.loads(amt)
            j_obj = j_obj['bpi']
            converter.lastPrice = float(j_obj[what]['rate_float'])
            
        q = Queue()
        t = threading.Thread(target=callback)
        t.daemon = True
        t.start()
        
    except Exception as e:
        print(e)
        root = tk.Tk()
        label = ttk.Label(root, text="Error", font=LARGE_FONT)
        label.pack()
        root.mainloop()

def quiter():
    quit()

def alert():
    root = tk.Tk()
    label = ttk.Label(root, text="Warning! This program is in beta. I am NOT resposible for any damage")
    label.pack()
    def run():
        root.destroy()
        converter.main()
        
    btn1 = ttk.Button(root, text="Agree", command=run)
    btn1.pack()
    btn2 = ttk.Button(root, text="Disagree", command=quiter)
    btn2.pack()
    root.mainloop()

def tutorial():
    def leavemini(what):
        what.destroy()

    def page2():
        tut.destroy()
        tut2 = tk.Tk()

        def page3():
            tut2.destroy()
            tut3 = tk.Tk()

            tut3.wm_title("Part 3")
            label = ttk.Label(tut3, text="Part 3", font=MED_FONT)
            label.pack(side="top", fill="x", pady=10)
            label2 = ttk.Label(tut3, text="Then from the combo box choose your unit!", font=MED_FONT)
            label2.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(tut3, text="Done", command=tut3.destroy)
            B1.pack()
            tut3.mainloop()

        tut2.wm_title("Part 2")
        label = ttk.Label(tut2, text="Part 2", font=MED_FONT)
        label.pack(side="top", fill="x", pady=10)
        label2 = ttk.Label(tut2, text="Choose catagory the unit you want to convert to is in", font=MED_FONT)
        label2.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(tut2, text="Next", command=page3)
        B1.pack()
        tut2.mainloop()

    tut = tk.Tk()
    tut.wm_title("Tutorial")
    label = ttk.Label(tut, text="Welcome to the help menu tutorial", font=MED_FONT)
    label.pack(side="top", fill="x", pady=10)

    B1 = ttk.Button(tut, text="Simple Instructions", command=page2)
    B1.pack()
    B2 = ttk.Button(tut, text="Advanced(Part One)", command=lambda: popupmsg("Not yet completed"))
    B2.pack()
    B3 = ttk.Button(tut, text="Advanced(Part Two)", command=lambda: popupmsg("Not yet completed"))
    B3.pack()
    tut.mainloop()
