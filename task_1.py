import json
import argparse


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


class CombinerRoomsAndStudents:

    def __init__(
            self,
            path_to_student_file: str,
            path_to_rooms_file: str,
    ):
        self.path_to_student_file = path_to_student_file
        self.path_to_rooms_file = path_to_rooms_file

    def registration_students_to_rooms(self):
        list_of_students = self.open_file(self.path_to_student_file)
        list_of_rooms = self.open_file(self.path_to_rooms_file)

        for student in list_of_students:
            room = list_of_rooms[student["room"]]
            students_in_room = room.setdefault("students", [])
            students_in_room.append(student)
        return list_of_rooms

    @staticmethod
    def open_file(path_to_file: str):
        with open(path_to_file) as file:
            data = json.load(file)
        return data


if __name__ == '__main__':
    Interface()
