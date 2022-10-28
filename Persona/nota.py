class Nota:
    def __init__(self, numero, porcentaje, valor):
        self.__numero = numero
        self.__porcentaje = porcentaje
        self.__valor=valor
    def getPorcentaje(self):
        return self.__porcentaje  
    def getValor(self):
        return self.__valor 
    def __str__(self):
        return f"Nro {self.__numero} Porcentaje {self.__porcentaje} Nota {self.__valor}"