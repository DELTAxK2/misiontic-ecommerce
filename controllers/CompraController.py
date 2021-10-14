import sqlite3
from views.forms import CompraForm as form
from flask import render_template
from datetime import datetime

class CompraController:

    def __init__(self):
        print("Compra Instanciada")

    def index(self, menu):
        data = form.CompraForm()
        lista = self.getAll()
        cant_elements = 0
        if len(lista)>0: cant_elements = len(lista[0])
        return render_template('CompraView.html', form=[data, lista, cant_elements, menu])

    def save(self, request):
        info = form.CompraForm()
        if request.method == 'POST':
            id_usuario = info.usuario.data
            id_proveedor = info.proveedor.data
            valor_total = info.valor_total.data
            impuesto = info.impuesto.data
            fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            usuario_registro = 1
            estado = 1
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'INSERT INTO compras (id_usuario, id_proveedor, valor_total, impuestos, ' \
                            'fecha_registro, usuario_registro, estado) VALUES (?, ?, ?, ?, ?, ?, ?)'
                    data = (id_usuario, id_proveedor, valor_total, impuesto, fecha_registro, usuario_registro, estado)
                    cur.execute(query, data)
                    conexion.commit()
                    return 'Compra Realizada exitosamente'
            except BaseException as e:
                return 'Error al intentar registrar la compra '+e.__str__()

    def get(self, request, id):
        if request.method == 'GET':
            rows = None
            try:
                with sqlite3.connect('db/ecommerceDB.db') as connection:
                    cur = connection.cursor()
                    query = 'SELECT * FROM compras WHERE estado = 1 AND id = ?'
                    cur.execute(query, (id))
                    rows = cur.fetchone()
                return rows
            except BaseException as e:
                return 'Error al intentar obtener la compra ' + e.__str__()


    def update(self, request):
        info = form.CompraForm()
        if request.method == 'PUT':
            id = info.id.data
            id_usuario = info.usuario.data
            id_proveedor = info.proveedor.data
            valor_total = info.valor_total.data
            impuesto = info.impuesto.data
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'UPDATE compras SET id_usuario = ?, descripcion = ?, valor_total = ?, impuesto = ? WHERE id = ?'
                    data = (id_usuario, id_proveedor, valor_total, impuesto, id)
                    cur.execute(query, data)
                    conexion.commit()
                    return 'Compra modificada exitosamente'
            except BaseException as e:
                return 'Error al intentar actualizar la compra '+e.__str__()


    def delete(self, request, id):
        if request.method == 'DELETE':
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'UPDATE compras SET estado = 2 WHERE id = ?'
                    cur.execute(query, (id))
                    conexion.commit()
                    return 'Compra eliminada exitosamente'
            except BaseException as e:
                return 'Error al intentar eliminar la compra '+e.__str__()

    def getAll(self):
        rows = None
        with sqlite3.connect('db/ecommerceDB.db') as connection:
            cur = connection.cursor()
            query = 'SELECT * FROM compras WHERE estado = 1'
            cur.execute(query)
            rows = cur.fetchall()
        return rows