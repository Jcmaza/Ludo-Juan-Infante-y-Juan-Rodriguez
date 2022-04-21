La implementación que nosotros hemos introducido es la de la interfaz gráfica, la cual apenas está en su estado más básico de desarrollo pero se puede observar sin problemas simplemente clonando el repositorio y corriendo el archivo "Visual.py"

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
