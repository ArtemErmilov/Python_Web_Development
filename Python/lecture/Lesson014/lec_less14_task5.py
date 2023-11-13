import doctest
doctest.testfile('prime.md', verbose=True) 

# Создаётся файл с документацией prime.md, в нём есть примеры имитирующие работу в режиме интерпретатора. 
# doctest.testfile('prime.md', verbose=True) считывает построчно файл, и если в нём встречаются
# примеры выполнения кода, то он их тестирует.