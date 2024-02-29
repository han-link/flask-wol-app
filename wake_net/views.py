# views.py
from flask import Blueprint, render_template, redirect, url_for
from wake_net.forms import WakeUpForm, AddDeviceForm
from wakeonlan import send_magic_packet
from wake_net.models import Device
from wake_net.main import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    records = Device.query.all()
    return render_template('index.html', Device=Device, records=records)


@main.route('/deleteDevice/<int:device_id>', methods=['POST'])
def delete_device(device_id):
    device = Device.query.get_or_404(device_id)
    db.session.delete(device)
    db.session.commit()
    return redirect(url_for('main.index'))


@main.route('/addDevice', methods=['GET', 'POST'])
def add_device():
    add_device_form = AddDeviceForm()
    if add_device_form.validate_on_submit():
        mac_exists = Device.query.filter(Device.mac == add_device_form.mac.data).first()
        ip_exists = Device.query.filter(Device.ip == add_device_form.ip.data).first()

        error = False
        if mac_exists:
            add_device_form.mac.errors.append('A device with this MAC address already exists.')
            error = True
        if ip_exists:
            add_device_form.ip.errors.append('A device with this IP address already exists.')
            error = True

        if not error:
            new_device = Device(
                name=add_device_form.name.data,
                mac=add_device_form.mac.data,
                ip=add_device_form.ip.data,
                netmask=add_device_form.netmask.data
            )
            db.session.add(new_device)
            db.session.commit()
            return redirect(url_for('main.index'))

    return render_template('addDevice.html', add_device_form=add_device_form)
