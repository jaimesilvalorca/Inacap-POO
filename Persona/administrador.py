from persona import Persona;

class Administrador(Persona):
    def __init__(self, rut, clave, nombre, cargo, claveAdmin):
        super().__init__(rut, clave, nombre, cargo)
        self.__claveAdmin = claveAdmin

    def __str__(self):
        return f'{super().__str__()}  Clave de adminitador no se muestra'

    def setClaveAdmin(self, claveAdmin):
        self.__claveAdmin = claveAdmin;

    def getClaveAdmin(self):
        return self.__claveAdmin;

    def getAcceso(self, claveAdmin, clave, rut):
        if rut == super().getRut() and claveAdmin == self.__claveAdmin and clave == super().getClave():
            return True
        else:
            return False
        """"""

