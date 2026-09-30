import json
import yaml
import xml.etree.ElementTree as ET
import csv
import logging

def parse_json(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            logging.info(f"PARSE_JSON_SUCCESS: Successfully parsed JSON file - {file_path}")
            return data
    except FileNotFoundError:
        logging.error(f"PARSE_JSON_ERROR: File not found - {file_path}")
        return{}
    except json.JSONDecodeError:
        logging.error(f"PARSE_JSON_ERROR: Invalid JSON format in file - {file_path}")
        return {}
    
def parse_yaml(file_path):
    try:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
            logging.info(f"PARSE_YAML_SUCCESS: Successfully parsed YAML file - {file_path}")
            return data
    except FileNotFoundError:
        logging.error(f"PARSE_YAML_ERROR: File not found - {file_path}")
        return {}
    except yaml.YAMLError:
        logging.error(f"PARSE_YAML_ERROR: Invalid YAML format in file - {file_path}")
        return {}

def parse_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        logging.info(f"PARSE_XML_SUCCESS: Successfully parsed XML file - {file_path}")
        return root
    except ET.ParseError:
        logging.error(f"PARSE_XML_ERROR: Invalid XML format in file - {file_path}")
        return None

def parse_csv(file_path):
    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            logging.info(f"PARSE_CSV_SUCCESS: Successfully parsed CSV file - {file_path}")
            return rows
    except FileNotFoundError:
        logging.error(f"PARSE_CSV_ERROR: File not found - {file_path}")
        return []
    