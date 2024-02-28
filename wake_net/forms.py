from flask_wtf import FlaskForm as Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class WakeUpForm(Form):
    mac = StringField('Mac Address', validators=[DataRequired(), Length(min=12, max=17)])
    submit = SubmitField()


class AddDeviceForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    mac = StringField('Mac Address', validators=[DataRequired(), Length(min=12, max=17)])
    ip = StringField('IP Address', validators=[DataRequired(), Length(min=15, max=15)])
    netmask = StringField('Netmask', validators=[DataRequired(), Length(min=15, max=15)])
    submit = SubmitField()
