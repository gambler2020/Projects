#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 17:36:16 2022

@author: gambler
"""

from forex_python.converter import CurrencyRates
import tkinter as tk
from tkinter import simpledialog
root=tk.Tk()
root.title("Aziz Money Exchanger")

def Ex_Aziz():
    c=CurrencyRates()
    amount=simpledialog.askfloat(title="Amount: ", prompt="Enter your amount: ")
    from_currency=simpledialog.askstring(title="From Currency: ", prompt="From Currency: ").upper()
    to_currency=simpledialog.askstring(title="To Currency: ", prompt="To Currency: ").upper()
    result=round(c.convert(from_currency, to_currency, amount), 2)
    label.configure(text=str(result))


label=tk.Label(root, width=50, height=10)
button=tk.Button(root, width=50, text="Click here for Exchange Rate", command=Ex_Aziz)

label.grid(row=0, column=1)
button.grid(row=1, column=1)

root.mainloop()

#connect with me on the following platform
#Google Scholar: https://scholar.google.com/citations?user=sblGKgMAAAAJ&hl=en
#ResearchGate: https://www.researchgate.net/profile/Mohammad-Aziz-26
#Linkedin: https://www.linkedin.com/in/mohammad-aziz-uk/