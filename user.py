class User:
    """ создаёт пользователя с атрибутами """

    def __init__(self, login, name, role):
        self.login = login
        self.name = name
        self.role = role


def authorization():
    """ создаёт и возвращает объект класса с атрибутами """

    login = input('Please, enter your login: ')
    name = input('Please, enter your name: ')
    role = input('Are you student or teacher?: ')
    return User(login, name, role)
