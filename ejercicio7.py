""" 7. Cuál es la diferencia entre un condicional simple y un
condicional compuesto? """

print("Un condicional simple, se refiere a que un hecho tiene solo una circunstancia de suceder. Y un condicional compuesto, refiere a que si un hecho sucede o no, provoca un resultado.")
print("Ejemplo condicional simple --> sueldo=int(input(Ingrese cual es su sueldo:))\nsi su sueldo>3000:\nEsta persona debe abonar impuestos")
sueldo=int(input("Ingrese cual es su sueldo:"))
if sueldo>3000:
    print("Esta persona debe abonar impuestos")
print("Ejemplo condicional simple --> sueldo=int(input(Ingrese cual es su sueldo:))\n si su sueldo>3000:\nEsta persona debe abonar impuestos\n si su sueldo<3000:\nCambie de trabajo")
sueldo=int(input("Ingrese cual es su sueldo(x2):"))
if sueldo>3000:
    print("Esta persona debe abonar impuestos")
else:
    print("Cambie de trabajo, mi amigo")