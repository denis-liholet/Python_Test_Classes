""" модуль запуска всей программы """

from quiz import launch
from user import Student
from decorators import logger


@logger
def start(login, name, course, role):
    launch()


print('You are:\n1 - Teacher\n2 - Student\nPlease, enter 1 or 2: ')
answer = int(input())

if answer == 1:
    print('Coming soon...\nBye!)')
else:
    user = Student.authorization()
    start(user.login, user.name, user.course, user.role)
