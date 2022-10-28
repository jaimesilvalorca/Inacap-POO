from persona import Persona
class Alumno(Persona):
    def __init__(self,rut="", nombres="", apellidos="", edad=0):
        super().__init__(rut, nombres, apellidos)
        self.__edad = edad
        
    def __str__(self):
        return f"{super().__str__()} Edad {self.__edad}"  
    
    def getRut(self):
        return super().getRut()