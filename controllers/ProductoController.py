import sqlite3
from views.forms import ProductoForm as form
from flask import render_template
from datetime import datetime

class ProductoController:

    def __init__(self):
        print("Producto Instanciado")

    def index(self):
        data = form.ProductoForm()
        lista = self.getAll()
        cant_elements = 0
        if len(lista)>0: cant_elements = len(lista[0])
        return render_template('ProductoView.html', form=[data, lista, cant_elements])

    def save(self, request):
        info = form.ProductoForm()
        if request.method == 'POST':
            nombre = info.nombre.data
            descripcion = info.descripcion.data
            valor_compra = info.valor_compra.data
            precio_venta = info.precio_venta.data
            existencias = info.existencias.data
            imagen = info.imagen.data
            fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:?")
            usuario_registro = 1
            estado = 1
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'INSERT INTO productos (nombre, descripcion, valor_compra, precio_venta, existencias, imagen, ' \
                            'fecha_registro, usuario_registro, estado) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
                    data = (nombre, descripcion, valor_compra, precio_venta, existencias, imagen, fecha_registro, usuario_registro, estado)
                    cur.execute(query, data)
                    conexion.commit()
                    return 'Producto Guardado exitosamente'
            except BaseException as e:
                return 'Error al intentar registrar Producto '+e.__str__()

    def get(self, request, id):
        if request.method == 'GET':
            rows = None
            try:
                with sqlite3.connect('db/ecommerceDB.db') as connection:
                    cur = connection.cursor()
                    query = 'SELECT * FROM productos WHERE estado = 1 AND identificacion = ?'
                    cur.execute(query, (id))
                    rows = cur.fetchone()
                return rows
            except BaseException as e:
                return 'Error al intentar registrar Producto ' + e.__str__()


    def update(self, request):
        info = form.ProductoForm()
        if request.method == 'PUT':
            id = info.id.data
            nombre = info.nombre.data
            descripcion = info.descripcion.data
            valor_compra = info.valor_compra.data
            precio_venta = info.precio_venta.data
            existencias = info.existencias.data
            imagen = info.imagen.data
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'UPDATE productos SET nombre = ?, descripcion = ?, valor_compra = ?, precio_venta = ?, existencias = ?, imagen = ? WHERE id = ?'
                    data = (nombre, descripcion, valor_compra, precio_venta, existencias, imagen, id)
                    cur.execute(query, data)
                    conexion.commit()
                    return 'Producto actualizado exitosamente'
            except BaseException as e:
                return 'Error al intentar registrar Producto '+e.__str__()


    def delete(self, request, id):
        if request.method == 'DELETE':
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'UPDATE productos SET estado = 2 WHERE id = ?'
                    cur.execute(query, (id))
                    conexion.commit()
                    return 'Producto Eliminado exitosamente'
            except BaseException as e:
                return 'Error al intentar registrar Producto '+e.__str__()

    def getAll(self):
        rows = None
        with sqlite3.connect('db/ecommerceDB.db') as connection:
            cur = connection.cursor()
            query = 'SELECT * FROM productos WHERE estado = 1'
            cur.execute(query)
            rows = cur.fetchall()
        return rows