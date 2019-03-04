#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 09:54:51 2019

@author: vla35123
"""

import tkinter as tk
from tkinter import LabelFrame, Radiobutton, Label, Entry, Button, filedialog, messagebox
import pylab as lab


class Application (tk.Tk):
    name = 'Graf funkce'
    
    def __init__ (self):
        super().__init__ (className = self.name)
        self.title(self.name)
        
        ### Frames ###
        self.GrafMatFrame = LabelFrame (self, text = 'Graf matemtické funkce')
        self.GrafMatFrame.pack (anchor = tk.W)
        self.GrafSouFrame = LabelFrame (self, text = 'Graf funkce ze souboru')
        self.GrafSouFrame.pack (anchor = tk.W)
        self.OsyFrame = LabelFrame (self, text = 'Názvy os')
        self.OsyFrame.pack (anchor = tk.W)
        
        ### Matematická funkce ###
        self.funkceVar = tk.StringVar()
        self.funkceVar.set ('sin')
        self.OdVar = tk.StringVar()
        self.OdVar.set ('0')
        self.DoVar = tk.StringVar()
        self.DoVar.set ('0')
        self.SinRad = Radiobutton (self.GrafMatFrame, text = 'Sin', variable = self.funkceVar, value = 'sin')
        self.SinRad.grid(row = 1, column = 1)
        self.LogRad = Radiobutton (self.GrafMatFrame, text = 'Log', variable = self.funkceVar, value = 'log')
        self.LogRad.grid(row = 2, column = 1)
        self.ExpRad = Radiobutton (self.GrafMatFrame, text = 'Exp', variable = self.funkceVar, value = 'exp')
        self.ExpRad.grid(row = 3, column = 1)
        Label (self.GrafMatFrame, text = '          Od:', width = 8).grid(row = 1, column = 3)
        Label (self.GrafMatFrame, text = '          Do:', width = 8).grid(row = 2, column = 3)
        self.OdEnt = Entry (self.GrafMatFrame, textvariable = self.OdVar, width = 10)
        self.OdEnt.grid(row = 1, column = 4)
        self.DoEnt = Entry (self.GrafMatFrame, textvariable = self.DoVar, width = 10)
        self.DoEnt.grid(row = 2, column = 4)
        Button (self.GrafMatFrame, text = 'Vytvořit graf', width = 8, command = self.GrafMat).grid(row = 4, column = 5)
        
        ### Funkce ze souboru ###
        self.SouVar = tk.StringVar()
        self.SouVar.set ('cesta/k/souboru')
        self.SouEnt = Entry (self.GrafSouFrame, textvariable = self.SouVar, width = 25)
        self.SouEnt.grid (row = 2, column = 0)
        Button (self.GrafSouFrame, text = 'Vyber soubor', width = 8, command = self.VyberSoubor).grid(row = 2, column = 2)
        Button (self.GrafSouFrame, text = 'Vytvořit graf', width = 8, command = self.GrafSou).grid(row = 3, column = 2)
        
        ### Názvy osy ###
        self.xvar = tk.StringVar()
        self.xvar.set ('')
        self.yvar = tk.StringVar()
        self.yvar.set ('')
        Label (self.OsyFrame, text = 'osa X'). grid(row = 0, column = 0)
        Label (self.OsyFrame, text = 'osa Y'). grid(row = 1, column = 0)
        self.XEnt = Entry (self.OsyFrame, textvariable = self.xvar, width = 10)
        self.XEnt.grid(row = 0, column = 1)
        self.YEnt = Entry (self.OsyFrame, textvariable = self.yvar, width = 10)
        self.YEnt.grid(row = 1, column = 1)
    def GrafMat(self):
        try:
            od = float (self.OdVar.get())
            do= float (self.DoVar.get())
            x = lab.linspace (od, do, 500)
            if self.funkceVar.get() == 'sin':
                y = lab.sin(x)
            elif self.funkceVar.get() == 'log':
                y = lab.log10(x)
            elif self.funkceVar.get() == 'exp':
                y = lab.exp(x)
            lab.figure()
            lab.plot(x,y)
            lab.xlabel(self.xvar.get())
            lab.ylabel(self.yvar.get())
            lab.grid(True)
            lab.show()
        except:
            messagebox.showerror (title = 'Špatné rozmezí', message = 'Rozmezí os musí být realná čísla')
    def GrafSou(self):
        try:
            cesta = self.SouVar.get()
            f = open (cesta, 'r')
            x = []
            y = []
            while True:
                radek = f.readline()
                if radek == '':
                    break
                else:
                    cisla = radek.split()
                    x.append (float(cisla[0]))
                    y.append (float(cisla[1]))

            f.close()
            lab.figure()
            lab.plot(x,y)
            lab.xlabel(self.xvar.get())
            lab.ylabel(self.yvar.get())
            lab.grid(True)
            lab.show()
        except:
            messagebox.showerror (title = 'Chybný soubor', 
                                  message = 'Graf se nepodařil vykreslit \nZkrontrolujte soubor a jeho formát')
    def VyberSoubor(self):
        self.cesta = filedialog.askopenfilename(title = 'Vyberte soubor')
        if self.cesta != '':
            self.SouVar.set(self.cesta)


app = Application()
app.mainloop()