#Importación de clase Flask para desarrollo de Formularios
from flask_wtf import FlaskForm, form
from wtforms import StringField, SelectField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import InputRequired
from wtforms.fields.html5 import TelField, EmailField
from models.Rol import Rol
from models.TiposIdentificacion import TiposIdentificacion


class UsuarioForm(FlaskForm):
    t_ctrl = TiposIdentificacion()
    tipo_id = SelectField('Tipo Identificación', choices=t_ctrl.selectHtml(), validators=[InputRequired()])
    identificacion = StringField('Identificación', validators=[InputRequired()])
    nombre1 = StringField('Primer Nombre', validators=[InputRequired()])
    nombre2 = StringField('Segundo Nombre')
    apellido1 = StringField('Primer Apellido', validators=[InputRequired()])
    apellido2 = StringField('Segundo Apellido', validators=[InputRequired()])
    email = EmailField('Email')
    telefono = TelField('Telefono')
    celular = TelField('Celular')
    direccion = TextAreaField('Dirección')
    r_ctrl = Rol()
    id_rol = SelectField('Rol', choices=r_ctrl.selectHtml())


