import pandas as pd
import mysql.connector

#df = pd.read_csv("oferta_gastronomica.csv", 'r')

'''columnas = { 'id_local':[], 
    'nombre':[],
    'categoria':[], 
    'direccion':[], 
    'barrio':[], 
    'comuna':[]}
'''
conexion = mysql.connector.connect(host='localhost',
                            user='user',
                            password='123456789',
                            database='gastronomiacaba')
                         