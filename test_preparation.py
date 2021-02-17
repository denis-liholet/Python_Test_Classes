""" модуль парсинга файла с вопросами теста """

INPUT_FILE_PATH = 'questions.txt'

questions = list()
temp_list = list()
correct_answers = list()


def preparation():
    """ читает строки из файла с вопросами теста, возвращает три списка:
    1) список вопросов, 2) список вариантов ответов, 3) список с правильными ответами
    """

    with open(INPUT_FILE_PATH, "r", encoding="UTF-8") as my_file:

        for line in my_file:
            questions.append(line.strip())
            temp_list.append(my_file.readline().strip())
            temp_list.append(my_file.readline().strip())
            temp_list.append(my_file.readline().strip())
            correct_answers.append(int(my_file.readline().split(":")[1].strip()))

        options = list()

        # формирует элементы списка вариантов ответов, создавая один элемент
        # нового списка "options" из трёх элементов временного списка "temp_list"
        for i in range(0, len(temp_list), 3):
            options.append(
                            temp_list[i] + "\n" +
                            temp_list[i + 1] + "\n" +
                            temp_list[i + 2]
                           )

    return questions, options, correct_answers
