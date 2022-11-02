import pandas as pd
import mysql.connector

df = pd.read_csv("oferta_gastronomica.csv")

columnas = { 'id_local':[], 
    'nombre':[],
    'categoria':[], 
    'direccion':[], 
    'barrio':[], 
    'comuna':[]}

columnas['id_local'] = df['id']
columnas['nombre'] = df['nombre']
columnas['categoria'] = df['categoria']
columnas['direccion'] = df['direccion_completa']
columnas['barrio'] = df['barrio']
columnas['comuna'] = df['comuna']

df1 = pd.DataFrame(columnas)

#df1.to_csv('restaurantescabacomma.csv', index=False,sep=',' ,encoding='utf-8')

'''conexion = mysql.connector.connect(host='localhost',
                            user='root',
                            password='123456789',
                            database='gastronomiacaba',
                            port='3306')

#mycursor = conexion.cursor()



#query = ("CREATE TABLE oferta_gastronomica (id_local INT PRIMARY KEY, nombre VARCHAR(50), categoria VARCHAR(50), direccion VARCHAR(50), barrio VARCHAR(50), comuna VARCHAR(50))")
                            
#query = ("INSERT INTO oferta_gastronomica (id_local,nombre,categoria,direccion,barrio,comuna) VALUES (1,'s','a','f','a','g') ")            

#query = ("INSERT INTO oferta_gastronomica (id_local,nombre,categoria,direccion,barrio,comuna) VALUES (?,?,?,?,?,?)")

#mycursor.execute(query)   

#conexion.commit()'''