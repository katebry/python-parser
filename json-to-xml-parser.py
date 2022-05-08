from dicttoxml import dicttoxml
from fakedata import data


xml = dicttoxml(data)
xmlfile = open("dogbreeds.xml", "w")
xmlfile.write(xml.decode())
xmlfile.close()
