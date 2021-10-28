import sqlite3
from views.forms import ProveedorForm as form
from flask import render_template, session
from datetime import datetime

class Proveedor:

    def __init__(self):
        print("Proveedor Instanciado")

    def index(self, menu):
        data = form.ProveedorForm()
        lista = self.getAll()
        cant_elements = 0
        if len(lista) > 0: cant_elements = len(lista[0]) + 1
        if session.get('menu') is not None:
            return render_template('ProveedorView.html', form=[data, lista, cant_elements, menu])
        else:
            return render_template('LoginView.html')

    def save(self, request):
        info = form.ProveedorForm()
        if request.method == 'POST':
            nit = info.nit.data
            razon_social = info.razon_social.data
            telefono = info.telefono.data
            correo_electronico = info.correo_electronico.data
            contacto = info.contacto.data
            fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:?")
            usuario_registro = 1
            estado = 1
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'INSERT INTO proveedores (nit, razon_social, telefono, correo_electronico, contacto, ' \
                            'fecha_registro, usuario_registro, estado) VALUES' \
                            '(?, ?, ?, ?, ?, ?, ?, ?)'
                    data = (nit, razon_social, telefono, correo_electronico, contacto, fecha_registro, usuario_registro, estado)
                    cur.execute(query, data)
                    conexion.commit()
                    return 'Proveedor Guardado exitosamente'
            except BaseException as e:
                return 'Error al intentar registrar Proveedor '+e.__str__()

    def get(self, request, id):
        if request.method == 'GET':
            rows = None
            try:
                with sqlite3.connect('db/ecommerceDB.db') as connection:
                    cur = connection.cursor()
                    query = 'SELECT * FROM proveedores WHERE estado = 1 AND identificacion = ?'
                    cur.execute(query, (id))
                    rows = cur.fetchone()
                return rows
            except BaseException as e:
                return 'Error al intentar registrar Proveedor ' + e.__str__()


    def update(self, request):
        info = form.ProveedorForm()
        if request.method == 'PUT':
            id = info.id.data
            nit = info.nit.data
            razon_social = info.razon_social.data
            telefono = info.telefono.data
            correo_electronico = info.correo_electronico.data
            contacto = info.contacto.data
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'UPDATE proveedores SET nit = ?, razon_social = ?, telefono = ?, correo_electronico = ?, contacto = ? WHERE id = ?'
                    data = (nit, razon_social, telefono, correo_electronico, contacto)
                    cur.execute(query, data)
                    conexion.commit()
                    return 'Proveedor actualizado exitosamente'
            except BaseException as e:
                return 'Error al intentar registrar Usuario '+e.__str__()


    def delete(self, request, id):
        if request.method == 'DELETE':
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'UPDATE proveedores SET estado = 2 WHERE id = ?'
                    cur.execute(query, (id))
                    conexion.commit()
                    return 'Proveedor Eliminado exitosamente'
            except BaseException as e:
                return 'Error al intentar registrar Usuario '+e.__str__()

    def getAll(self):
        rows = None
        with sqlite3.connect('db/ecommerceDB.db') as connection:
            cur = connection.cursor()
            query = 'SELECT * FROM proveedores WHERE estado = 1'
            cur.execute(query)
            rows = cur.fetchall()
        return rows