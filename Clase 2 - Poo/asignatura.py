from profesor import Profesor

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

print(asignatura.get_profesor().get_rut())
asignatura.set_profesor(profesor2)
print(asignatura.get_profesor().get_rut())