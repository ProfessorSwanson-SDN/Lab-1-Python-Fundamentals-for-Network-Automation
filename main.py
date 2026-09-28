import logging
from src.network_device import NetworkDevice
from src.parser_utils import parse_json, parse_yaml, parse_xml, parse_csv

def main():

    devices = parse_json("data/devices.json")
    interfaces = parse_yaml("data/interfaces.yaml")
    vlans = parse_xml("data/vlans.xml")
    inventory = parse_csv("data/inventory.csv")

    for item in devices:
        device = NetworkDevice(item["hostname"], item["ip"], item["type"])

        device.summarize()

    for item in interfaces["interfaces"]:
        msg = f"Interface {item['name']} is {item['status']}"
        print(msg)
        logging.info(f"INTERFACE_MSG: {msg}")

    for item in vlans.getroot().findall("vlan"):
        msg = f"VLAN {item.findtext('id')} is the {item.findtext('name')}"
        print(msg)
        logging.info(f"VLAN_MSG: {msg}")

    for item in inventory:
        msg = f"Device {item['hostname']} is a {item['location']} {item['role']}"
        print(msg)
        logging.info(f"DEVICE_MSG: {msg}")

if __name__ == "__main__":
     logging.basicConfig(filename="logs/lab.log", level=logging.INFO)
     logging.info("[LAB1_START]")
     main()
     logging.info("[LAB1_END]")