import os
from math import floor
class Configuracion:

    def __init__(self):
        self.num_juga = 2
        self.distan_pist = 10000
    
    def __str__(self):
        os.system("clear")
        return "\n Cantidad de jugadores: " + str(self.num_juga) + \
                "    Distancia de la pista: " + str(int(self.distan_pist/1000)) + " km \n"

    def fijar_num_juga(self):          ## Fija el numero de jugadores que el usuario ingrese
        os.system("clear")
        self.num_juga = input("¿Cuantas personas van a jugar?: ")

    def fijar_distan_pist(self):        ## Fija la distancia que el jugador quiera recorrer
        os.system("clear")
        self.distan_pist = input("Cuantos kilometros desea recorrer: ")
        self.distan_pist = int(self.distan_pist)*1000
    
    def abrir(self):                        ##Muestra el menu de configuracion
        
        seleccion = 0
        while int(seleccion) != 3:

            self._menu()
            seleccion = input()

            if int(seleccion) == 1 :
                self.fijar_num_juga()
            elif int(seleccion) == 2:
                self.fijar_distan_pist()
            elif int(seleccion) == 3:
                os.system("clear")
            else:
                print("\n Entrada erronea, intente nuevamente \n")

    def _menu(self):
        print(self)
        print("¿Que quiere configurar? \n 1. Cuantos jugadores van a competir \n 2. Distancia de la pista \n 3. Volver al inicio")

