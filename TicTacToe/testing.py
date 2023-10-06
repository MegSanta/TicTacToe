import tkinter as tk
from tkinter import ttk




def hi():
    print(IP.get())

master = tk.Tk()
IP = tk.StringVar()
master.configure(background='red')
'''submitButton = tk.Button(master, text='Submit', anchor='ne').grid(column=0, row=0)
space = tk.Button(master, text='space', anchor='nw').grid(column=1, row=0)'''
master.columnconfigure(0, weight=1)
master.columnconfigure(1, weight=2)
label = tk.Label(master, text='last player').grid(column=0, row=0, sticky=tk.E, padx=10, pady=10)
#Why does this button not work? It does the stuff before I press the button aahhhhhhhhhh
button = tk.Button(master, text='print', command=hi)
button.grid(column=1, row =1, padx=10, pady=10)
#button['state'] = 'disabled'
#label['text'] = 'yay'
#label.grid_remove()

IPEntry = tk.Entry(master, textvariable=IP).grid(row=5, column=3, padx=10, pady=10)


master.mainloop()

