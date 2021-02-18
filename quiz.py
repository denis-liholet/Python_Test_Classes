from test_preparation import preparation


class Quiz:
    """ класс, содержащий логику работы теста """

    quiz_score = 0  # переменная класса для подсчета правильных ответов

    def __init__(self, questions_list, options_list, solve_list):
        self.questions_list = questions_list
        self.options_list = options_list
        self.solve_list = solve_list


result = preparation()  # создаю кортеж, елементы которого - это списки заданий, вариантов и ответов
quiz = Quiz(result[0], result[1], result[2])  # объект класса с атрибутами в виде списков


def _is_true(value, answer_number):
    """ проверка ответа пользователя на "правильность" """

    if value == quiz.solve_list[answer_number]:
        print('Верно!\n')
        Quiz.quiz_score += 1
        return True
    else:
        print('Ошибка!\n')
        return False


def _take_user_answer(answer_number):
    """ принимает ответ пользователя """

    user_answer = input("\nВведите ваш ответ: ")
    user_answer = int(user_answer.strip())
    _is_true(user_answer, answer_number)


def _print_question():
    """ задаёт вопрос, используя атрибут объекта класса """

    for i in range(10):
        print(quiz.questions_list[i])
        print(quiz.options_list[i])
        _take_user_answer(i)

    print(f"Верных ответов: {Quiz.quiz_score}")


def launch():
    """ запуск теста """
    _print_question()
