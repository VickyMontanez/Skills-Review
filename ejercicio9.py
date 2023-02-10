#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
cantidad= int(input("Indique la cantidad de personas que desea ingresar: "))
if (cantidad> 0):
    print("*******SIGUE LA LISTA*******")
    print("1.AGREGAR NOMBRE")
    print("2.AGREGAR APELLIDO")
    print("3.AGREGAR EDAD")
    print("4.AGREGAR TELEFONO")
    print("5.AGREGAR AÑO DE INGRESO")
    print("6.MOSTRAR EMPLEADOS")
    print()
    for c in range(0,cantidad):
        nombre= input("Ingrese el nombre: ")
        apellido=input("Ingrese el apelido: ")
        edad= input("Ingrese la edad: ")
        telefono= input("Ingrese el telefono: ")
        año= int(input("Ingrese el año: "))
        

print(nombre,apellido,(2023-año),"año(s) de antiguedad")