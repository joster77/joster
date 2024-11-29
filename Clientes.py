from Conexion import *

class CClientes:

    def mostrarClientes():
       
       try:

         cone = CConexion.ConexionBaseDeDatos()
         cursor = cone.cursor()
         cursor.execute("select *  from usuarios;")
         miresultado=cursor.fetchall()
         cone.commit()
         cone.close()

         return miresultado
        
       except mysql.connector.Error as error:
            print ("Error de mostrar datos::..()".format(error))

    def ingresarClientes(nombres, apellidos, sexo):

        try:

         cone = CConexion.ConexionBaseDeDatos()
         cursor = cone.cursor()
         sql="insert into usuarios values (null,%s,%s,%s);"
         # La variable valores tiene que ser una tupla
         # como mínima expresion es: (valor,) la coma hace que nsea una tupla
         # Las tuplas son listas inmutables, no se pueden modificar.
         valores=(nombres, apellidos, sexo)
         cursor.execute(sql, valores)
         cone.commit()
         print(cursor.rowcount,"Registro ingresado::..")
         cone.close()

        except mysql.connector.Error as error:
            print ("Error de ingreso de datos::..()".format(error))

    def modificarClientes(idUsuario,nombres, apellidos, sexo):

        try:

         cone = CConexion.ConexionBaseDeDatos()
         cursor = cone.cursor()
         sql="update usuarios U set U.nombres=%s, U.apellidos=%s, U.sexo=%s where U.id=%s;"

         valores=(nombres, apellidos, sexo, idUsuario)
         cursor.execute(sql, valores)
         cone.commit()
         print(cursor.rowcount,"Registro Actualizado::..")
         cone.close()

        except mysql.connector.Error as error:
            print ("Error de actualización de datos::..()".format(error))

    
    
    def eliminarClientes(idUsuario):

        try:

         cone = CConexion.ConexionBaseDeDatos()
         cursor = cone.cursor()
         sql="delete from usuarios u where u.id=%s;"

         valores=(idUsuario,)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Registro Eliminado::..")
         cone.close()

        except mysql.connector.Error as error:
            print ("Error de eliminación de datos::..()".format(error))