#Importación de clase Flask para desarrollo de Formularios
from flask_wtf import FlaskForm, form
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired


class VentaForm(FlaskForm):
    usuario = StringField('Usuario (Identificación)', validators=[InputRequired()])
    valor_total = FloatField('Valor', validators=[InputRequired()])
    impuesto = FloatField('Impuesto(%)')
    descuento = FloatField('Descuento(%)')