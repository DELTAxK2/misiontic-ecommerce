#Importación de clase Flask para desarrollo de Formularios
from flask_wtf import FlaskForm, form
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired


class CompraForm(FlaskForm):
    usuario = StringField('Usuario (Identificación)', validators=[InputRequired()])
    proveedor = StringField('Proveedor (Nit)', validators=[InputRequired()])
    valor_total = FloatField('Valor Total', validators=[InputRequired()])
    impuesto = FloatField('Impuesto(%)')