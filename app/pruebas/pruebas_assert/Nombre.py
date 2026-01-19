import re

def validar_nombre(nombre):
    # Expresión regular que valida el nombre
    patron = r"^[A-Za-záéíóúÁÉÍÓÚüÜÑñ']+$"
   
    # Verificar si el nombre coincide con el patrón
    if re.match(patron, nombre):
        return True
    else:
        return False

# Assert 
assert validar_nombre("Carlos")
assert validar_nombre("José")
assert validar_nombre("María")
assert validar_nombre("O'Connor")   # Acepta apóstrofo
assert validar_nombre("Ñañez")      # Acepta ñ

# Assert not 
assert not validar_nombre("Carlos123")   # No debe tener números
assert not validar_nombre("Ana_")        # No debe tener guiones bajos
assert not validar_nombre("Pepe!")       # No debe tener símbolos
assert not validar_nombre(" ")           # No debe estar vacío
assert not validar_nombre("")            # Cadena vacía
