#Importación de clase Flask para desarrollo de Formularios
from flask_wtf import FlaskForm, form
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired
from wtforms.fields.html5 import TelField, EmailField


class ProveedorForm(FlaskForm):
    nit = StringField('Nit', validators=[InputRequired()])
    razon_social = StringField('Razón Social', validators=[InputRequired()])
    telefono = TelField('Telefono')
    correo_electronico = EmailField('Email')
    contacto = StringField('Contacto', validators=[InputRequired()])