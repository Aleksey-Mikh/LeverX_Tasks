import argparse

from converters_to_format import ConvertDataToJson, ConvertDataToXml
from combiners import CombinerRoomsAndStudents


class InitArgparse:
    """
    Class that initializes argparse to work with the console
    """

    allowed_output_types = ["json", "xml"]

    def __init__(self):
        self.parse_result = self._parse_args()

    def _parse_args(self):
        """
        Get arguments from the console
        """
        parser = argparse.ArgumentParser(
            description="A script that combines students and the rooms they should be in"
        )
        parser.add_argument("students", help="path to student file")
        parser.add_argument("rooms", help="path to rooms file")
        parser.add_argument("format", choices=self.allowed_output_types, help="type of output file")

        return parser.parse_args()


class Interface:
    """
    Interface that connects a class to receive arguments
    with a class that processes data and sends the received data
    to classes that convert data to a specified format
    """

    def __init__(self):
        """
        Method that calls Init Arg parse to get
        the necessary arguments and sets internal variables
        """
        parser = InitArgparse()
        self.path_to_student_file = parser.parse_result.students
        self.path_to_rooms_file = parser.parse_result.rooms
        self.output_type = parser.parse_result.format
        self._result_data = []
        self._convertor = None

    def get_data(self):
        """
        Get a list with registered students in rooms
        """
        combiner = CombinerRoomsAndStudents(self.path_to_student_file, self.path_to_rooms_file)
        self._result_data = combiner.registration_students_to_rooms()

    def convert_to_format(self):
        """
        Call classes to convert data to a format
        """
        if self.output_type == "xml":
            self._convertor = ConvertDataToXml(self._result_data)
        elif self.output_type == "json":
            self._convertor = ConvertDataToJson(self._result_data)

        self._convertor.convert_to_format()

    def write_to_file(self):
        """
        Call the method to write the converted data to a file
        """
        self._convertor.write_to_file()


if __name__ == '__main__':
    inter = Interface()
    inter.get_data()
    inter.convert_to_format()
    inter.write_to_file()
