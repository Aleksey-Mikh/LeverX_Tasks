import argparse

from converters_to_format import ConvertDataToJson, ConvertDataToXml
from combiners import CombinerRoomsAndStudents


class InitArgparse:

    allowed_output_types = ["json", "xml"]

    def __init__(self):
        self.parse_result = self._parse_args()

    def _parse_args(self):
        parser = argparse.ArgumentParser(
            description="A script that combines students and the rooms they should be in"
        )
        parser.add_argument("students", help="path to student file")
        parser.add_argument("rooms", help="path to rooms file")
        parser.add_argument("format", choices=self.allowed_output_types, help="type of output file")

        return parser.parse_args()


class Interface:

    def __init__(self):
        parser = InitArgparse()
        self.path_to_student_file = parser.parse_result.students
        self.path_to_rooms_file = parser.parse_result.rooms
        self.output_type = parser.parse_result.format
        self.result_list = []
        self.convertor = None

    def get_data(self):
        combiner = CombinerRoomsAndStudents(self.path_to_student_file, self.path_to_rooms_file)
        self.result_list = combiner.registration_students_to_rooms()

    def convert_to_format(self):
        if self.output_type == "xml":
            self.convertor = ConvertDataToXml(self.result_list)
        elif self.output_type == "json":
            self.convertor = ConvertDataToJson(self.result_list)

        self.convertor.convert_to_format()

    def write_to_file(self):
        self.convertor.write_to_file()


if __name__ == '__main__':
    inter = Interface()
    inter.get_data()
    inter.convert_to_format()
    inter.write_to_file()
