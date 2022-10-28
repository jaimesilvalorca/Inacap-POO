from persona import Persona;

class Empleado(Persona):
    def __init__(self, rut, clave, nombre, cargo, depto):
        super().__init__(rut, clave, nombre, cargo)
        self.__listaEmpleado = []
        self.__depto = depto

    def __str__(self):
        return f'{super().__str__()}  Departamento: {self.__depto}'

    def setDepto(self, depto):
        self.__depto = depto

    def getDepto(self):
        return self.__depto

    def getListaEmpleado(self):
        return self.__listaEmpleado
        
    def addEmpleado(self, rut, clave, nombre, cargo, depto):
        e = Empleado(rut, clave, nombre, cargo, depto)
        if e not in self.getListaEmpleado():
            self.getListaEmpleado().append(e)
            return "Empleado registrado de manera exitosa"
        else:
            return 'Empleado ya existe, vuelva a intentarlo'

    def buscarEmpleado(self, rut):
        if len(self.getListaEmpleado()) != 0:
            for e in self.getListaEmpleado():
                if rut == e.getRut():
                    return e
            return None
        else:
            return None

    def subEmpleado(self, rut):
        e = self.buscarEmpleado(rut)
        if e is not None:
            self.getListaEmpleado().remove(e)
            return 'Empleado eliminado exitosamente!'
        else:
            return 'Empleado no encontrado'

    
    def modificarEmpleado(self, clave, opcion, rut):
        e = self.buscarEmpleado(rut)
        if e is not None:
            if opcion == 1:
                e.setClave(clave)
                return 'Clave modificada exitosamente!'
            elif opcion == 2:
                e.setNombre(clave)
                return 'Nombre modificado exitosamente!'
            elif opcion == 3:
                e.setCargo(clave)
                return 'Cargo modificado exitosamente!'
        else:
            return 'Empleado no encontrado'

    def mostrarTodos(self):
        for e in self.getListaEmpleado():
            print(e)
        
            

