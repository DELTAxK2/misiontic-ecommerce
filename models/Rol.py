import sqlite3

class Rol:

    def __init__(self):
        print("Rol Instanciado")

    def getAll(self):
        rows = None
        try:
            with sqlite3.connect('db/ecommerceDB.db') as connection:
                cur = connection.cursor()
                query = 'SELECT * FROM roles WHERE estado = 1'
                cur.execute(query)
                rows = cur.fetchall()
        except BaseException as e:
            return 'Error al intentar obtener Roles ' + e.__str__()
        return rows

    def selectHtml(self):
        result = [('#', 'Seleccione opción')]
        for val in self.getAll():
            result.append((val[0], val[1]))
        return result

    def getMenu(self, usuario):
        rows = None
        try:
            with sqlite3.connect('db/ecommerceDB.db') as connection:
                cur = connection.cursor()
                query = 'SELECT m.* FROM menu m INNER JOIN detalle_menu_rol d ON d.id_menu = m.id ' \
                        'INNER JOIN usuarios u ON u.id_rol = d.id_rol WHERE u.id = ? AND u.estado = 1 AND m.estado = 1 ' \
                        'ORDER BY m.orden ASC'
                cur.execute(query, (str(usuario)))
                rows = cur.fetchall()
        except BaseException as e:
            return 'Error al intentar obtener las opciones de Menú ' + e.__str__()
        return rows