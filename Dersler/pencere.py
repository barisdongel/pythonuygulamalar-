#araüz geliştirme de kullanılır.

import tkinter as tk

pencere = tk.Tk()
pencere.title("İlk GUI")
pencere.geometry("500x300+50+50")

etiket = tk.Label(text="ilk etiket",font="Ariel 16 bold")
etiket.place(x=230,y=0)
etiket['font'] = "Helvetica 22 italic"
etiket['bg'] = "#0face0"
etiket['fg'] = "#fff"

giris = tk.Entry(font="Robotic 20")
giris.place(x=100,y=100)

pencere.mainloop()