#Importación de clase Flask para desarrollo de Formularios
from flask_wtf import FlaskForm, form
from wtforms import StringField, SelectField, SubmitField, TextAreaField,FloatField,FloatField,FileField
from wtforms.validators import InputRequired
from wtforms.fields.html5 import TelField


class ProductoForm(FlaskForm):

    nombre = StringField('Nombre', validators=[InputRequired()])
    descripcion = TextAreaField('Descripcion')
    valor_compra = FloatField('Valor Compra', validators=[InputRequired()])
    precio_venta = FloatField('Precio Venta', validators=[InputRequired()])
    existencias = StringField('Existencias', validators=[InputRequired()])
    imagen = FileField('Imagen')
    #fecha_registro = StringField('fecha_registro')
    #usuario_registro = StringField('usuario_registro')
    #estado = StringField('estado')
    #btnRegistrar = SubmitField('Registrar', render_kw={"class": "btn btn-primary"})


