# views.py
from flask import Blueprint, render_template, redirect, url_for
from wake_net.forms import WakeUpForm, AddDeviceForm
from wakeonlan import send_magic_packet
from wake_net.models import Device
from wake_net.main import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    records = Device.query.all()
    return render_template('index.html', records=records)

@main.route('/addDevice', methods=['GET', 'POST'])
def add_device():
    add_device_form = AddDeviceForm()
    if add_device_form.validate_on_submit():
        device = Device.query.filter_by(mac=add_device_form.mac.data).first()
        if device is None:
            device = Device(
                name=add_device_form.name.data,
                mac=add_device_form.mac.data,
                ip=add_device_form.ip.data,
                netmask=add_device_form.netmask.data
            )
            db.session.add(device)
            db.session.commit()
            return redirect(url_for('main.index'))
    return render_template('addDevice.html', add_device_form=add_device_form)
