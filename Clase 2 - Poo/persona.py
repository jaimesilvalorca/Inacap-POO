class Persona:
    def __init__(self, rut="", nombres="", apellidos=""):
        self.__rut = rut
        self.__nombres = nombres
        self.__apellidos = apellidos
    def __str__(self):
        return f"RUT : {self.__rut} Nombres: {self.__nombres} Apellidos: {self.__apellidos}"
    def getRut(self):
        return self.__rut