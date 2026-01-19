import re

def validar_correo_personal(correo):
    # Expresión regular para validar correo electrónico personal 
    patron_general = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    patron_institucional = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.edu\.co$"

    # Es personal si cumple el general y NO es institucional
    if re.match(patron_general, correo) and not re.match(patron_institucional, correo):
        return True
    return False

def validar_correo_institucional(correo):
    # Expresión regular para validar correo electrónico institucional (.edu.co o .com) 
    patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.(edu\.co)$"
    if re.match(patron, correo):
        return True
    else:
        return False

# Assert
assert validar_correo_personal("juan.perez@gmail.com")
assert validar_correo_personal("maria_23@hotmail.co")
assert validar_correo_personal("user123@yahoo.es")

# Assert not
assert not validar_correo_personal("juanperez@")       # Falta dominio
assert not validar_correo_personal("maria@gmail")      # Falta .com
assert not validar_correo_personal("correo@@gmail.com")# Doble @
assert not validar_correo_personal("")                 # Vacío

# Assert
assert validar_correo_institucional("andres@universidad.edu.co")

# Assert not
assert not validar_correo_institucional("andres@universidad.edu")   # Falta .co
assert not validar_correo_institucional("soporte@empresa.org")      # .org no permitido
assert not validar_correo_institucional("")                         # Vacío
