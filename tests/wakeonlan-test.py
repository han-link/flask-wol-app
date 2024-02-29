import os
from dotenv import load_dotenv
from wake_net.wakeonlan import send_magic_packet

load_dotenv()

if __name__ == "__main__":
    try:
        send_magic_packet(os.getenv("MAC_ADDRESS"))
    except Exception as e:
        print(f"Error sending magic packet: {e}")
