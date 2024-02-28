class Device:
    def __init__(self, name, ip, mac, port):
        self.name = name
        self.ip = ip
        self.mac = mac
        self.port = port


    def wake(self):
        pass