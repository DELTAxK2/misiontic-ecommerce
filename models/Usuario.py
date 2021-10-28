import sqlite3
from views.forms import UsuarioForm as form
from flask import render_template, session
from datetime import datetime
from werkzeug.security import check_password_hash as checkph
from werkzeug.security import generate_password_hash as genph

class Usuario:

    def __init__(self):
        print("Usuario Instanciado")

    def index(self, menu):
        data = form.UsuarioForm()
        lista = self.getAll()
        cant_elements = 0
        if len(lista) > 0 : cant_elements = len(lista[0]) + 1
        if session.get('menu') is not None:
            return render_template('UsuarioView.html', form=[data, lista, cant_elements, menu])
        else:
            return render_template('LoginView.html')


    def login(self, request):
        user = request.args['user']
        password = request.args['password']
        rows = None
        if request.method == 'GET':
            try:
                with sqlite3.connect('db/ecommerceDB.db') as connection:
                    cur = connection.cursor()
                    query = 'SELECT u.* FROM usuarios u WHERE u.user = ? AND u.estado = ?'
                    cur.execute(query, (user, 1))
                    rows = cur.fetchone()
                    flag = checkph(rows[13], password)
                    if flag:
                        return rows
                    else:
                        return None
            except BaseException as e:
                print('Error al intentar obtener Usuario ' + e.__str__())
                return rows


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
                    return True
            except BaseException as e:
                return 'Error al intentar registrar Usuario '+e.__str__()

    def get(self, request):
        if request.method == 'GET':
            rows = None
            try:
                with sqlite3.connect('db/ecommerceDB.db') as connection:
                    cur = connection.cursor()
                    query = 'SELECT * FROM usuarios WHERE estado = 1 AND id = ?'
                    cur.execute(query, (request.args['id']))
                    rows = cur.fetchone()
                return rows
            except BaseException as e:
                return 'Error al intentar registrar Usuario ' + e.__str__()


    def update(self, request):
        info = form.UsuarioForm()
        if request.method == 'PUT':
            id = request.args['id']
            tipo_id = request.args['tipo_id']
            identificacion = request.args['identificacion']
            nombre1 = request.args['nombre1']
            nombre2 = request.args['nombre2']
            apellido1 = request.args['apellido1']
            apellido2 = request.args['apellido2']
            email = request.args['email']
            telefono = request.args['telefono']
            celular = request.args['celular']
            direccion = request.args['direccion']
            id_rol = request.args['id_rol']
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'UPDATE usuarios SET tipo_id = ?, identificacion = ?, nombre1 = ?, nombre2 = ?, apellido1 = ?, ' \
                            'apellido2 = ?, email = ?, telefono = ?, celular = ?, direccion = ?, id_rol = ? WHERE id = ?'
                    data = (tipo_id, identificacion, nombre1, nombre2, apellido1, apellido2, email, telefono, celular,
                            direccion, id_rol, id)
                    cur.execute(query, data)
                    conexion.commit()
                    return True
            except BaseException as e:
                return 'Error al intentar registrar Usuario '+e.__str__()


    def delete(self, request):
        if request.method == 'DELETE':
            try:
                with sqlite3.connect('db/ecommerceDB.db') as conexion:
                    cur = conexion.cursor()
                    query = 'UPDATE usuarios SET estado = 2 WHERE id = ?'
                    cur.execute(query, (request.args['id']))
                    conexion.commit()
                    return True
            except BaseException as e:
                return 'Error al intentar registrar Usuario '+e.__str__()

    def getAll(self):
        rows = None
        with sqlite3.connect('db/ecommerceDB.db') as connection:
            cur = connection.cursor()
            query = 'SELECT ' \
                    'u.id AS ID, t.nombre AS TIPO_ID, u.identificacion IDENTIFICACION, u.nombre1 AS NOMBRE1, ' \
                    'u.nombre2 AS NOMBRE2, u.apellido1 AS APELLIDO1, u.apellido2 AS APELLIDO2, u.email AS EMAIL, ' \
                    'u.telefono AS TELEFONO, u.celular AS CELULAR, u.direccion AS DIRECCION, r.nombre AS ROL, ' \
                    'u.fecha_registro AS FECHA_REG ' \
                    'FROM usuarios u ' \
                    'INNER JOIN tipos_identificacion t ON t.id = u.tipo_id ' \
                    'INNER JOIN roles r ON r.id = u.id_rol ' \
                    'WHERE u.estado = 1'
            cur.execute(query)
            rows = cur.fetchall()
        return rows