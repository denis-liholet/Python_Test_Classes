from quiz import launch
from user import authorization
from decorators import logger


@logger
def start(login, name, role):
    launch()


user = authorization()
start(user.login, user.name, user.role)
