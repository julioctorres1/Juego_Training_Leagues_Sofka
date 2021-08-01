class Jugador:
    def __init__(self, nomb, ven = 0, puest_recient = 0):
        self.nomb = nomb
        self.ven = ven
        self.puest_recient = puest_recient
        self.carr = {}
        self.dist_recorrida = 0
    
    def __str__(self):
        return self.nombre + " " + str(self.ven) + " " + str(self.puesto_reciente) 

    def ubicar_carril(self, carr):                        ##asocia un carril con el jugador
        self.carr = carr
    
    def avanzar(self, avan):                              ##Aumenta la distancia que reccore sobre el carril segun indique el dado
        if self.dist_recorrida <= self.carr.distan:
            self.dist_recorrida += avan

            