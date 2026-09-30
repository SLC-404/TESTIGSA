from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional

from app.models import STATUSES


class TaskForm(FlaskForm):
    title = StringField("Título", validators=[DataRequired(message="Escribe el título"),
                                              Length(max=150)])
    description = TextAreaField("Descripción", validators=[Optional()])
    status = SelectField("Estatus", choices=list(STATUSES.items()), default="pending")
    submit = SubmitField("Guardar")
