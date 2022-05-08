import xmltodict
import json


def xml_to_json():
    with open("dogbreeds.xml") as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        xml_file.close()

        json_data = json.dumps(data_dict)

        with open("dogbreeds.json", "w") as json_file:
            json_file.write(json_data)
            json_file.close()
