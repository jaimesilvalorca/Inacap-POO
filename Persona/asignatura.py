from profesor import Profesor
from alumno import Alumno
from nota import Nota
class Asignatura:
    def __init__(self, codigo, nombre, profe=Profesor(), notas={}):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__profesor = profe
        self.__lista = []
        self.__notas = notas
    def __str__(self):
        return f"código: {self.__codigo} - {self.__nombre} - Datos profesor: {self.__profesor}"
    
    def __del__(self):
        print("Asignatura Eliminada")
        
    def setProfesor(self, p):
        self.__profesor = p

    """listar todos los estudiantes de la asignatura x"""
    def listar(self):
        if len(self.__lista) == 0:
            print("No hay alumnos")
        else:
            print(f"Alumnos Asignatura {self.__codigo}-{self.__nombre} - {self.__profesor}")
            for a in self.__lista:
                print(a)

    """matricula cada estudiante en la asignatura, usando una lista"""            
    def matricular(self, a):
        if a not in self.__lista:
            self.__lista.append(a)
            return f"Alumno {a} matriculado"
        else:
            return "Alumno ya existe en la asignatura"

    """busca el alumno dentro de la lista"""    
    def getAlumno(self, rut):
        for a in self.__lista:
            if rut == a.getRut():
                return a
        return None
    
    """Agrega nota de alumno por medio de su rut,
    dentro del diccionario notas"""
    def addNota(self, rut, numero, porcentaje, nota):
        if self.getAlumno(rut) is not None:
            if rut not in self.__notas.keys():
                self.__notas[rut] = []
                self.__notas[rut].append(Nota(numero, porcentaje, nota))
            else:
                self.__notas[rut].append(Nota(numero, porcentaje, nota))
        else:
            print("alumno No matriculado")
    
    """imprime notas de un alumno"""
    def printNotas(self, rut):
        if self.getAlumno(rut) is not None:
            if rut in self.__notas.keys():
                print(f"Notas del Alumno {self.getAlumno(rut)}")
                for n in self.__notas[rut]:
                    print(n, end=" ")
                print("promedio --> ", self.getPromedio(rut))
            else:
                print(f"El alumno  {self.getAlumno(rut)} no tiene notas")
        else:
            print("el alumno no está en la lista de la asignatura")
    
    """obtiene el promedio del estudiante"""
    def getPromedio(self, rut):
        p=0
        if self.getAlumno(rut) is not None:
            if rut in self.__notas.keys():
                for n in self.__notas[rut]:
                    p += (n.getPorcentaje()/100) * n.getValor()
                return round(p,2)
            else:
                return f"Alumno {self.getAlumno(rut)} no tiene notas"
        else:
            return f"Alumno no está en la lista de la asignatura"

    """listar todos los alumnos con sus respectivas notas y promedio"""        
    def listarNotas(self):
        for a in self.__lista:
            self.printNotas(a.getRut())