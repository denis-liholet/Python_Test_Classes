class User:
    """ создаёт пользователя с атрибутами """

    def __init__(self, login, name, role):
        self.login = login
        self.name = name
        self.role = role


class Student(User):
    """ создаёт пользователя с уровнем доступа 'student' """

    def __init__(self, login, name, course, role='student'):
        super().__init__(login, name, role)
        self.login = login
        self.name = name
        self.course = course

    @classmethod
    def authorization(cls):
        """ создаёт и возвращает объект класса с атрибутами """

        login = input('Please, enter your login: ')
        name = input('Please, enter your name: ')
        course = input('Please, enter your course: ')
        role = 'student'
        return Student(login, name, course, role)


class Teacher(User):
    """ создаёт пользователя с уровнем доступа 'teacher' """

    def __init__(self, login, name, role='teacher'):
        super().__init__(login, name, role)
        self.login = login
        self.role = role
