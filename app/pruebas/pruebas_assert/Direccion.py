import re  
  
def validar_direccion(direccion):  
    # Expresión regular que valida la dirección  
    patron = (  
        r"^"    
        r"(Calle|Carrera|Diagonal|Avenida|Transversal|Avenida Carrera)\s"  # Tipo de vía  
        r"\d{1,3}[A-Za-z]?\s?"  # Número y posible letra (ej. 123A)  
        r"#?\s?\d{1,3}[A-Za-z]?(?:-\d{1,3}[A-Za-z]?)?\s"  # Complemento y posible extensión  
        r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+"  # Nombre del barrio  
        r"(,\sConjunto\s[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+"  # Nombre del conjunto   
        r"(,\sTorre\s[\w\s]+)?\sNúmero\s?[\w\s]+)?$"  # Torre y apartamento  
    )  
  
    if re.match(patron, direccion, re.IGNORECASE):  
        return True  
    else:  
        return False  

# Pruebas con assert
assert validar_direccion("Calle 123 #45-67 San Martín")
assert validar_direccion("Carrera 10 #20-30 La Esperanza")
assert validar_direccion("Avenida 15 #12A-45 Centro")
assert validar_direccion("Calle 23 #56-78 El Poblado, Conjunto Los Almendros, Torre 3 Número 402")

# Pruebas con assert not
assert not validar_direccion("Calle #45-67 San Martín")     # Falta el número antes del #
assert not validar_direccion("Carrera 20 #30-40")           # Falta nombre de barrio
assert not validar_direccion("")                            # Vacío
