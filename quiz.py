from test_preparation import preparation


class Quiz:

    quiz_score = 0

    def __init__(self, questions_list, options_list, solve_list):
        self.questions_list = questions_list
        self.options_list = options_list
        self.solve_list = solve_list


result = preparation()
quiz = Quiz(result[0], result[1], result[2])


def _is_true(value, answer_number):
    if value == quiz.solve_list[answer_number]:
        print('Верно!\n')
        Quiz.quiz_score += 1
        return True
    else:
        print('Ошибка!\n')
        return False


def _take_user_answer(answer_number):
    user_answer = input("\nВведите ваш ответ: ")
    user_answer = int(user_answer.strip())
    _is_true(user_answer, answer_number)


def _print_question():
    for i in range(10):
        print(quiz.questions_list[i])
        print(quiz.options_list[i])
        _take_user_answer(i)


def launch():
    _print_question()
