""" модуль парсинга файла с вопросами теста """

INPUT_FILE_PATH = 'questions.txt'


def preparation():
    """ читает строки из файла с вопросами теста, возвращает кортеж из трёх списков:
    1) список вопросов, 2) список вариантов ответов, 3) список с правильными ответами
    """

    with open(INPUT_FILE_PATH, "r", encoding="UTF-8") as my_file:

        questions = list()
        options_list = list()
        correct_answers = list()
        temp_list = list()

        for line in my_file:
            questions.append(line.strip())
            temp_list.append(my_file.readline().strip())
            temp_list.append(my_file.readline().strip())
            temp_list.append(my_file.readline().strip())
            correct_answers.append(int(my_file.readline().split(":")[1].strip()))

        # формирует элементы списка вариантов ответов, создавая один элемент
        # нового списка "options_list" из трёх элементов временного списка "temp_list"
        for i in range(0, len(temp_list), 3):
            options_list.append(
                temp_list[i] + "\n" +
                temp_list[i + 1] + "\n" +
                temp_list[i + 2]
            )

    return questions, options_list, correct_answers
