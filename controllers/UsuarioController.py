import sqlite3
from views.forms import UsuarioForm as form
from flask import render_template
from datetime import datetime

class UsuarioController:

    def __init__(self):
        print("Usuario Instanciado")

    def index(self):
        data = form.UsuarioForm()
        lista = self.getAll()
        cant_elements = 0
        if len(lista)>0: cant_elements = len(lista[0])
        return render_template('UsuarioView.html', form=[data, lista, len(lista[0])])

    def save(self, request):
        info = form.UsuarioForm()
        if request.method == 'POST':
            tipo_id = info.tipo_id.data
            identificacion = info.identificacion.data
            nombre1 = info.nombre1.data
            nombre2 = info.nombre2.data
            apellido1 = info.apellido1.data
            apellido2 = info.apellido2.data
            email = info.email.data
            telefono = info.telefono.data
            celular = info.celular.data
            direccion = info.direccion.data
            id_rol = info.id_rol.data
            fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:?")
            usuario_registro = 1
            estado = 1
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'INSERT INTO usuarios (tipo_id, identificacion, nombre1, nombre2, apellido1, apellido2, ' \
                            'email, telefono, celular, direccion, id_rol, fecha_registro, usuario_registro, estado) VALUES' \
                            '(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
                    data = (tipo_id, identificacion, nombre1, nombre2, apellido1, apellido2, email, telefono, celular,
                            direccion, id_rol, fecha_registro, usuario_registro, estado)
                    cur.execute(query, data)
                    conexion.commit()
                    return 'Usuario Guardado exitosamente'
            except BaseException as e:
                return 'Error al intentar registrar Usuario '+e.__str__()

    def get(self, request, id):
        if request.method == 'GET':
            rows = None
            try:
                with sqlite3.connect('db/ecommerceDB.db') as connection:
                    cur = connection.cursor()
                    query = 'SELECT * FROM usuarios WHERE estado = 1 AND identificacion = ?'
                    cur.execute(query, (id))
                    rows = cur.fetchone()
                return rows
            except BaseException as e:
                return 'Error al intentar registrar Usuario ' + e.__str__()


    def update(self, request):
        info = form.UsuarioForm()
        if request.method == 'PUT':
            id = info.id.data
            tipo_id = info.tipo_id.data
            identificacion = info.identificacion.data
            nombre1 = info.nombre1.data
            nombre2 = info.nombre2.data
            apellido1 = info.apellido1.data
            apellido2 = info.apellido2.data
            email = info.email.data
            telefono = info.telefono.data
            celular = info.celular.data
            direccion = info.direccion.data
            id_rol = info.id_rol.data
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'UPDATE usuarios SET tipo_id = ?, identificacion = ?, nombre1 = ?, nombre2 = ?, apellido1 = ?, ' \
                            'apellido2 = ?, email = ?, telefono = ?, celular = ?, direccion = ?, id_rol = ? WHERE id = ?'
                    data = (tipo_id, identificacion, nombre1, nombre2, apellido1, apellido2, email, telefono, celular,
                            direccion, id_rol, id)
                    cur.execute(query, data)
                    conexion.commit()
                    return 'Usuario actualizado exitosamente'
            except BaseException as e:
                return 'Error al intentar registrar Usuario '+e.__str__()


    def delete(self, request, id):
        if request.method == 'DELETE':
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'UPDATE usuarios SET estado = 2 WHERE id = ?'
                    cur.execute(query, (id))
                    conexion.commit()
                    return 'Usuario Eliminado exitosamente'
            except BaseException as e:
                return 'Error al intentar registrar Usuario '+e.__str__()

    def getAll(self):
        rows = None
        with sqlite3.connect('db/ecommerceDB.db') as connection:
            cur = connection.cursor()
            query = 'SELECT * FROM usuarios WHERE estado = 1'
            cur.execute(query)
            rows = cur.fetchall()
        return rows