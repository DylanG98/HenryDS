from nodo import Nodo

class Arbol:

    #########
    ########################

    def __init__(self, dato):

    #####################################
   
    # DATO PRIMARIO QUE SE USA PARA COLOCARLE LA RAIZ DEL ARBOL
    #####################################
   

        self.raiz = Nodo(dato)

    def __agregar_recursivo(self, nodo, dato):
    
    ##############################################################
    ##############################################################
    # EXPLICACION DE RECURSIVIDAD, primero se evalua el dato para saber si va a la izq o der,
    #  SE FIJA DISPONIBILIDAD, 
    # SI ESTA VACIO se inserta, SINO VUELVE A CALLEAR LA FUNCION CON EL NUEVO NODO (nodo.izquierda)
    #  y el dato que teníamos
    # HASTA QUE EL NODO A INGRESAR EL DATO ESTE VACIO.
    ##############################################################
    ##############################################################

        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)

    def __inorden_recursivo(self, nodo): 

        ### inorder visita primero toda la izquierda, se imprime el actual y luego visita toda la derecha ##

        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):

        ### se visita primero el actual, despues la izq y luego la der ###

        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):

        ### primero visita la izq, luego la der y despúes imprime el actual ###

        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.dato, end=", ")

    def __buscar(self, nodo, busqueda):

        ### si está vacia --> no encuenta nada y devuelve None, si nodo.dato es == busqueda regresa nodo 
        # xq encontré el nodo que tiene el dato que busco
        #  

        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    ########################################################
    ########################################################

    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)