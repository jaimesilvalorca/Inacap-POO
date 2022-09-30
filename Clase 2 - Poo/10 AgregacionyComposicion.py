class Motor:
    def __init__(self, ns, p, listaPiezas = ["1","2","3","4"] ):
        self.__numeroSerie = ns
        self.__procedencia = p
        self.__listaPiezas = listaPiezas
        
    def getSerie(self):
        return self.__numeroSerie
    
    def getListaPiezas(self):
        return self.__listaPiezas
    
    def addPieza(self, pieza):
        if pieza not in self.getListaPiezas():
            self.getListaPiezas().append(pieza)
        else:
            print("no se puede agregar pieza..Revisar!!")
    
    def setSerie(self, nro):
        self.__numeroSerie = nro

m1= Motor("00000001", "xx")
print(m1.getSerie())
#cambiamos el valor de la propiedad
m1.setSerie("00000002")
print(m1, m1.getSerie())

m2 = m1 #2 variables apuntan a la misma referencia de memoria
print(m2, m2.getSerie())
m1.setSerie("0222222222")
print(m2, m2.getSerie())
print(m1, m1.getSerie())
print(m1.getListaPiezas())
#enviamos una nueva pieza la motor
m1.addPieza("5")
print(m1.getListaPiezas())
m1 = None
print(m2.getListaPiezas())