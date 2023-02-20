""" 10. En su casa le solicitan que realice un algoritmo en Python,
que permita calcular el valor a pagar por concepto de
energía eléctrica. Los datos que se conocen son los
siguientes:
- Mes de consumo - Valor kw
-Total kw consumido en el mes - estrato """

mesEnero=400
mesFebrero=450
mesDiciembre=600
valorKw=275.04
impuesto=250000

print("REGISTRO DE CONSUMO DE ENERGÍA ELECTRICA")
print("(MESES DICIEMBRE, ENERO Y FEBRERO)")
mes=input("Ingresa el mes que quieres consultar (MAYUS): ")
if mes== "ENERO": total={
     int((mesEnero*0.5*30)*valorKw)
}
elif mes== "FEBRERO":total={
    int((mesFebrero*0.5*30)*valorKw)
}
elif mes== "DICIEMBRE":total={
    int((mesDiciembre*0.5*30)*valorKw)
}
estrato=int(input("Ingresa tu estrato: "))
if estrato>2:total={
    sum(total,impuesto)
}

print("El total a pagar del mes "+ str(mes)+" es de: ",total,"COP")