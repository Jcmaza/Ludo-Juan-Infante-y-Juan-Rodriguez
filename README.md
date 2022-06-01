

![uml](https://user-images.githubusercontent.com/98894988/164529479-7eb7cf0a-ccdc-4957-b267-1d3c6931dcae.PNG)

@startuml
class  Parques
class  Jugadores
class  Tablero
class  Fichas 
class  Dados
class  casillas
class  pasillo
class  seguros 
class  meta
class  base
class salida
Parques : inicar_partida()
Parques : salir_del_juego()
Parques : numero_de_jugadores[]
Jugadores : tirar_dados()
Jugadores : elegir_mov()
Jugadores : abandonar()
Jugadores : color[]
Dados : tirar()
Dados : caras()
Fichas : movimiento()
Fichas : comer()
Fichas : salir_de_base()
Fichas : viva[]
Fichas : color[]
Fichas : posición[]
casillas : posición[]
casillas : tamaño[]
casillas : color[]
pasillo : entrada_restringida()
seguros : salvar()
meta : victoria()
meta : entrada()
base : en_base()
Jugadores - Parques : de 2 a 4 juegan >
Parques *-- Tablero : 1 <
Parques *-- Dados : 2 < 
Parques *-- casillas
Parques *-- Fichas : 4 por jugador <
casillas *-- pasillo 
casillas *-- seguros 
casillas *-- meta
casillas *-- base 
casillas *-- salida
salida <|-- seguros
@enduml
