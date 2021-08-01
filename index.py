import os
import json
import operator

from podio import Podio
from config import Configuracion
from juego import Juego

with open('src/datos.json') as datos:
    datos = json.load(datos)

config = Configuracion()



def historico(datos):       #Muestra los datos guradados en el archivo .json, nombre, las veces que ha ganado y el puesto mas reciente
    os.system("clear")
    lista = list(datos.values())
    print("\n {:^15} {:^15} {:^15}".format('nombre','veces primero','puesto_reciente'))
    print("-----------------------------------------------------")
    for item in lista:
        print("{:^15} {:^15} {:^15}".format(item['nombre'],item['vencedor'],item['puesto_reciente']))
    print("\n")
    input("Presiones ENTER para regresar al menu anterior")


while (True):
    ###### Menu principal#####
    print("""Seleccione una de las siguientes opciónes: \n 
            1. Inicia el juego \n 
            2. Configuracion del juego \n 
            3. Clasificaciones finales \n
            4. Guardar y salir""")

    seleccion = input()

    if int(seleccion) == 1:                  #Iniciar juego
        juego = Juego(config, datos)
        juego.fijar_jugadores()
        juego.crear_pista()
        juego.iniciar_juego()

    elif int(seleccion) == 2:               #Configurar juego
        config.abrir()

    elif int(seleccion) == 3:               #Clasificacion
        historico(datos)

    elif int(seleccion) == 4:               #Salir
        print("\n Adios \n")
        with open('src/datos.json', 'w') as outfile:        #Al salir guarda los cambios en los atributos de los jugadores
            json.dump(datos, outfile)
        exit() 

    else:
        print("Ingreso un nuemero equivocado \n")


