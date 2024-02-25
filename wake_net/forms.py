from flask_wtf import FlaskForm as Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class WakeUpForm(Form):
    mac = StringField('Mac Address', validators=[DataRequired(), Length(min=12, max=17)])
    submit = SubmitField()
