from flask_wtf import FlaskForm as Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class WakeUpForm(Form):
    mac = StringField('Mac Address', validators=[DataRequired(), Length(min=12, max=17)])
    submit = SubmitField()


class DeviceForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    mac = StringField('Mac Address', validators=[DataRequired(), Length(min=12, max=17)])
    ip = StringField('IP Address', validators=[DataRequired(), Length(min=7, max=15)])
    netmask = StringField('Netmask', validators=[DataRequired(), Length(min=7, max=15)])
    submit = SubmitField()

class EditDeviceForm(DeviceForm):
    submit = SubmitField('Edit')

class AddDeviceForm(DeviceForm):
    submit = SubmitField('Add')
