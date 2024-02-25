import socket


BROADCAST_IP = '255.255.255.255'
DEFAULT_PORT = 7


def create_magic_packet(macaddress: str) -> bytes:
    macaddress = macaddress.replace(':', '')
    if len(macaddress) != 12:
        raise ValueError("Incorrect MAC address format")
    return bytes.fromhex('FF' * 6 + macaddress * 16)


def send_magic_packet(macaddress: str, ip_address: str = BROADCAST_IP, port: int = DEFAULT_PORT) -> None:
    packet = create_magic_packet(macaddress)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        try:
            sock.sendto(packet, (ip_address, port))
        except Exception as e:
            print(f"Failed to send magic packet: {e}")
