from email.mime import image
from pydoc import plain
import re
from tkinter import *  
def Iniciar():
    def Proceso():
        Juego.destroy()
        Cred = Tk()
        Jeje=Label(Cred, text="Aún en proceso"). place(x=0, y=0, relheight=1, relwidth=1)

    Raiz.destroy()
    Juego = Tk()  
    Tab = PhotoImage(file="tablero.gif")  
    Tablero = Button(Juego, image=Tab, cursor="hand2", width=700, height=700, command=Proceso).place(x=225, y=45)

    Juego.title("Ludo")
    Juego.iconbitmap("tab.ico")
    Juego.geometry("1200x775")
    Juego.resizable(False, False)
    Juego.mainloop()

def Credito():
    Raiz.destroy()
    Cred = Tk()
    Jeje=Label(Cred, text="Aún en proceso"). place(x=0, y=0, relheight=1, relwidth=1)

Raiz = Tk()
fondo = PhotoImage(file="fondo.gif")

Raiz.title("Ludo")
Raiz.iconbitmap("tab.ico")
Raiz.geometry("900x500")
Raiz.resizable(False,False)
Fondo = Label(Raiz, image=fondo). place(x=0, y=0, relheight=1, relwidth=1)
Inicio = Button(Raiz, text="Iniciar el juego", cursor="hand2", width=25, height=3,command=Iniciar).place(x=600, y=100)
Salir = Button(Raiz, text="Salir",cursor="hand2",width=25, height=3 ,command=Raiz.quit).place(x=600, y=200) 
Creditos = Button(Raiz, text="Creditos", cursor="hand2",width=25, height=3, command=Credito).place(x=600, y=300)

Raiz.mainloop()
