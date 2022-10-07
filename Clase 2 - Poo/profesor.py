from persona import Persona
class Profesor(Persona):
    def __init__(self,rut="", nombres="NN", apellidos="NN", rango="x"):
        super().__init__(rut, nombres, apellidos)
        self.__rango = rango 
        
    def __str__(self):
        return f"{super().__str__()} Rango {self.__rango}"