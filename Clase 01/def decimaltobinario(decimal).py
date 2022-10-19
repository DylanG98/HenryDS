def decimaltobinario(decimal):

    if decimal <= -1:
        return "Nulo"
    
    binario= ""

        
    while decimal > 0:

        resto = int(decimal % 2)

        decimal = int (decimal / 2) 

        binario = str (resto) + binario

    return binario 

#decimal = int(input("Número:"))
#binario = decimaltobinario(decimal)

#print(f'El número {decimal} es {binario} en binario')

#---------------------------------------------------------------

def NumeroBinario(numero):
    if numero < 0:
        print('Debe ingresar un numero mayot que cero')
        return None
    elif type(numero) != int:
        print('Debe ingresar un numero entero')
        return None
    elif numero == 0:
        return 0
    else:

        '''crear una lista vacia para ir guardando los valores binarios'''
        lista_binaria= []
        '''definimos el primer numero binario del cociente'''
        modulo = numero % 2
        lista_binaria.append(modulo)
        '''defino una lista para los cocientes'''
        lista_cocientes= []
        cociente= numero // 2
        lista_cocientes.append(cociente)

        for i in lista_cocientes:
            '''cuando el iterador i pasa por la lista y se encuenta con un 1, el bucle se frena y sale'''
            if i == 1:
                break
            else:
                nuevo_cociente = i // 2
                lista_cocientes.append(nuevo_cociente)
        
        for i in lista_cocientes:
            if i == 1:
                lista_binaria.append(1)
            else:
                binario = i % 2
                lista_binaria.append(binario)

    print(lista_binaria[::-1])

NumeroBinario(25)