import sqlite3
from views.forms import VentaForm as form
from flask import render_template, session
from datetime import datetime

class Venta:

    def __init__(self):
        print("Venta Instanciada")

    def index(self, menu):
        data = form.VentaForm()
        lista = self.getAll()
        cant_elements = 0
        if len(lista) > 0 : cant_elements = len(lista[0]) + 1
        if session.get('menu') is not None:
            return render_template('VentaView.html', form=[data, lista, cant_elements, menu])
        else:
            return render_template('LoginView.html')

    def save(self, request):
        info = form.VentaForm()
        if request.method == 'POST':
            id_usuario = info.usuario.data
            valor_total = info.valor_total.data
            impuesto = info.impuesto.data
            descuento = info.descuento.data
            fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            usuario_registro = 1
            estado = 1
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'INSERT INTO ventas (id_usuario, valor_total, impuestos, descuento, ' \
                            'fecha_registro, usuario_registro, estado) VALUES (?, ?, ?, ?, ?, ?, ?)'
                    data = (id_usuario, valor_total, impuesto, descuento, fecha_registro, usuario_registro, estado)
                    cur.execute(query, data)
                    conexion.commit()
                    return 'Venta Realizada exitosamente'
            except BaseException as e:
                return 'Error al intentar registrar la venta '+e.__str__()

    def get(self, request, id):
        if request.method == 'GET':
            rows = None
            try:
                with sqlite3.connect('db/ecommerceDB.db') as connection:
                    cur = connection.cursor()
                    query = 'SELECT * FROM ventas WHERE estado = 1 AND id = ?'
                    cur.execute(query, (id))
                    rows = cur.fetchone()
                return rows
            except BaseException as e:
                return 'Error al intentar obtener la venta ' + e.__str__()


    def update(self, request):
        info = form.VentaForm()
        if request.method == 'PUT':
            id = info.id.data
            id_usuario = info.usuario.data
            valor_total = info.valor_total.data
            impuesto = info.impuesto.data
            descuento = info.descuento.data
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'UPDATE ventas SET id_usuario = ?, descripcion = ?, valor_total = ?, impuesto = ? WHERE id = ?'
                    data = (id_usuario, valor_total, impuesto, descuento, id)
                    cur.execute(query, data)
                    conexion.commit()
                    return 'Venta modificada exitosamente'
            except BaseException as e:
                return 'Error al intentar actualizar la venta '+e.__str__()


    def delete(self, request, id):
        if request.method == 'DELETE':
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'UPDATE ventas SET estado = 2 WHERE id = ?'
                    cur.execute(query, (id))
                    conexion.commit()
                    return 'Venta eliminada exitosamente'
            except BaseException as e:
                return 'Error al intentar eliminar la venta '+e.__str__()

    def getAll(self):
        rows = None
        with sqlite3.connect('db/ecommerceDB.db') as connection:
            cur = connection.cursor()
            query = 'SELECT * FROM ventas WHERE estado = 1'
            cur.execute(query)
            rows = cur.fetchall()
        return rows