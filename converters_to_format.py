import xml.etree.ElementTree as xml
from abc import ABC, abstractmethod
import json


class AbstractConvertData(ABC):

    @abstractmethod
    def convert_to_format(self):
        pass

    @abstractmethod
    def write_to_file(self):
        pass


class ConvertDataToJson(AbstractConvertData):

    def __init__(self, data: list):
        self.data = data

    def convert_to_format(self):
        pass

    def write_to_file(self):
        with open("result.json", "w") as file:
            json.dump(self.data, file, indent=4)


class ConvertDataToXml(AbstractConvertData):

    def __init__(self, data: list):
        self.data = data
        self.root = None

    def convert_to_format(self):
        self.root = xml.Element("rooms")
        for room in self.data:
            room_xml = xml.SubElement(self.root, "room")

            room_xml_id = xml.SubElement(room_xml, "id")
            room_xml_id.text = str(room["id"])

            room_xml_name = xml.SubElement(room_xml, "name")
            room_xml_name.text = room["name"]

            room_xml_students = xml.SubElement(room_xml, "students")
            for student in room["students"]:
                student_xml = xml.SubElement(room_xml_students, "student")

                student_xml_id = xml.SubElement(student_xml, "id")
                student_xml_id.text = str(student["id"])

                student_xml_name = xml.SubElement(student_xml, "name")
                student_xml_name.text = student["name"]

                student_xml_room = xml.SubElement(student_xml, "room")
                student_xml_room.text = str(student["room"])

    def write_to_file(self):
        tree = xml.ElementTree(self.root)
        tree.write("sample.xml")
