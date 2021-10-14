from flask import Flask, jsonify, request, render_template
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

@app.route('/')
def home():
    return render_template('helpers/Template.html')

# ---- Generación de Menu ----
usuario_session = 1
rol_ctrl = RolController()
menu = rol_ctrl.getMenu(usuario_session)

# ------ Compra ---------
compra_ctrl = CompraController()

@app.route('/compras/')
def homeCompra():
    return compra_ctrl.index(menu)

@app.route('/compras/save')
def saveCompra():
    return compra_ctrl.save(request)

# ------ Detalle de la Compra ---------
detallecompra_ctrl = DetalleCompraProductoController()

@app.route('/detallecompras/')
def homeDetalleCompra():
    return detallecompra_ctrl.index(menu)

@app.route('/detallecompras/save')
def saveDetalleCompra():
    return detallecompra_ctrl.save(request)

# ------ Venta ---------
venta_ctrl = VentaController()

@app.route('/ventas/')
def homeVenta():
    return venta_ctrl.index(menu)

@app.route('/ventas/save')
def saveVenta():
    return venta_ctrl.save(request)

# ------ Detalle de la Venta ---------
detalleventa_ctrl = DetalleVentaProductoController()

@app.route('/detalleventas/')
def homeDetalleVenta():
    return detalleventa_ctrl.index(menu)

@app.route('/detalleventas/save')
def saveDetalleVenta():
    return detalleventa_ctrl.save(request)

# ------ Proveedor ---------

proveedor_ctrl = ProveedorController()

@app.route('/proveedores/')
def homeProveedor():
    return proveedor_ctrl.index(menu)

@app.route('/proveedores/save')
def saveProveedor():
    return proveedor_ctrl.save(request)

# ------ Usuarios ---------

usuario_ctrl = UsuarioController()

@app.route('/usuarios/')
def homeUsuario():
    return usuario_ctrl.index(menu)

@app.route('/usuario/save')
def saveUsuario():
    return usuario_ctrl.save(request)

# ----- Productos ---------

producto_ctrl = ProductoController()

@app.route('/productos/')
def homeProducto():
    return producto_ctrl.index(menu)

@app.route('/productos/save')
def saveProducto():
    return producto_ctrl.save(request)

# -------- Exec --------

if __name__ == "__main__":
    app.run(debug=True)
