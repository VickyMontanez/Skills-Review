""" 4. Que son las expresiones regulares en Python? """
print("Las expresiones regulares en Python son unas secuencias de caracteres que forma un patrón de búsqueda para arrojar un valor\nej:Agenda de contactos")

def obtener_agenda():
  contactos = {}
  while True:
    nombre = input("Ingresa un nombre")
    if nombre == "":
      break
    if nombre in contactos:
      print("Nombre ya existente")
      else:
        telefono= input(f"Ingrese el telefono de {nombre}: ")
        contactos[nombre] = telefono
    return contactos
  
  def imprimir_agenda():
    contactos = obtener_agenda()
    for nombre un contactos:
      telefono = contactos[nombre]
      print(f"{nombre} tiene el telefono {telefono}")
