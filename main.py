from flask import Flask, jsonify, request, render_template
from controllers.UsuarioController import UsuarioController
from controllers.ProductoController import ProductoController
from flask_bootstrap import Bootstrap
import os

# ----- App Configuration ----
app = Flask(__name__, template_folder='views')
Bootstrap(app)
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return render_template('helpers/Template.html')

# ------ Usuarios ---------
usuario_ctrl = UsuarioController()

@app.route('/usuario/')
def homeUsuario():
    return usuario_ctrl.index()

@app.route('/usuario/save')
def saveUsuario():
    return usuario_ctrl.save(request)

# ----- Productos ---------

producto_ctrl = ProductoController()

@app.route('/productos/')
def homeProducto():
    return producto_ctrl.index()

@app.route('/productos/save')
def saveProducto():
    return producto_ctrl.save(request)

# -------- Exec --------

if __name__ == "__main__":
    app.run(debug=True)
