import logging
class NetworkDevice:
    def __init__(self, hostname, ip, type):
        self.hostname = hostname
        self.ip = ip
        self.type = type

    def summarize(self):
        message = f"{self.hostname} {self.type} - {self.ip}" 
        print(message)
        logging.info(f"DEVICE_SUMMARY:  {message}")
        return message
    
      





    












