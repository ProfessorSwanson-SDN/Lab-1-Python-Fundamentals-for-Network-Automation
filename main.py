import logging

from src.network_device import NetworkDevice
from src.parser_utils import parse_json, parse_yaml, parse_xml, parse_csv

logging.basicConfig(
    filename="logs/lab.log",
    level=logging.INFO
)

def main():
    print("Starring Lab 1")

    device_data = parse_json("data/devices.json")
    print(device_data)
    
    for device in device_data:
       network_device = NetworkDevice(
           hostname=device.get("hostname"),
           ip=device.get("ip"),
           device_type=device.get("type")
         )
       network_device.summary()

if __name__ == "__main__":
    logging.info("LAB1-START")
    main()
    logging.info("[LAB1-END]")








