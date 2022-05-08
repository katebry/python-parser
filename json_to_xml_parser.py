from dicttoxml import dicttoxml
from fakedata import data


def json_to_xml():
    xml = dicttoxml(data)
    xmlfile = open("dogbreeds.xml", "w")
    xmlfile.write(xml.decode())
    xmlfile.close()
