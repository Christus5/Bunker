# -*- coding: utf-8 -*-
import tkinter as tk

class Window():
    def __init__(self):
        self.window = tk.Tk()
        self.inputText = tk.Label(text="Enter player count:")
        self.userInput = tk.Entry(width=100)
        
        self.inputText.pack()
        self.userInput.pack()
        
        self.window.mainloop()
        
        self.playerCount = self.userInput.get()
    

    def __del__(self):
        self.window.destroy()        

    def getPlayerCount():
        return self.playerCount