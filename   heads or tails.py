#Yazı-Tura 

import random 
import tkinter as tk 
from tkinter import messagebox 


def f () : 
    sayı = random.randint(1,2) 
    if sayı == 1 : 
        messagebox.showinfo("YAZI GELDİ ", "YAZI GELDİ !!!" ) 
    else : 
        messagebox.showinfo("TURA GELDİ ","TURA GELDİ !!!") 

         


window = tk.Tk() 
window.title("Yazı-Tura ") 
window.geometry("200x200")

label = tk.Label(text = "Lütfen butona basarak atma işlemini başlatınız ")  
label.pack() 

Buton = tk.Button(text = "At" , command = f  ) 
Buton.pack() 

window.mainloop() 