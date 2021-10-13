import sqlite3

class RolController:

    def __init__(self):
        print("Rol Instanciado")

    def getAll(self):
        rows = None
        with sqlite3.connect('db/ecommerceDB.db') as connection:
            cur = connection.cursor()
            query = 'SELECT * FROM roles WHERE estado = 1'
            cur.execute(query)
            rows = cur.fetchall()
        return rows

    def selectHtml(self):
        result = [('#', 'Seleccione opción')]
        for val in self.getAll():
            result.append((val[0], val[1]))
        return result