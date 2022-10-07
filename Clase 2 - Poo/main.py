from profesor import Profesor
from alumno import Alumno
from asignatura import Asignatura

def opciones():
    print("Menú principal")
    print("1 Crear asignatura")
    print("2 Asignar Profesor")
    print("3 Matricular alumno")
    print("4 Ingresar nota de alumno")
    print("5 listar notas de un alumno")
    print("6 Listar notas de todos los estudiantes")
    print("7 listar todos los alumnos de la asignatura")
    print("8 Salir")
def ingresoOpcion():
    try:
        op = int(input("Ingrese opción:"))
        if op >=1 and op<=8:
            return op
        else:
            print("Debe ingresar una opción valida")
            ingresoOpcion()
    except Exception:
        print("Error en el ingreso")
        ingresoOpcion()
sw = 0    
while True:
    opciones()
    op = ingresoOpcion()
    if op ==8:
        break
    else:
        if op==1:
            asi = Asignatura(int(input("Ingrese código:")),input("Ingrese nombre asignatura"))
            print(asi)
            sw=1
            tecla = input("Digite enter para continuar")
        elif op==2:
            if sw==1:
                pro = Profesor(input("Ingrese rut:"),input("Ingrese nombre:"),  \
                input("Ingrese apellido:"), input("Ingrese rango:"))
                print(pro)
                asi.setProfesor(pro)
                print(asi)
            else:
                print("Usted debe registrar antes que todo la asignatura")
            tecla = input("Digite enter para continuar")
        elif op==3:
            if sw==1:
                a = Alumno(input("Ingrese rut:"),input("Ingrese nombre:"),  \
                input("Ingrese apellido:"), input("Ingrese edad:"))
                print(asi.matricular(a))
            else:
                print("Usted debe registrar antes que todo la asignatura")
            tecla = input("Digite enter para continuar")
        elif op==4:
            if sw==1:
                asi.addNota(input("Ingrese rut:"),float(input("Ingrese nota:")))
            else:
                print("Usted debe registrar antes que todo la asignatura")    
            tecla = input("Digite enter para continuar")
        elif op ==5:
            if sw==1:
                asi.printNotas(input("Ingrese rut:"))
            else:
               print("Usted debe registrar antes que todo la asignatura")
            tecla = input("Digite enter para continuar")
        elif op==6:
            if sw==1:
                asi.listarNotas()
            else:
               print("Usted debe registrar antes que todo la asignatura")
            tecla = input("Digite enter para continuar") 
        else:
            if sw==1:
                asi.listar()
            else:
               print("Usted debe registrar antes que todo la asignatura")
            tecla = input("Digite enter para continuar") 

"""p = Profesor("1-1","Pedro","Gonzalez","A1")
a = Alumno("33-3","Juan","Covarrubias",22)
b = Alumno("44-4","Diego","Soto",21)
c = Alumno("55-5","Claudia","Tapia",25)

asi = Asignatura(10101, "POO" )
print(asi)
asi.listar()


print(asi.matricular(a))
print(asi.matricular(b))
print(asi.matricular(c))

asi.listar()
asi.setProfesor(p)
asi.listar()

asi.addNota("33-3",5)
asi.addNota("33-3",4)
asi.addNota("33-3",4)
asi.addNota("44-4",5)

asi.printNotas("33-3")
  
asi.listarNotas()"""