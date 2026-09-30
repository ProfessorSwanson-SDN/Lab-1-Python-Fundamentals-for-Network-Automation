import logging

from network_device import NetworkDevice

from parser_utils import parse_json, parse_yaml, parse_xml, parse_csv

logging.basicConfig(level=logging.INFO)

def main():
    devices = []
    json_data = parse_json("data/devices.json")
    yaml_data = parse_yaml("data/devices.yaml")
    xml_data = parse_xml("data/devices.xml")
    csv_data = parse_csv("data/devices.csv")

    for data in json_data:
        device = NetworkDevice(data["hostname"], data["ip"], data["type"])
        device.summarize()
        devices.append(device)

        return devices

if __name__ == "__main__":
    main()
