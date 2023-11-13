from lec_less13_task14 import UserNameError, UserAgeError

class User:
    MIN_LEN = 6
    MAX_LEN = 30

    def __init__(self, name, age):
    
        if self.MIN_LEN < len(name) < self.MAX_LEN:
            self.name = name
        else:
            raise UserNameError (name, self.MIN_LEN, self.MAX_LEN)
        if not isinstance(age, (int, float)) or age < 0:
            raise UserAgeError
        else:
            self.age = age
       

user = User('Яковktd', 12)