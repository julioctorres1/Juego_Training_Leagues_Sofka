import os
import time
import random
from math import floor
from juga import Jugador
from pista import Pista
from podio import Podio

class Juego:

    def __init__(self, config, datos):
        self.config = config
        self.jugadores = []                     #En jugadores se guardan los objetos de la cantidad de personas que jugaran
        self.datos = datos
        self.pista = {}
        self.clasificacion = []
        self.finish = 0
        self.podio = {}

    def fijar_jugadores(self):                  #Se crean los objetos de los jugadores que van a jugar esta partida
        for i in range(int(self.config.num_juga)):
            self.jugadores.append(self.consultar_jugadores(input(f"\n Ingrese el nombre del jugador {i+1}: "))) 

    def consultar_jugadores(self, nombre):      #Se consulta si el jugador esta en la base de datos
        if f'{nombre}' in self.datos:           #Si el jugador esta en la base de datos, se crea un nuevo objeto jugador con los datos existentes
            jugador = Jugador(self.datos[f'{nombre}']['nombre'],self.datos[f'{nombre}']['vencedor'],self.datos[f'{nombre}']['puesto_reciente'])
            return jugador
        else:
            return self.nuevo_jugador(nombre)

    def nuevo_jugador(self, nombre):            #Si el jugador no esta en la base de datos, se crea un nuevo jugador
        print("\n ... \n Nuevo jugador creado\n...\n")
        jugador = Jugador(nombre)
        self.datos[f'{nombre}'] = {'nombre':f'{jugador.nombre}','vencedor':f'{jugador.vencedor}','puesto_reciente':f'{jugador.puesto_reciente}'}
        return jugador

    def crear_pista(self):                      #Crea la pista con su distancia y su cantidad de carriles, asocia a sus carriles con los jugadores
        self.pista = Pista(self.config)
        carriles = self.pista.construir_carriles()
        for i in range(self.pista.num_carriles):
            self.jugadores[i].ubicar_carril(carriles[i])
    
    def iniciar_juego(self):                    ##Inicia el juego
        os.system("clear")
        while(not self.finish):                 #Mientras no termina el juego no avanza la ejecucion
            for i in range(len(self.jugadores)):    #Respresenta el turno de cada jugador
                
                print(f"===== El primero en llegar a la meta gana ({self.config.distan_pist/1000} km) =====\n")
                self.pista.mostrar(self.jugadores)
                input(f"El turno para el jugador {self.jugadores[i].nomb}, presiona ENTER para tirar el dado")
                print("El resultado del dado es: ", end="")
                
                avance = self.lanzar_dado()
                self.jugadores[i].avanzar(avance*1000)
                self.clasificador()
                
                
                os.system("clear") 

            if len(self.clasificacion) >= self.config.num_juga:            #Cuando han llegado todos los jugadores a la meta, crea el podio
                    self.podio = Podio(self.clasificacion)                      
                    self.podio.mostrar()    
                    for jugador in self.jugadores:                              #Actualiza los datos de los  jugadores
                        self.datos[f'{jugador.nomb}']['vencedor'] = jugador.ven
                        self.datos[f'{jugador.nomb}']['puesto_reciente'] = jugador.puesto_reciente
                    self.finish = True   
                

    def lanzar_dado(self):
        print("...",end="")
        avance = random.randint(1,6)
        print(" ",avance, " -> Avanza ",avance*100," metros")
        time.sleep(2)
        return avance

    def clasificador(self):                         #Clasifica los jugadores segun van llegando a la meta
        for jugador in self.jugadores:
            if floor(jugador.dist_recorrida/1000) >= int(self.pista.distancia/1000):
                if jugador not in self.clasificacion:
                    self.clasificacion.append(jugador)
        time.sleep(1)