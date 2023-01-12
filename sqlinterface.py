import sqlite3

miconexion = sqlite3.connect("tabla_api_juego") #si no existe bbdd se crea una nueva

class Conexion:
    def __init__(self, base, tabla):
        self.base = base
        self.tabla = tabla
        self.__conexion = self.conectar()
        self._cursor = self.cursor()

    def conectar(self):
        conexion = sqlite3.connect(self.base)
        return conexion

    def cursor(self):
        cursor = self.__conexion.cursor()
        return cursor

    def consulta(self, consulta):
        consulta = self._cursor.execute(consulta)
        consulta = consulta.fetchall()
        self.cierre()
        return consulta


    def commit(self):
        self.__conexion.commit()
        return True

    def cierre(self):
        self.__conexion.close()
        return True


