import os
from dotenv import load_dotenv
from wake_net.wakeonlan import send_magic_packet

load_dotenv()


if __name__ == "__main__":
    send_magic_packet(os.getenv('MAC_ADDRESS'))
