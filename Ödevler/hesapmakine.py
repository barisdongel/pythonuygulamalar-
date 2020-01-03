"""
Barış Ömer DÖNGEL
19410051042
"""

import tkinter
from tkinter import messagebox

def topla():
    try:
        t1 = int(number.get())
        t2 = int(number2.get())
        sonuc['text'] = str(t1+t2)
        messagebox.showinfo("Sonuç",str(t1+t2))
    except ValueError:
        messagebox.showerror("Hata!","Lütfen kutucukları boş bırakmayınız ve harf girmeyiniz !")
        number.delete(0,'end')
        number2.delete(0, 'end')
def cıkar():
    try:
        t1 = int(number.get())
        t2 = int(number2.get())
        sonuc['text'] = str(t1-t2)
        messagebox.showinfo("Sonuç",str(t1-t2))
    except ValueError:
        messagebox.showerror("Hata!","Lütfen kutucukları boş bırakmayınız ve harf girmeyiniz !")
        number.delete(0,'end')
        number2.delete(0, 'end')
def carp():
    try:
        t1 = int(number.get())
        t2 = int(number2.get())
        sonuc['text'] = str(t1*t2)
        messagebox.showinfo("Sonuç",str(t1*t2))
    except ValueError:
        messagebox.showerror("Hata!","Lütfen kutucukları boş bırakmayınız ve harf girmeyiniz !")
        number.delete(0,'end')
        number2.delete(0, 'end')
def bol():
    try:
        t1 = int(number.get())
        t2 = int(number2.get())
        sonuc['text'] = str(t1/t2)
        messagebox.showinfo("Sonuç",str(t1/t2))
    except ValueError:
        messagebox.showerror("Hata!","Lütfen kutucukları boş bırakmayınız ve harf girmeyiniz !")
        number.delete(0,'end')
        number2.delete(0, 'end')

window = tkinter.Tk()
window.geometry("400x300")

number = tkinter.Entry(width=20)
number.place(x=20,y=20)

number2 = tkinter.Entry(width=20)
number2.place(x=150,y=20)

sonuc = tkinter.Label(width=10,font="Helvetica",fg="#000000",bg="#0face0")
sonuc.place(x=290,y=20)

topla = tkinter.Button(bg="lightgreen",width=3,text="+",font="Robotica 17",command=topla)
topla.place(x=20,y=45)
cikar = tkinter.Button(bg="lightgreen",width=3,text="-",font="Robotica 17",command=cıkar)
cikar.place(x=80,y=45)
carp = tkinter.Button(bg="lightgreen",width=3,text="x",font="Robotica 17",command=carp)
carp.place(x=140,y=45)
bol = tkinter.Button(bg="lightgreen",width=3,text="/",font="Robotica 17",command=bol)
bol.place(x=200,y=45)

window.mainloop()