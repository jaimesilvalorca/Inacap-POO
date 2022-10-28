from persona import Persona
def validaDNI(): 
    dni = input("Ingrese rut (sin puntos, ni guión):")
    if dni[0:len(dni)-1].isnumeric() and dni[-1] in "0123456789kK":
        if len(dni)!=9: 
            print("Largo del DNI, debe ser de 9 digitos") 
            return validaDNI() 
        else: 
            return dni
    else:
        print("Dato no cumple con formato solicitado") 
        return validaDNI()
def validaNombre():
    nombre = input("Ingrese nombre:")
    if nombre != "":
        return nombre
    else:
        print("Debe ingresar un nombre válido")
        return validaNombre()
def validaEdad(): 
    try:
        edad = int(input("Ingrese edad:"))
        if edad > 0: 
            return edad
        else: 
            print("Edad debe ser mayor a cero") 
            return validaEdad()
    except:
        print("Debe ingresar un valor numérico")
        return validaEdad()
def menu():
    print("Menú principal")
    print("1 Ingreso")
    print("2 Es mayor de edad")
    print("3 mostrar una persona")
    print("4 mostrar todas las personas")
    print("5 Salir")

def validaOpcion():
    try:
        op = int(input("Ingrese opción:"))
        if op > 0 and op <6: 
            return op
        else: 
            print("opción fuera de rango") 
            return validaOpcion()
    except:
        print("Debe ingresar un valor numérico")
        return validaOpcion()

perso = Persona()

while True:
    menu()
    op = validaOpcion()
    if op == 5:
        break
    elif op== 1:
        perso.addPersona(Persona(validaNombre(),validaEdad(), validaDNI()))
        print("Grabación realizada")
    elif op==2:
        if len(perso.getLista())>0:
            print(perso.esMayorDeEdad(validaDNI()))
        else:
            print("No hay personas ingresadas")
            
    elif op==3:
        if len(perso.getLista())>0:
            p = perso.obtenerDNILista(validaDNI())
            print("Rut no encontrado" if p is None else p)
        else:
            print("No hay personas ingresadas")
    else:
        if len(perso.getLista())>0:
            for lista in perso.getLista():
                print(lista)
        else:
            print("No hay personas ingresadas")
