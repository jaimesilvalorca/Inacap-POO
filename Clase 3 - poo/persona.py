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
 

class Asignatura:
    def __init__(self,  codigo, nombre, profesor):
        self.__codigo: int= codigo
        self.__nombre: str= nombre
        self.__profesor = profesor
        self.__notas = {}

    def set_profesor(self, profesor):
        self.__profesor = profesor

    def get_profesor(self):
        return self.__profesor

profesor = Profesor("1687815", "andres", "silva", "profesor")
profesor2 = Profesor("454546", "jaime", "silva", "profesor")

asignatura = Asignatura("codigo", "nombre", profesor)

print(asignatura.get_profesor().get_rango())
asignatura.set_profesor(profesor2)
print(asignatura.get_profesor().get_rut())
