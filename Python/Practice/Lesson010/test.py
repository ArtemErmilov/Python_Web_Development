import M_Ba 

f = M_Ba.PathFile(__file__)

print()
print(f'1. {f.get_path_file()}\n') # Возвращение полного пути к запускаемому файлу
print(f'2. {f.get_name_file()}\n') # Возвращение имени запускаемого фила c расширением
print(f'3. {f.get_full_name_file()}\n') # Возвращение название запускаемого фила с полным путём.
print(f'4. {f.get_name_file_no_exten()}\n') # Возвращение название запускаемого фила без расширения.
print(f'5. {f.get_full_name_file_no_exten()}\n') # Возвращение название запускаемого фила c полным путём без расширения.