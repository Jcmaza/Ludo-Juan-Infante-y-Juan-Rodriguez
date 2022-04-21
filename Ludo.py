import imp
import random as rd
from xmlrpc.client import boolean

class Jugadores():
    def __init__(self,color):
        self.color = color
        self.jugando = False

    def Emov(self):
        Fmov = int(input("elija la ficha que desea move: "))
        if Fmov == 1:
            print("Escogió la ficha 1")
        elif Fmov == 2:
            print("Escogió la ficha 2")
        elif Fmov == 3:
            print("Escogió la ficha 4")
        elif Fmov == 4:
            print("Escogió la ficha 3")

class Dados():
    def __init__(self, valor):
        self.valor = valor  

    def tirar_dados(self):
        Vdados= rd.randint

class Casillas():
    def __init__(self,posicion,tamaño,color,tipo):
        self.posicion = posicion
        self.tamaño = tamaño
        self.color = color 
        self.tipo = tipo

class Pasillo(Casillas):
   def __init__(self, posicion, tamaño, color, tipo, entrada):
        super().__init__(posicion, tamaño, color,tipo)
        self.entrada = entrada(boolean)

class Seguros(Casillas):
    def __init__(self, posicion, tamaño, color, tipo, protegida):
        super().__init__(posicion, tamaño, color, tipo)
        self.protegida=protegida

class Meta(Casillas):
    def __init__(self, posicion, tamaño, color,tipo, victoria):
        super().__init__(posicion, tamaño,tipo, color)
        self.victoria = victoria(boolean)

class Base(Casillas):
    def __init__(self, posicion, tamaño, color,tipo, jugando):
        super().__init__(posicion, tamaño,tipo, color)
        self.jugando = jugando

class Tablero():
    def __init__(self, numcasillas):
        for i in range(numcasillas):
            print("se crean casilla")
            self.Tablero[y][x]=Casillas
