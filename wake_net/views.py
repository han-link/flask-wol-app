# views.py
from flask import Blueprint, render_template
from wake_net.forms import WakeUpForm, AddDeviceForm
from .wakeonlan import send_magic_packet

# Define a Blueprint named 'main'. This can be named anything.
main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    wake_up_form = WakeUpForm()
    if wake_up_form.validate_on_submit():
        send_magic_packet(wake_up_form.mac.data)

    return render_template('index.html', wake_up_form=wake_up_form)

@main.route('/addDevice', methods=['GET', 'POST'])
def add_device():
    add_device_form = AddDeviceForm()
    if add_device_form.validate_on_submit():
        pass

    return render_template('addDevice.html', add_device_form=add_device_form)