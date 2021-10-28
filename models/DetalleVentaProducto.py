import sqlite3
from views.forms import DetalleVentaProductoForm as form
from flask import render_template, session
from datetime import datetime

class DetalleVentaProducto:

    def __init__(self):
        print("Detalle de Venta Instanciada")

    def index(self, menu):
        data = form.DetalleVentaProductoForm()
        lista = self.getAll()
        cant_elements = 0
        if len(lista)>0 : cant_elements = len(lista[0])+1
        if session.get('menu') is not None:
            return render_template('DetalleVentaProductoView.html', form=[data, lista, cant_elements, menu])
        else:
            return render_template('LoginView.html')

    def save(self, request):
        info = form.DetalleVentaProductoForm()
        if request.method == 'POST':
            id_producto = info.id_producto.data
            id_venta = info.id_venta.data
            cantidad = info.cantidad.data
            valor = info.valor.data
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'INSERT INTO detalle_venta_producto (id_producto, id_venta, cantidad, valor) VALUES (?, ?, ?, ?)'
                    data = (id_producto, id_venta, cantidad, valor)
                    cur.execute(query, data)
                    conexion.commit()
                    return 'Detalle de la venta guardada exitosamente'
            except BaseException as e:
                return 'Error al intentar registrar Detalle de la venta '+e.__str__()

    def get(self, request, id):
        if request.method == 'GET':
            rows = None
            try:
                with sqlite3.connect('db/ecommerceDB.db') as connection:
                    cur = connection.cursor()
                    query = 'SELECT * FROM detalle_venta_producto WHERE estado = 1 AND identificacion = ?'
                    cur.execute(query, (id))
                    rows = cur.fetchone()
                return rows
            except BaseException as e:
                return 'Error al intentar obtener Detalle de la venta ' + e.__str__()


    def update(self, request):
        info = form.DetalleVentaProductoForm()
        if request.method == 'PUT':
            id = info.id.data
            id_producto = info.id_producto.data
            id_venta = info.id_venta.data
            cantidad = info.cantidad.data
            valor = info.valor.data
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'UPDATE detalle_venta_producto SET id_producto = ?, id_venta = ?, cantidad = ?, valor = ? WHERE id = ?'
                    data = (id_producto, id_venta, cantidad, valor, id)
                    cur.execute(query, data)
                    conexion.commit()
                    return 'Detalle de la venta actualizada exitosamente'
            except BaseException as e:
                return 'Error al intentar actualizar Detalle de la venta '+e.__str__()


    def delete(self, request, id):
        if request.method == 'DELETE':
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'UPDATE detalle_venta_producto SET estado = 2 WHERE id = ?'
                    cur.execute(query, (id))
                    conexion.commit()
                    return 'Detalle de la venta eliminada exitosamente'
            except BaseException as e:
                return 'Error al intentar eliminar Detalle de la venta '+e.__str__()

    def getAll(self):
        rows = None
        with sqlite3.connect('db/ecommerceDB.db') as connection:
            cur = connection.cursor()
            query = 'SELECT * FROM detalle_venta_producto WHERE estado = 1'
            cur.execute(query)
            rows = cur.fetchall()
        return rows