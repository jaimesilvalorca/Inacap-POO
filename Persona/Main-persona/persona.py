class Persona():
    __listaPersona = []  #atributo de clase
    # Constructor
    def __init__(self,nombre="",edad=0,dni=""):
        self.__nombre=nombre
        self.__edad=edad
        self.__dni=dni
    #retorna el nombre del objeto instanciado
    def getNombre(self):
        return self.__nombre
    #retorna la edad del objeto instanciado
    def getEdad(self):
        return self.__edad
    #retorna el DNI del objeto instanciado
    def getDNI(self):
        return self.__dni
    #Permite asignar un nuevo nombre al atributo del objeto instanciado
    def setNombre(self,nombre):
        self.__nombre=nombre
    #Permite asignar un nuevo dni al atributo del objeto instanciado    
    def setDNI(self,dni):
        self.__dni = dni
    #Permite asignar una nueva edad al atributo del objeto instanciado
    def setEdad(self,edad):
        self.__edad = edad

    #permite incorporar un objeto de tipo persona al atributo de clase __listaPersona
    def addPersona(self,p):
        self.__listaPersona.append(p)
    #Permite retornar la lista de personas ingresadas
    def getLista(self):
        return self.__listaPersona
    """Permite devolver un objeto persona o un None, 
    según rut enviado desde la vista""" 
    def obtenerDNILista(self,rut):
        for perso in self.__listaPersona:
            if perso.getDNI() == rut:
                return perso
        return None
    #retorna el detalle del objeto instanciado
    def __str__(self):
        return f"DNI: {self.__dni} NOMBRE: {self.__nombre} EDAD: {self.__edad}"
    """retorna una cadena de mayor o menor de edad, según
    rut enviado desde la vista"""
    def esMayorDeEdad(self, dni): 
        #Recorre lista, buscando rut ingresado en vista
        perso = self.obtenerDNILista(dni) 
        if perso is not None:
            #verifica que el objeto encontrado sea mayor de edad
            if perso.__edad >=18: 
                return "es mayor de edad"  
            else:
                return "es menor de edad"
        else:
            return "rut no encontrado"
        