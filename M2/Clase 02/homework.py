import math
import pandas as pd
import numpy as np

##############################################################
# PUNTO 1
##############################################################

Cep_1 = (2*1)**(10)
#print(Cep_1)

##############################################################
# PUNTO 2
##############################################################

def factorial(n):
    resultado = 1
    for i in range(1,n+1):
        resultado*=i

    return resultado


Cep_2 = factorial(10) / (factorial(3)*factorial(7))
#print(Cep_2)

##############################################################
# PUNTO 3
##############################################################

# a) Es frecuentista

# b) 

list_regiones = ['Norte','Noreste', 'Sur', 'Centro']
list_si = np.array([148, 162, 296, 252])
list_no = np.array([52, 54, 74, 48])

dicc = {
        'Region':list_regiones,
        'Si': list_si,
        'No': list_no
        } 

df = pd.DataFrame(dicc)
#print(df)

list_porcentaje_si = list_si*100/(list_si+list_no)
list_porcentaje_no = 100-list_porcentaje_si

df['Probabilidad si (%)'] = list_porcentaje_si
df['Probabilidad no (%)'] = list_porcentaje_no

#print(df)

# c) La frecuentista

# d) Si es satisfecho 

# e) 

def porc_max(df):
    for region,probabilidad in enumerate(df['Probabilidad si (%)']):

        if probabilidad == df['Probabilidad si (%)'].max():
            return print('La region donde mas se usa el cinturon es {}'.format(df['Region'][region]))


#porc_max(df)


tipo= ['Trebol','Pica','Corazon','Diamante','Negra','Roja']
cantidad = [13,13,13,13,26,26]

maso = {'Tipo': tipo,
        'Cantidad': cantidad}

df = pd.DataFrame(maso)



def proba (df):
    total_maso = 52
    df['Probabilidad (en %)'] = df ['Cantidad']*100/total_maso
    
    
    return print(df)

#######

### 2*4/52*100
 
def mundial():

    cant_equipos = 32
    prob_win = 1/cant_equipos*100

    return print('La probabilidad de cada equipo de ganar es: ',prob_win, '%')
mundial()




    








