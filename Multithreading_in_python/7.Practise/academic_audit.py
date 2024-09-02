from concurrent.futures import ThreadPoolExecutor


students_grades = {
    "Иван": [5, 4, 3, 5],
    "Алексей": [],
    "Мария": [5, 5, 5, 5],
    "Андрей": [4, 4, 3, 5],
    "Екатерина": [3, 4, 5, 4],
    "Петр": [5, 5, 4, 4],
    "Наталья": [3, 4, 4, 3],
    "Сергей": [4, 4, 4, 5],
    "Анна": [5, 4, 5, 5],
    "Дмитрий": [],
    "Елена": [3, 4, 4, 3],
    "Алина": [5, 5, 5, 5],
    "Артем": [4, 4, 5, 4],
    "Ольга": [5, 4, 3, 5],
    "Ирина": [4, 3, 5, 5],
    "Константин": [],
    "Татьяна": [3, 4, 5, 5],
    "Владимир": [4, 4, 5, 4],
    "Юлия": [5, 5, 5, 5],
    "Валентин": [],
    "Светлана": [3, 4, 3, 3],
    "Виктор": [5, 4, 5, 5],
    "Галина": [4, 4, 4, 4],
    "Роман": [5, 4, 5, 4],
    "Михаил": [4, 4, 5, 4],
    "Оксана": [],
    "Лариса": [4, 4, 3, 5],
    "Даниил": [5, 5, 5, 5],
    "Максим": [4, 4, 5, 4],
    "Валерия": [3, 3, 4, 4]
}


def calculate_average_grade(student_name, scores):
    if scores:
        average_scores = round((sum(scores) / len(scores)), 2)
        return student_name, average_scores
    else:
        raise ValueError(f'У студента {student_name} нет оценок.')


with ThreadPoolExecutor(max_workers=10) as executor:
    futures = []
    for student_name, average_scores in students_grades.items():
        future = executor.submit(calculate_average_grade,
                                 student_name,
                                 average_scores)
        futures.append(future)
    for future in futures:
        try:
            student_name, average_scores = future.result()
            print(f'Средний балл {student_name}: {average_scores:.2f}')
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f'Непредвиденная ошибка: {e}')
