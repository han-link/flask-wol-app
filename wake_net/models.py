from . import db


class Device(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    mac = db.Column(db.String(17), nullable=False)
    ip = db.Column(db.String(15), nullable=False)
    netmask = db.Column(db.String(15), nullable=False)

    def __init__(self, name, mac, ip, netmask):
        self.name = name
        self.mac = mac
        self.ip = ip
        self.netmask = netmask
