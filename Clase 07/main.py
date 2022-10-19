from arbol import Arbol
    

arbol_numeros = Arbol(5)   ##### el 5 es la raiz, que hay que crear si o si


lista_agregar = [20,58,45,174,74,1,5,78]

for i in lista_agregar:
    arbol_numeros.agregar(i)


arbol_numeros.preorden()
arbol_numeros.inorden()
arbol_numeros.postorden()


while True:   ## para que no corte  

    busqueda = int(input("Ingresa un número para buscar en el árbol: "))
    n = arbol_numeros.buscar(busqueda)
    if n is None:
        print(f"{busqueda} no existe")
    else:
        print(f"{busqueda} sí existe")