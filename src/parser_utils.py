import json
import logging

def parse_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        logging.info("PARSE_JSON_SUCCESS")
        return data
    except (FileNotFoundError, json.JSONDecodeError) as error:
        logging.error("PARSE_JSON_ERROR: %s", error)
        return[]

import yaml
def parse_yaml(filename):
    try:
        with open(filename, 'r') as file:
            data = yaml.safe_load(file)
        logging.info("PARSE_YAML_SUCCESS")
        return data
    except (FileNotFoundError, yaml.YAMLError) as error:
         logging.error("PARSE_YAML_ERROR: %s", error)
         return[]

import xml.etree.ElementTree as XML
def parse_xml(filename):
    try:
         with open(filename, 'r') as file:
            data = XML.parse(file)
            logging.info("PARSE_XML_SUCCESS")
            return data
    except (FileNotFoundError, XML.ParseError) as error:
        logging.error("PARSE_XML_ERROR: %s", error)
        return []


import csv
def parse_csv(filename):
        try:
            with open(filename, 'r') as file:
                data = list(csv.DictReader(file))
                logging.info("PARSE_CSV_SUCCESS")
                return data
        except Exception as error:
            logging.error("PARSE_CSV_ERROR: %s", error)
            return []