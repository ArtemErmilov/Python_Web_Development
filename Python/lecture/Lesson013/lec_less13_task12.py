#Родительское исключение
class UserException(Exception):
    pass

# добавим исключения для ошибок имени и возраста пользователя.
class UserAgeError(UserException):
    pass

class UserNameError(UserException):
    pass