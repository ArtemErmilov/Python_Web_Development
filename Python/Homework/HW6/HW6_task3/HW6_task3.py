# # Задача 3


# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, 
# # решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, 
# # чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, 
# # есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, 
# # каждое число от 1 до 8 -координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, 
# # а если бьют -ложь.

import copy

from random import randint as ri

def intersections(control:list,etalon:list)->bool:
    """
    Проверка, бют ли друг-друга ферзи.
    Вводятся координаты ферзей в формате [x1,y1] [x2,y2].
    Если ферзи бют друг-друга то функция выводит False, если нет то True.
    """
    
    math_list = ([1,1],[1,-1],[-1,1],[-1,-1])
    
    STOP_MAX_LIM = 8
    STOP_MIN_LIM = 1

    if(control[0]==etalon[0] or control[1]==etalon[1]):
        return False   
    for a,b in math_list:
        new_x = copy.copy(control[0])
        new_y = copy.copy(control[1])        
        while STOP_MIN_LIM<=new_x<=STOP_MAX_LIM and STOP_MIN_LIM<=new_y<=STOP_MAX_LIM:
            if (etalon == [new_x,new_y]):
                return False
            new_x += a
            new_y += b
            
    else:
        return True

def chess_board (queens:list):
    """
    Проверка на бют лт друг-друга ферзи из списка 8 координат.
    Если одн из пар бьёт друг-друга то функция выводит False, если нет то True.
    """
    while len(queens):
        control = queens.pop(0)
        for data in queens:
            if(not intersections(control,data)):
                return False
    return True

def queens_rand():
    queens_set =set()
    while len(queens_set)<=8:
        queens_set.add(f'{ri(1,8)},{ri(1,8)}')
    queens_list = []
    for data in queens_set:
        new_list = list(map(int,data.split(',') ))
        queens_list.append(new_list)
    return queens_list

def chess_board_rand (inum:int = 4):
    count = 0
    while count < inum:
        queens_list = copy.copy(queens_rand())
        if(chess_board(queens_list)):
            count +=1
            print(f'{count} Лучший вариант: {queens_list}')


