import socket
from dotenv import load_dotenv

load_dotenv()


def send_magic_packet(mac_address):
    # Clean up this mac address convert from string to byte
    mac_clean = mac_address.replace(":", "").replace("-", "")
    mac_byte = bytes.fromhex(mac_clean)

    # Create the payload 0xFF * 6 FF:FF: FF: FF: FF:FF + Mac address * 16
    payload = b"\xFF" * 6 + mac_byte * 16

    # Send magic packet
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        sock.sendto(payload, ("<broadcast>", 9))
