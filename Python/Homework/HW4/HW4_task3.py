# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

# Разбейте её на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

import decimal
import copy
from os import system

def wealth (cash:decimal):
    """
    Вычет налога на богатство в размере 10% от
    суммы счёта, если сумма превышает 5_000_000 у.е..
    """
    system ('cls')
    if (cash >= 5_000_000):
        tips = round(cash * decimal.Decimal(0.1),2)
        cash -= tips
        print(f'С Вас снят налог на богатство в размере 10% - {tips}у.е.\nОстаток Вашего счёта {cash} у.е.')
        input('Для продолжения нажмите Enter')
        global_transactions([tips],[False])    

    return cash

def money_transactions(text:str,MULTIPLICITY:decimal = 50)->decimal:

    """
    Проверка введённой суммы на кратность 50 и на неправильность ввода данных.
    """

    while (True):
        try:
            number = decimal.Decimal(input(text))
            if (number < 0):
                print('Введено отрицательное значение. Введите сумму заново!')
                continue
            elif (number%50 != 0):
                print('Сумма введена не кратна 50. Введите сумму заново!')
                continue
            else:
                break
        except :
            print('Вместо цифр введены буквы. Введите сумму заново!')
            continue
        
    return number

def cashback (transaction:int,cash:decimal,RATIO = 0.03):
    """
    Функция для начисления кешбека. 
    """
    transaction = 0
    tips = cash*decimal.Decimal(RATIO)
    cash +=tips
    cash = round(cash,2)
    print(f'Вам начислен кешбек в размере 3% от суммы остатка по счёту.\nОстаток Вашего счёта {cash} у.е.')
    input('Для продолжения нажмите Enter')
    global_transactions([tips],[True])
    return transaction, cash

def menu_one(cash):
    """
    Меню один. Вывод баланса счёта на экран.
    """
    print(f'На вашем счете {cash} у.е.\n')
    input('Для продолжения нажмите Enter')

def menu_two(transaction:int,cash:decimal):
    """
    Меню два. Внесение денег.
    """
    text_menu_two ='Внесите деньги. Вносимая сумма должна быть кратна 50 у.е.: '
    cash_new = money_transactions(text_menu_two)
    cash += cash_new
    print(f'Вы внесли {cash_new} у.е. Баланс Вашего счёта {cash} у.е.')
    input('Для продолжения нажмите Enter')
    transaction +=1
    global_transactions([cash_new],[True])
    
    return  transaction, cash

def menu_three(transaction:int,cash:decimal):
    """
    Меню 3. Снятие денег со счёта.
    """
    if (cash==0):
            print('Вы не можете сеять деньги!!! На вашем счёте 0 у.е.')

    else:
            text_menu_three = 'Введите сумму для снятия. Введённая сумма должна быть кратна 50 у.е.: '
            cash_wit = money_transactions(text_menu_three)
            cash_wit_cop = cash_wit.copy_abs()

            if (cash_wit*decimal.Decimal(0.015)<decimal.Decimal(30)):
                tips = decimal.Decimal (30)
                cash_wit += 30

            elif (cash_wit*decimal.Decimal(0.015)>600):
                tips = decimal.Decimal (600)
                cash_wit += tips

            else:
                tips = cash_wit *decimal.Decimal (0.015)
                cash_wit += tips
            cash = round(cash,2)
            tips = round(tips,2)
            if(cash - cash_wit>0):
                cash -= cash_wit
                print(f'Вы сняли {cash_wit_cop} у.е. Процент за снятие денег {tips} у.е.\nБаланс вашего счёта {cash} у.е.')
                global_transactions([cash_wit_cop,tips],[False,False])
                transaction +=1

            else:
                print(f'На вашем счёте недостаточно средств {cash} у.е.!!! Вы не можете снять сумму {cash_wit_cop} у.е. плюс процент за снятие  {tips} y.e.') 

    input('Для продолжения нажмите Enter')

    return transaction, cash

def global_transactions(cash:list,operations:list):
    """
    Заполнение глобального списка транзакциями.
    """
    glob_dict = globals()
    for ca, op in zip(cash,operations):
        if(op==False):
            ca = float(ca)*(-1.0)
        else:
            ca = float(ca)
        glob_dict['money_transactions_list'].append(round(float(ca),2))

money_transactions_list = [] #Список с операциями по транзакциям со счётом.

cash:decimal.Decimal = 0

transaction = 0

text_greetings =    'Вас приветствует программа БАНКОМАТ!!!\n'\
                    'Вам доступны следующие операции:\n\n'\
                    '1 - Вывести содержание счёта на экран,\n'\
                    '2 - Пополнить счёт,\n'\
                    '3 - Снять деньги,\n'\
                    'Enter - выйти из программы.\n'

while (True):

    system ('cls')
    print(f'Операции по счёту: {money_transactions_list}')
    cash = round(cash,2)
    if (transaction == 3): # Начисление кешбека.
        transaction,cash = cashback(transaction,cash)
        continue  

    print(text_greetings)
    
    menu_selection = input('Введите значения от 1 до 3: ')

    if(menu_selection=='1'): # Вывод баланса счёта на экран.  

        system ('cls') 

        menu_one(cash)

        continue

    elif(menu_selection=='2'): # Внесение денег.

        cash = wealth(cash)

        system ('cls')

        transaction, cash = menu_two(transaction, cash)
       
        continue

    elif(menu_selection=='3'): # Снятие денег.

        cash = wealth(cash)

        system ('cls')

        transaction,cash = menu_three(transaction,cash)
        
        continue
    else: # Выход из программы
        system ('cls') 
        print('Вы вышли из программы БАНКОМАТ!\n')
        break
