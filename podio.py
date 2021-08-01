import os
class Podio:
    def __init__(self, clasificacion):
        self.clasificacion = clasificacion

    def mostrar(self):                          ## Muestra el podia al terminar la partida
        os.system("clear")
        
        print(f"La ubicacion de los jugadores es: \n ")
        for i,jugador in enumerate(self.clasificacion):
            print(i+1,". ",jugador.nomb)
            jugador.puesto_reciente = i+1
            if i+1 ==1:
                jugador.ven = int(jugador.ven) + 1

        
        input("\n Presiona ENTER para volver a la pantalla de inicio ")
