import xml.etree.ElementTree as etree
import json

class JSONConnector:

    def __init__ (self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)
    
    @property    
    def parsed_data(self):
        return self.data


class XMLConnector:

    def __init__(self, filepath):
        self.tree = etree.parse(filepath)
    
    @property
    def parsed_data(self):
        return self.tree


def connector_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('unkown file {}'.format(filepath))

    return connector


def connect_to(filepath):
    factory = None
    try:
         factory = connector_factory(filepath)
    except ValueError as ve:
        print(ve)
    
    return factory

def show_person():
    xml_factory = connect_to('data/person.xml')
    xml_data = xml_factory.parsed_data()
    liars = xml_data.findall(".//{person}[{lastName}='{}']".format('Liar'))
    print('found:{} persons'.format(len(liars)))
    for liar in liars:
        print("first name: {}".format(liar.find('firstName').text))
        print('last name: {}'. format(liar.find('lastName'). text))
        [print('phone number ({}):'.format(p.attrib['type']), p.text) for p in liar.find('phoneNumbers')]


if __name__ == "__main__":
    #sqlite_factory = connect_to('data/person.sq3')
    show_person()