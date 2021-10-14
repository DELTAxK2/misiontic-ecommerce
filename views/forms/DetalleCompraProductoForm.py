#Importación de clase Flask para desarrollo de Formularios
from flask_wtf import FlaskForm, form
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired


class DetalleCompraProducto(FlaskForm):
    compra = StringField('Codigo Compra', validators=[InputRequired()])
    producto = StringField('Codigo Producto', validators=[InputRequired()])
    cantidad = FloatField('Cantidad', validators=[InputRequired()])
    valor = FloatField('Valor', validators=[InputRequired()])