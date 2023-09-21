# Задание №7
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года -31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.


def leap_year (year:int) -> bool:
    """
    Если високосный год то функция выдаст True, если нет то False.
    """
    GREG_YEAR = 1582
    LEAP_YEAR = 4
    LEAP_YEAR100 = 100
    LEAP_YEAR400 = 400

    if year > GREG_YEAR:
        if year%LEAP_YEAR == 0 : 
            if (year%LEAP_YEAR100 == 0 and year%LEAP_YEAR400 != 0):
                return False                
            else:
                return True
        else:
            return False
    else:
            return False
def day_(month:int,year:int)-> int:
    """
    Функция определения максимального количества дней в месяце.
    """
    day = -1
    MONTH_BIG = 12
    FEBRUARY_MONTH = 2
    MONTH_LIST = [1,3,5,7,8,10,12]
    DAY_BIG_BIG = 31
    DAY_BIG = 30
    DAY_LEAP = 29
    DAY_SMALL = 28 

    if (month<= MONTH_BIG):
        if (month in MONTH_LIST):
            day = DAY_BIG_BIG
        elif(month == FEBRUARY_MONTH):
            if(leap_year (year)):
                day = DAY_LEAP
            else:
                day = DAY_SMALL
        else:
            day = DAY_BIG
    return day

def correct_dates (date:str)->bool:
    """
    Функция определения правильности введённой даты.
    Если дата правильная то функция выведет True, если не правильная то False.
    """
    day,month,year = list(map(int,date.split('.')))
    if (0<year<=9999 and 0 < month <= 12 and  0 < day <= day_(month,year)): 
        return True
    else:
        return False