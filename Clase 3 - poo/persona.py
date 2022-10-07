class Persona:

    def __init__(self, rut, nombre, apellidos):
        self.__rut: str= rut
        self.__nombre: str= nombre
        self.__apellidos: str=apellidos

    def get_rut(self):
        return self.__rut

    def set_rut(self, rut):
        self.__rut = rut
 

class Profesor(Persona):

    def __init__(self,  rut, nombre, apellidos, rango):
        super().__init__(rut, nombre, apellidos)
        self.__rango = rango

    def get_rango(self):
        return self.__rango

    def set_rango(self, rango):
        self.__rango = rango
 



class Alumno(Persona):

    def __init__(self,  rut, nombre, apellidos, edad):
        super().__init__(rut, nombre, apellidos)
        self.__edad = edad

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad= edad
 


