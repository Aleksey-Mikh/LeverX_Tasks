import xml.etree.ElementTree as xml
from abc import ABC, abstractmethod
import json


class AbstractConvertData(ABC):
    """
    Abstract class that is needed
    to create converter classes
    """

    @abstractmethod
    def convert_to_format(self):
        """
        Method for converting and preparing
        data for writing to a file
        """
        pass

    @abstractmethod
    def write_to_file(self):
        """
        Method for writing data to a file
        """
        pass


class ConvertDataToJson(AbstractConvertData):
    """
    Class for converting data to JSON format
    """

    def __init__(self, data: list):
        """
        :param data: list which contains dicts of rooms
        with lists of students
        """
        self.data = data

    def convert_to_format(self):
        """
        Data already prepared to write to JSON file
        """
        pass

    def write_to_file(self):
        """
        Method for writing data to a JSON file
        """
        with open("result.json", "w") as file:
            json.dump(self.data, file, indent=4)


class ConvertDataToXml(AbstractConvertData):
    """
    Class for converting data to XML format
    """

    def __init__(self, data: list):
        """
        :param data: list which contains dicts of rooms
        with lists of students
        """
        self.data = data
        self.root = None

    def convert_to_format(self):
        """
        Convert list of rooms to XMl format
        and create XML tree
        """
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
        """
        Method for writing data to a XML file
        """
        tree = xml.ElementTree(self.root)
        tree.write("sample.xml")
