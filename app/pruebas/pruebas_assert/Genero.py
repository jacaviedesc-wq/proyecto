import re

def validar_genero(genero):
    # Expresión regular 
    patron = r'^(masculino|femenino|otro|m|f|o)$'
    
    if re.match(patron, genero.strip().lower()):
        return True
    return False


# Pruebas con assert
assert validar_genero("masculino")
assert validar_genero("femenino")
assert validar_genero("otro")
assert validar_genero("M")   
assert validar_genero("F")
assert validar_genero("o")

# Pruebas con assert not
assert not validar_genero("hombre")
assert not validar_genero("mujer")
assert not validar_genero("x")
assert not validar_genero("")
assert not validar_genero("otros")  # debe ser solo "otro"
