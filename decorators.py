""" декоратор, записывает параметры и результаты теста в файл """

from datetime import datetime
from quiz import Quiz

LOG_FILE_PATH = "log.txt"


def logger(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        finish = datetime.now()
        time_result = finish - start
        with open(LOG_FILE_PATH, "a", encoding="UTF-8") as log:
            log.write("login: " + args[0] + "\n")
            log.write("name: " + args[1] + "\n")
            log.write("study course: " + args[2] + "\n")
            log.write("access level: " + args[3] + "\n")
            log.write("date: " + str(start.date()) + "\n")
            log.write("time: " + str(start.strftime("%r")) + "\n")
            log.write("test time: " + str(time_result.seconds).strip() + " seconds" + "\n")
            log.write("result: " + str(Quiz.quiz_score) + " points" + "\n")
            log.write("---------------------------------------------------" + "\n")
    return wrapper
