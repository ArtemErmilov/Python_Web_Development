# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

from datetime import datetime
import logging

logger = logging.getLogger(__name__)

format = '{asctime:<20} - {levelname:<10} - {msg}'

logging.basicConfig(filename='Python\Practice\Lesson015\Pra_less15_task4.log',filemode='a', 
                     level=logging.ERROR, style='{', format=format) # encoding = 'UTF-8'

WEEKDAYS = {'понедельник': 0,'вторник': 1,'среда': 2,'четверг': 3,
                'пятница': 4,'суббота': 5,'воскресенье': 6 }

months = {'января':1,'февраля':2,'марта':3, 'апреля':4,'мая':5,'июня':6,'июля':7,'августа':8,
                                        'сентября':9, 'октября':10,'ноября':11,'декабря':12}
DAYS_WEEK = 7 # Количество дней в недели

def fun_date (date:str ='5-й пятница сентября'):

    try:
        week, day_week, months_new = date.split()
        week = int(week[0])
        nay_year = datetime.now().year
        str_date = datetime(year = nay_year, month = months[months_new], day = 1)
        if(WEEKDAYS[day_week] - str_date.weekday()) >= 0:
            day_new=(WEEKDAYS[day_week] - str_date.weekday())+((week-1)*DAYS_WEEK)+1
        else:
            day_new=(WEEKDAYS[day_week] - str_date.weekday())+((week)*DAYS_WEEK)+1
        
        str_date = datetime(year = nay_year, month = months[months_new], day =  day_new)

        if str_date ==None:
            raise ValueError('Нет такой даты')
    
        return str_date
    except Exception as e:
        print(e)
        logger.error(msg=e)
 

if __name__ == '__main__':
    print(fun_date('5-е воскресенье декабря'))