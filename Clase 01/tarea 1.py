def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    return binario


decimal = int(input("Ingresa un número decimal: "))
binario = decimal_a_binario(decimal)
print(f"El número {decimal} es {binario} en binario")