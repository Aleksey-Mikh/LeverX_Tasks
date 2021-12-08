import json


class CombinerRoomsAndStudents:

    def __init__(
            self,
            path_to_student_file: str,
            path_to_rooms_file: str,
            path_to_output_file: str,
    ):
        self.path_to_student_file = path_to_student_file
        self.path_to_rooms_file = path_to_rooms_file
        self.path_to_output_file = path_to_output_file

    def combiner(self):
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

    def write_file(self, data: list):
        with open(self.path_to_output_file, "w") as file:
            json.dump(data, file, indent=4)


if __name__ == '__main__':
    comb = CombinerRoomsAndStudents("students.json", "rooms.json", "result.json")
    output_data = comb.combiner()
    comb.write_file(output_data)
