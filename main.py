from builtins import len

from flask import Flask, jsonify, request, render_template, session
from models.Usuario import Usuario
from models.Producto import Producto
from models.Rol import Rol
from models.Compra import Compra
from models.DetalleCompraProducto import DetalleCompraProducto
from models.DetalleVentaProducto import DetalleVentaProducto
from models.Proveedor import Proveedor
from models.Venta import Venta

from flask_bootstrap import Bootstrap
import os

# ----- App Configuration ----
app = Flask(__name__, template_folder='views')
Bootstrap(app)
app.secret_key = os.urandom(24)

@app.before_request
def session_management():
  session.permanent = True

@app.route('/home/')
def home():
    return render_template('index.html')

# ---- Valores  ----
menu =  None

# ------ Compra ---------
compra_ctrl = Compra()

@app.route('/compras/')
def homeCompra():
    return compra_ctrl.index(session['menu'])

@app.route('/compras/get', methods=['GET'])
def getCompras():
    compra_data = compra_ctrl.get(request)
    if compra_data != None:
        output = dict(error=False, output=compra_data)
    else:
        output = dict(error=True, output='Compra no encontrada')
    return output

@app.route('/compras/save')
def saveCompra():
    return compra_ctrl.save(request)

# ------ Detalle de la Compra ---------
detallecompra_ctrl = DetalleCompraProducto()

@app.route('/detallecompras/')
def homeDetalleCompra():
    return detallecompra_ctrl.index(session['menu'])

@app.route('/detallecompras/save')
def saveDetalleCompra():
    return detallecompra_ctrl.save(request)

@app.route('/detallecompras/get', methods=['GET'])
def getDetalleCompras():
    compra_data = detallecompra_ctrl.get(request)
    if compra_data != None:
        output = dict(error=False, output=compra_data)
    else:
        output = dict(error=True, output='Detalles de compra no encontrada')
    return output

# ------ Venta ---------
venta_ctrl = Venta()

@app.route('/ventas/')
def homeVenta():
    return venta_ctrl.index(session['menu'])

@app.route('/ventas/save')
def saveVenta():
    return venta_ctrl.save(request)

@app.route('/ventas/get', methods=['GET'])
def getVentas():
    compra_data = venta_ctrl.get(request)
    if compra_data != None:
        output = dict(error=False, output=compra_data)
    else:
        output = dict(error=True, output='Venta no encontrada')
    return output

# ------ Detalle de la Venta ---------
detalleventa_ctrl = DetalleVentaProducto()

@app.route('/detalleventas/')
def homeDetalleVenta():
    return detalleventa_ctrl.index(session['menu'])

@app.route('/detalleventas/save')
def saveDetalleVenta():
    return detalleventa_ctrl.save(request)

@app.route('/detalleventas/get', methods=['GET'])
def getDetalleVentas():
    detalleventa_data = detalleventa_ctrl.get(request)
    if detalleventa_data != None:
        output = dict(error=False, output=detalleventa_data)
    else:
        output = dict(error=True, output='Detalles de venta no encontrada')
    return output
# ------ Proveedor ---------

proveedor_ctrl = Proveedor()

@app.route('/proveedores/')
def homeProveedor():
    return proveedor_ctrl.index(session['menu'])

@app.route('/proveedores/save')
def saveProveedor():
    return proveedor_ctrl.save(request)

@app.route('/proveedores/get', methods=['GET'])
def getProveedores():
    proveedores_data = proveedor_ctrl.get(request)
    if proveedores_data != None:
        output = dict(error=False, output=proveedores_data)
    else:
        output = dict(error=True, output='Proveedor no encontrado')
    return output
# ------ Usuarios ---------

usuario_ctrl = Usuario()

@app.route('/usuarios/')
def homeUsuario():
    return usuario_ctrl.index(session['menu'])

@app.route('/usuarios/save', methods=['POST'])
def saveUsuario():
    usuario_data = usuario_ctrl.save(request)
    if usuario_data == True:
        output = dict(error=False, output=usuario_data)
    else:
        output = dict(error=True, output='Usuario no guardado')
    return output

@app.route('/usuarios/update', methods=['PUT'],)
def updateUsuario():
    usuario_data = usuario_ctrl.update(request)
    if usuario_data == True:
        output = dict(error=False, output=usuario_data)
    else:
        output = dict(error=True, output='Usuario no actualizado')
    return output

@app.route('/usuarios/delete', methods=['DELETE'])
def deleteUsuario():
    usuario_data = usuario_ctrl.update(request)
    if usuario_data == True:
        output = dict(error=False, output=usuario_data)
    else:
        output = dict(error=True, output='Usuario no eliminado')
    return output

@app.route('/usuarios/get', methods=['GET'])
def getUsuario():
    usuario_data = usuario_ctrl.get(request)
    if usuario_data != None:
        output = dict(error=False, output=usuario_data)
    else:
        output = dict(error=True, output='Usuario no encontrado')
    return output

@app.route('/login/', methods=['GET'])
def logIn():
    view = ''
    output = ''
    if request.method == 'GET':
        usuario_data = usuario_ctrl.login(request)
        if usuario_data != None:
            rol_ctrl = Rol()
            session.clear()
            session["menu"] = rol_ctrl.getMenu(usuario_data[0])
            session["usuario_session"] = usuario_data[0]
            session["info_usuario"] = usuario_data[3]
            session["rol_session"] = usuario_data[11]
            session['user_is_logged'] = True
            output = dict(error=False, output=usuario_data)
        else:
            output = dict(error=True, output='El usuario y la contraseña suministrada no son consistentes')
    return output

@app.route('/', methods=['GET'])
def inciarsesion():
    output = None
    if menu is not None:
        session['user_is_logged'] = False
    return render_template('LoginView.html', output=output)

@app.route('/destroy_session', methods=['GET'])
def destroysession():
    session.clear()
    output = None
    return render_template('LoginView.html', output=output)
# ----- Productos ---------

producto_ctrl = Producto()

@app.route('/productos/')
def homeProducto():
    return producto_ctrl.index(session['menu'])

@app.route('/productos/save')
def saveProducto():
    return producto_ctrl.save(request)

@app.route('/productos/get', methods=['GET'])
def getProductos():
    producto_data = producto_ctrl.get(request)
    if producto_data != None:
        output = dict(error=False, output=producto_data)
    else:
        output = dict(error=True, output='Producto no encontrado')
    return output

# -------- Exec --------

if __name__ == "__main__":
    app.run(debug=True)