# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 19:45:56 2016

@author: felipe
"""

import tkinter as tk

class Tabuleiro:
    
    def __init__ (self): 
            
        self.window = tk.Tk()
        self.window.title("Jogo da Velha!")
        self.window.configure(height=64, width=42)