# Задание №3

# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните имя  записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.

directory = 'Python/Practice/Lesson007'

    

def reading_file(file_num:str,file_name:str,new_name_file:str):

    file_num_new = f'{directory}/{file_num}'
    file_name_new = f'{directory}/{file_name}'
    new_name_file_new = f'{directory}/{new_name_file}'

    with    open(file_num_new, 'r', encoding='utf-8') as f_num,\
            open(file_name_new, 'r', encoding='utf-8') as f_name,\
            open( new_name_file_new, 'w', encoding='utf-8') as f_new_name:

        list_num = list(f_num)
        list_name = list(f_name)
        len_num = len(list_num)
        len_name = len(list_name)
        
        if (len_num>len_name):
            for i in range(len_num-len_name):
                list_name.append(list_name[i])
        else:
            for i in range(len_name-len_num):
                list_num.append(list_num[i])
        
        name_max_len = len(max(list_name))
       

        for num, name in zip(list_num,list_name):

            num1,num2 = num.split('|')
            num1,num2 = int(num1),float(num2)

            

            if (num1*num2<0):
                f_new_name.write(f'{name[:-2]}{abs(num1*num2):>{name_max_len*3}}\n')
            else:
                f_new_name.write(f'{name[:-2]}\t{round(num1*num2):>{name_max_len*3}}\n')





reading_file('Pra_Less7_task1_data.txt', 'Pra_Less7_task2_data.txt','Pra_Less7_task3_data.txt')