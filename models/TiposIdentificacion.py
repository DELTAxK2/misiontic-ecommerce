import sqlite3

class TiposIdentificacion:

    def __init__(self):
        print("Tipo de Identificación Instanciado")

    def listAll(self):
        rows = None
        with sqlite3.connect('db/ecommerceDB.db') as connection:
            cur = connection.cursor()
            query = 'SELECT * FROM tipos_identificacion WHERE estado = 1'
            cur.execute(query)
            rows = cur.fetchall()
        return rows

    def selectHtml(self):
        result = [('#', 'Seleccione opción')]
        for val in self.listAll():
            result.append((val[0], val[2]))
        return result