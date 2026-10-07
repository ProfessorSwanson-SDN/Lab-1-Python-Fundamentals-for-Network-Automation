import logging


class NetworkDevice:
    def __init__(self, hostname, ip, device_type):
        self.hostname = hostname
        self.ip = ip
        self.type = device_type

    def summary(self):
        message = f"[DEVICE_SUMMARY]: {self.hostname} ({self.type}) - ({self.ip})"
        print(message)
        logging.info(message)
        return message
        

