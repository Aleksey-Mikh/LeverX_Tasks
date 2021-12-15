import json


class CombinerRoomsAndStudents:
    """
    Class that registers students in rooms
    """

    def __init__(
            self,
            path_to_student_file: str,
            path_to_rooms_file: str,
    ):
        """
        :param path_to_student_file: path to student file
        :param path_to_rooms_file: path to rooms file
        """
        self.path_to_student_file = path_to_student_file
        self.path_to_rooms_file = path_to_rooms_file

    def registration_students_to_rooms(self):
        """
        Registration of students in the rooms.
        The list of rooms should be sorted
        """
        list_of_students = self.open_file(self.path_to_student_file)
        list_of_rooms = self.open_file(self.path_to_rooms_file)

        for student in list_of_students:
            room = list_of_rooms[student["room"]]
            students_in_room = room.setdefault("students", [])
            students_in_room.append(student)
        return list_of_rooms

    @staticmethod
    def open_file(path_to_file: str):
        """
        Open JSON file
        """
        with open(path_to_file) as file:
            data = json.load(file)
        return data
