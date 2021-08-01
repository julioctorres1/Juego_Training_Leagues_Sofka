from carr import Carril
from math import floor

class Pista:
    def __init__(self, config):
        self.carriles = []
        self.distancia = config.distan_pist
        self.num_carriles = config.num_juga
        
    
    def construir_carriles(self):                               #Construye el numero de carriles en la pista segun la cantidad de jugadores
        for i in range(self.num_carriles):
            self.carriles.append(Carril(i+1, self.distancia))
        return self.carriles

    def mostrar(self,jugadores):                                #Muestra el avance de los jugadores en la pista, si llego a la meta y la distancia recorrida hasta el momento
        for jugador in jugadores:
            print("{:8} ||".format(jugador.nomb),end="")
            for i in range(int(self.distancia/1000)-1):
                if floor(jugador.dist_recorrida/1000) == i:
                    print("O",end="")
                else:
                    print("-", end="")
            if floor(jugador.dist_recorrida/1000) >= int(self.distancia/1000):
                print("O", end="")
            else:
                print("[", end="")

            print(f"  {jugador.dist_recorrida/1000} km\n")
            
