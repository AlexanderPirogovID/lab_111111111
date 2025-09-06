student = {
    "name": "Иван",
    "age": 20,
    "course": "Информатика",
    "grades": [4, 5, 3, 5, 4]
}
print(f"Имя: {student['name']}, Курс: {student['course']}")
print("Средний балл: ", sum(student['grades'])/len(student['grades']))
student['grades'].append(5)
print("Обновлённый словарь: ")
print(student)