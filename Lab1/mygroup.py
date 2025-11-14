groupmates = [
    {
        "name": "Конев",
        "surname": "Дмитрий",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [3, 5, 5]
    },
    {
        "name": "Старостин",
        "surname": "Данил",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [3, 3, 3]
    },
    {
        "name": "Дашиева",
        "surname": "Марина",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [3, 4, 3]
    },
    {
        "name": "Круглов",
        "surname": "Степан",
        "exams": ["УД", "ИС", "КТП"],
        "marks": [3, 3, 3]
    },
    {
        "name": "Трошин",
        "surname": "Вячеслав",
        "exams": ["СИАОД", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Прохоров",
        "surname": "Максим",
        "exams": ["СИАОД", "ИС", "КТП"],
        "marks": [3, 4, 4]
    }
]
def print_students(students):
    """Показывает список студентов в виде таблицы."""

    # формируем и выводим заголовок
    header = (
        "Имя".ljust(12)
        + "Фамилия".ljust(12)
        + "Экзамены".ljust(35)
        + "Оценки".ljust(15)
        + "Средний"
    )
    print(header)
    print("-" * len(header))  # полоска под шапкой

    # выводим данные по каждому элементу списка
    for student in students:
        exams = ", ".join(student["exams"])  # список предметов -> одна строка
        marks = ", ".join(str(mark) for mark in student["marks"])  # оценки -> строка
        avg_mark = sum(student["marks"]) / len(student["marks"])  # среднее значение

        row = (
            student["name"].ljust(12)
            + student["surname"].ljust(12)
            + exams.ljust(35)
            + marks.ljust(15)
            + f"{avg_mark:.2f}"
        )
        print(row)


def filter_by_average(students, threshold):
    """
    Возвращает новый список, в который попадают только те студенты,
    чей средний балл строго больше указанного порога.
    """
    filtered = []

    for student in students:
        avg_mark = sum(student["marks"]) / len(student["marks"])
        if avg_mark > threshold:
            filtered.append(student)

    return filtered


if __name__ == "__main__":
    try:
        # читаем минимальный допустимый средний балл
        min_avg = float(input("Введите минимальный средний балл: "))
    except ValueError:
        # если пользователь ввёл не число
        print("Ошибка: нужно ввести число, например 4.5")
    else:
        # выбираем подходящих студентов
        selected = filter_by_average(groupmates, min_avg)

        if selected:
            print(f"\nСтуденты со средним баллом выше {min_avg}:\n")
            print_students(selected)
        else:
            print("Студентов с таким средним баллом не найдено.")
