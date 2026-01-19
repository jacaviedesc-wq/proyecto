import re

def validar_celular(celular):
    # Expresión para eliminar espacios, guiones, etc.
    celular = re.sub(r'[^\d+]', '', celular)

    # Si el número es local se agrega el +57
    if re.match(r'^3\d{9}$', celular):
        celular = '+57' + celular
    elif re.match(r'^57\d{10}$', celular):
        celular = '+' + celular

    patron = r'^(?:\+57|57)(?:3[0-9]{9}|9[0-9]{9})$'
   
    # Verificar si el teléfono coincide con el patrón
    if re.match(patron, celular):
        return celular
    else:
        return False

# Assert
assert validar_celular("3001234567") == "+573001234567"    # Número local
assert validar_celular("+573001234567") == "+573001234567" # Ya con +57
assert validar_celular("573001234567") == "+573001234567"  # Con 57
assert validar_celular(" 300 123 4567 ") == "+573001234567" # Con espacios
assert validar_celular("315-678-9012") == "+573156789012"   # Con guiones

# Assert not
assert not validar_celular("2001234567")   # No empieza con 3 
assert not validar_celular("300123456")    # Muy corto
assert not validar_celular("300123456789") # Muy largo
assert not validar_celular("abcdefg")      # Letras no válidas
assert not validar_celular("")             # Vacío
