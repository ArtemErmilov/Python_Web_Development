# Задача 1

# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
# В консоль вводим cmd Enter,  HW6_task2.py 29.02.2104 Enter

from sys import argv

from HW6_task1 import correct_dates, leap_year

date_list = argv[1:]
date, *_ = date_list

print(correct_dates(date))
