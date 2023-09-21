# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.



def cash(name_list:list,salary_list:list,bonus_list:list)->dict:
    bonus_list_new = bonus_list.copy()
    name_dict = {name_list[i]:((float(bonus_list_new[i].replace('%',''))/100)*salary_list[i]) for i in range(len(name_list))}
    return name_dict


name_list =['Саша','Петя','Вася']

salary_list =[100,200,300] 

bonus_list = ['1.5%','15.5%','10.25%']

print(cash(name_list,salary_list,bonus_list))