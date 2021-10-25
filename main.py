from builtins import len

from flask import Flask, jsonify, request, render_template, session
from controllers.UsuarioController import UsuarioController
from controllers.ProductoController import ProductoController
from controllers.RolController import RolController
from controllers.CompraController import CompraController
from controllers.DetalleCompraProductoController import DetalleCompraProductoController
from controllers.DetalleVentaProductoController import DetalleVentaProductoController
from controllers.ProveedorController import ProveedorController
from controllers.VentaController import VentaController

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
compra_ctrl = CompraController()

@app.route('/compras/')
def homeCompra():
    return compra_ctrl.index(session['menu'])

@app.route('/compras/save')
def saveCompra():
    return compra_ctrl.save(request)

# ------ Detalle de la Compra ---------
detallecompra_ctrl = DetalleCompraProductoController()

@app.route('/detallecompras/')
def homeDetalleCompra():
    return detallecompra_ctrl.index(session['menu'])

@app.route('/detallecompras/save')
def saveDetalleCompra():
    return detallecompra_ctrl.save(request)

# ------ Venta ---------
venta_ctrl = VentaController()

@app.route('/ventas/')
def homeVenta():
    return venta_ctrl.index(session['menu'])

@app.route('/ventas/save')
def saveVenta():
    return venta_ctrl.save(request)

# ------ Detalle de la Venta ---------
detalleventa_ctrl = DetalleVentaProductoController()

@app.route('/detalleventas/')
def homeDetalleVenta():
    return detalleventa_ctrl.index(session['menu'])

@app.route('/detalleventas/save')
def saveDetalleVenta():
    return detalleventa_ctrl.save(request)

# ------ Proveedor ---------

proveedor_ctrl = ProveedorController()

@app.route('/proveedores/')
def homeProveedor():
    return proveedor_ctrl.index(session['menu'])

@app.route('/proveedores/save')
def saveProveedor():
    return proveedor_ctrl.save(request)

# ------ Usuarios ---------

usuario_ctrl = UsuarioController()

@app.route('/usuarios/')
def homeUsuario():
    return usuario_ctrl.index(session['menu'])

@app.route('/usuario/save')
def saveUsuario():
    return usuario_ctrl.save(request)

@app.route('/login/', methods=['GET'])
def logIn():
    view = ''
    output = ''
    if request.method == 'GET':
        usuario_data = usuario_ctrl.login(request)
        if usuario_data != None:
            rol_ctrl = RolController()
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

producto_ctrl = ProductoController()

@app.route('/productos/')
def homeProducto():
    return producto_ctrl.index(session['menu'])

@app.route('/productos/save')
def saveProducto():
    return producto_ctrl.save(request)

# -------- Exec --------

if __name__ == "__main__":
    app.run(debug=True)