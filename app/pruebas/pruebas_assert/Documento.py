import re

# Función para validar el tipo de documento
def validar_tipo_documento(tipo, documento):
    # Patrones para validar diferentes documentos 
    patrones = {
        "CC": r'^\d{6,10}$',        # Cédula de ciudadanía: 6 a 10 dígitos
        "CE": r'^\d{7,9}$',         # Cédula de extranjería: 7 a 9 dígitos
        "PPT": r'^[A-Za-z0-9]{5,15}$',  # Pasaporte: 5 a 15 caracteres alfanuméricos
        "TI": r'^\d{7,10}$',        # Tarjeta de identidad: 7 a 10 dígitos
        "NIT": r'^\d{9,12}$'        # NIT: 9 a 12 dígitos
    }
    
    # Validar el documento según el correspondiente
    if re.match(patrones[tipo], documento.strip()):
        return True
    return False


# Assert y assert not
assert validar_tipo_documento("CC", "123456")       # válido, 6 dígitos
assert validar_tipo_documento("CC", "1234567890")   # válido, 10 dígitos
assert not validar_tipo_documento("CC", "12345")    # inválido, muy corto
assert not validar_tipo_documento("CC", "12345678901") # inválido, muy largo

assert validar_tipo_documento("CE", "1234567")      # válido, 7 dígitos
assert validar_tipo_documento("CE", "123456789")    # válido, 9 dígitos
assert not validar_tipo_documento("CE", "123456")   # inválido

assert validar_tipo_documento("PPT", "A12345")      # válido
assert validar_tipo_documento("PPT", "PASSPORT123") # válido
assert not validar_tipo_documento("PPT", "AB")      # inválido, muy corto

assert validar_tipo_documento("TI", "1234567")      # válido, 7 dígitos
assert validar_tipo_documento("TI", "1234567890")   # válido, 10 dígitos
assert not validar_tipo_documento("TI", "123456")   # inválido

assert validar_tipo_documento("NIT", "123456789")   # válido, 9 dígitos
assert validar_tipo_documento("NIT", "123456789012") # válido, 12 dígitos
assert not validar_tipo_documento("NIT", "12345")   # inválido
assert not validar_tipo_documento("NIT", "1234567890123") # inválido, muy largo