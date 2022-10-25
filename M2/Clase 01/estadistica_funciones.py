import numpy as np # importando numpy
from scipy import stats # importando scipy.stats
import pandas as pd #importando pandas
import matplotlib.pyplot as plt # importando matplotlib
import seaborn as sns # importando seaborn
import math



class estadistica:

    def __init__(self, muestra):
        self.muestra = muestra
    


    #########################################################################
    # Calcular media de un arreglo
    #########################################################################

    def media(self):
        '''
        Esta funcion se encarga de sacar la media de cualquier arreglo de numpy;
        lo que hace es un for en el rango del arreglo, y luego otro que pase por cada
        lista dentro del arreglo, sumandolas y luego dividiendo por la cantidad de values
        '''
        muestra = self.muestra

        alto_arreglo = len(muestra)
        ancho_arreglo = len(muestra[0])

        cant_values = ancho_arreglo * alto_arreglo
        sumatoria = 0

        for i in range(len(muestra)):
            for g in muestra[i]:
                sumatoria += g

        return sumatoria/cant_values


    #########################################################################
    #########################################################################


    def media_np(self, muestra):
        muestra = self.muestra

        return np.mean(muestra)



    #########################################################################
    # Calcular mediana de un arreglo
    #########################################################################

    def mediana(self):
        '''
        Esta funcion sirve para retornar la mediana de un array.
        '''
        muestra = self.muestra  

        alto_arreglo = len(muestra)
        ancho_arreglo = len(muestra[0])

        cant_values = ancho_arreglo * alto_arreglo

        b = np.reshape(muestra, (1,cant_values))
        b.sort()


        if len(b[0])%2 == 1:

            posicion = int((len(b[0])/2))
    
            return b[0, posicion]

        else:

            posicion_1 = int((len(b[0])/2)-1)
            posicion_2 = int((len(b[0])/2))

            return ((b[0,posicion_1]+b[0,posicion_2])/2)



    #########################################################################
    #########################################################################

    def mediana_np(self, muestra):
        muestra = self.muestra


        return np.median(muestra)
        


    #########################################################################
    # Calcular moda de un arreglo
    #########################################################################


    def moda(self, muestra):
        '''
        Esta funcion retorna el value de moda en un array
        '''
        muestra = self.muestra
            
        alto_arreglo = len(muestra)
        ancho_arreglo = len(muestra[0])

        cant_values = ancho_arreglo * alto_arreglo

        b = np.reshape(muestra, (1,cant_values))
        b.sort()

        moda = []
        aux = 0
        contador = 0

        for i in b[0]:
          
            for g in b[0]:
               
                if g == i:

                    contador +=1 
                 

            if contador>aux:
                
                for z in range(len(moda)):
                    moda.pop()
                aux = contador

                if i not in moda:
                    moda.append(i)

            if contador == aux:
                
                if i not in moda:

                    moda.append(i)

            contador = 0

        if len(moda) != cant_values:
            return 'Moda: {}'.format(moda)

        else:
            return 'No existe moda para este arreglo'


  

    #########################################################################
    # Calcular varianza de un arreglo
    #########################################################################


    def varianza(self, muestra):

        muestra = self.muestra

        alto_arreglo = len(muestra)
        ancho_arreglo = len(muestra[0])

        cant_values = ancho_arreglo * alto_arreglo

        b = np.reshape(muestra, (1,cant_values))

        sumatoria = 0

        for i in b[0]:
            sumatoria += i

        media = sumatoria/cant_values

        aux = 0
        
        for i in b[0]:
            aux += (i-media)**2

        varianza = aux/cant_values

        return varianza



    #########################################################################
    #########################################################################


    def varianza_np(self, muestra):
        muestra = self.muestra

        return np.var(muestra)



    #########################################################################
    # Calcular desvio estandar de un arreglo
    #########################################################################

    def desvio_estandar(self, muestra):

        varianza = varianza(muestra)

        return varianza**(0.5)




