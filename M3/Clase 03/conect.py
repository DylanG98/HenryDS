import mysql.connector

class conexion:

    def conectar(self, base):

    # Connect to the database
        credencial =    {
                        "host":'localhost',
                        "user":'root',
                        "password":'123456789',
                        "database": base,
                        "port":'3306'
                        }
        
        conect1 = None
        conect1 = mysql.connector.connect(**credencial) #pasa múltiples variables el **
        return conect1
    
    def execute(self, base, query):

        cone = self.conectar(base)

        cursor1 = cone.cursor()

        cursor1.execute(query)

  

    def execute_agregar(self, base, query, argumento):

        cone = self.conectar(base)

        cursor1 = cone.cursor()

        cursor1.execute(query, argumento)

        cone.commit()

        cone.close()


###### Hay que solucionar el commit automatico, xq no da lugar al error mío
###### Crear función con executemany para no usar el iterrows()