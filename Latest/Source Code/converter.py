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

euro = 0

lastPrice = 0

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
                euro = j_obj['rates']['USD']

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
            lastPrice = float(j_obj[what]['rate_float'])
            print(lastPrice)
            
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
        main()
        
    btn1 = ttk.Button(root, text="Agree", command=run)
    btn1.pack()
    btn2 = ttk.Button(root, text="Disagree", command=quiter)
    btn2.pack()
    root.mainloop()

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
        filemenu.add_command(label="About", command=about)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quiter)
        menubar.add_cascade(label="File",menu=filemenu)

        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (StartPage, PageOne):
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

        btn1 = ttk.Button(self, text="Currency Converter", command=lambda: controller.show_frame(PageOne))
        btn1.pack()

        btn2 = ttk.Button(self, text="Science Converter", command=lambda: popupmsg("Not Supported Yet"))
        btn2.pack()

        btn3 = ttk.Button(self, text="Weight Converter", command=lambda: popupmsg("Not Supported Yet"))
        btn3.pack()

        btn4 = ttk.Button(self, text="Temperature Converter", command=lambda: popupmsg("Not Supported Yet"))
        btn4.pack()

        btn5 = ttk.Button(self, text="Quit", command=quiter)
        btn5.pack()
        
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

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
    def converted(self):
        if self.combVar.get() == self.combVar2.get():
            popupmsg("Choose two different values")
        elif self.combVar.get() == "USD" and self.combVar2.get() == "Bitcoin(s)":
            bicoin_amt("USD")
            euro_amt()
            label = ttk.Label(self, text="", font=SMALL_FONT)
            label2 = ttk.Label(self, text="", font=SMALL_FONT)
            total = float(self.amt.get()) / float(lastPrice)
            label['text'] = str(total)
            label2['text'] = " Bicoin(s)"
            #label = ttk.Label(self, text=str(total), font=SMALL_FONT)
            label.grid(column=8, row=2)
            #label2 = ttk.Label(self, text=" Bicoin(s)", font=SMALL_FONT)
            label2.grid(column=9, row=2)
            self.update()
        elif self.combVar.get() == "Bitcoin(s)" and self.combVar2.get() == "USD":
            bicoin_amt("USD")
            label = ttk.Label(self, text="", font=SMALL_FONT)
            label2 = ttk.Label(self, text="", font=SMALL_FONT)
            total = float(self.amt.get()) * float(lastPrice)
            label['text'] = str(total)
            label2['text'] = " USD"
            #label = ttk.Label(self, text=str(total), font=SMALL_FONT)
            label.grid(column=8, row=2)
            #label2 = ttk.Label(self, text=" USD", font=SMALL_FONT)
            label2.grid(column=9, row=2)
            self.update()
        elif self.combVar.get() == "Euro(s)" and self.combVar2.get() == "USD":
            euro_amt()
            total = euro * float(self.amt.get())
            label = ttk.Label(self, text="", font=SMALL_FONT)
            label2 = ttk.Label(self, text="", font=SMALL_FONT)
            label = ttk.Label(self, text=str(total), font=SMALL_FONT)
            label.grid(column=8, row=2)
            label2 = ttk.Label(self, text=" USD", font=SMALL_FONT)
            label2.grid(column=9, row=2)
            self.update()
        elif self.combVar.get() == "USD" and self.combVar2.get() == "Euro(s)":
            euro_amt()
            total = float(self.amt.get()) / euro
            label = ttk.Label(self, text="", font=SMALL_FONT)
            label2 = ttk.Label(self, text="", font=SMALL_FONT)
            label = ttk.Label(self, text=str(total), font=SMALL_FONT)
            label.grid(column=8, row=2)
            label2 = ttk.Label(self, text=" Euro(s)", font=SMALL_FONT)
            label2.grid(column=9, row=2)
            self.update()
        elif self.combVar.get() == "Euro(s)" and self.combVar2.get() == "Bitcoin(s)":
            bicoin_amt("EUR")
            total = (float(self.amt.get())) / float(lastPrice)
            label = ttk.Label(self, text="", font=SMALL_FONT)
            label2 = ttk.Label(self, text="", font=SMALL_FONT)
            label = ttk.Label(self, text=str(total), font=SMALL_FONT)
            label.grid(column=8, row=2)
            label2 = ttk.Label(self, text=" Bitcoin(s)", font=SMALL_FONT)
            label2.grid(column=9, row=2)
            self.update()
        elif self.combVar.get() == "Bitcoin(s)" and self.combVar2.get() == "Euro(s)":
            bicoin_amt("EUR")
            total = (float(self.amt.get())) * float(lastPrice)
            label = ttk.Label(self, text="", font=SMALL_FONT)
            label2 = ttk.Label(self, text="", font=SMALL_FONT)
            label = ttk.Label(self, text=str(total), font=SMALL_FONT)
            label.grid(column=8, row=2)
            label2 = ttk.Label(self, text=" Euro(s)", font=SMALL_FONT)
            label2.grid(column=9, row=2)
            self.update()
        else:
            popupmsg("Not Supported Yet")
        
def main():
    app = Converter()
    app.geometry("650x300")
    app.mainloop()

alert()
