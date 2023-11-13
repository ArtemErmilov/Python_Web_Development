import os
from pathlib import Path


def creat_folders_files(chapter:str,lesson:int,task:int):
    """
    chapter: - раздел где надо создать папку.
        p - практика, l - лекция, hw - домашнее задание.
    lesson: - номер урока, папка с название
    task: - количество файлов в папке lesson.
    """
    chapter = chapter.lower()
    lesson_number = '00'+str(lesson)
    print(lesson_number)
    if(chapter == 'p'):
        chapter_folder = 'Practice'
        lesson_folder = f'Lesson{lesson_number[-3:]}'
        console = 'Pra_less'
        pass
    elif(chapter == 'l'):
        chapter_folder = 'lecture'
        lesson_folder = f'Lesson{lesson_number[-3:]}'
        console = 'lec_less'
        pass
    elif(chapter == 'hw'):
        chapter_folder = 'Homework'
        lesson_folder = f'HW{lesson}'
        console = lesson_folder
        pass
    else:
        print(f'Раздела {chapter} не существует')
        return

    path_folder = f'Python/{chapter_folder}' # Путь к папки
    name_folder = path_folder+'/'+lesson_folder #Название файла
    try:
        os.mkdir(name_folder)
    except:
        pass
    if (chapter == 'p' or chapter == 'l'):
        console_name = f'{console}{name_folder[-2]+name_folder[-1]}'
    else:
        console_name = console
    for num in range(1,task+1):
        try:
            name = f'{name_folder}/{console_name}_task{num}.py'
            
            f = open(name, 'x', encoding='utf-8')
            f.close()
        except:
            continue

if __name__ == '__main__':

    creat_folders_files('hw',15,1)
