# LeverX Task 1

Даны 2 файла (смотрите в прикрепленных файлах):
- students.json
- rooms.json

Необходимо написать скрипт, целью которого будет загрузка этих двух файлов, объединения их в список комнат где каждая комната содержит список студентов которые
находятся в этой комнате, а также последующую выгрузку их в формате JSON или XML.

Необходима поддержка следующих входных параметров:
- students # путь к файлу студентов
- rooms # путь к файлу комнат
- format # выходной формат (xml или json)

Ожидается использование ООП и SOLID

---

# Quick start

```
python main_program.py students.json rooms.json xml
```
---

## JSON format

        [
            {
                "id": 0,
                "name": "Room #",
                "students": [
                    {
                        "id": 345,
                        "name": "William Perez",
                        "room": 0
                    },
                    ...
                ]       
            },
            ...
        ]

---

## XML format

        <rooms>
            <room>
                <id>0</id>
                <name>Room #0</name>
                <students>
                    <student>
                        <id>345</id>
                        <name>William Perez</name>
                        <room>0</room>
                    </student>
                    ...
                </students>
            </room>
            ...
        </rooms>
