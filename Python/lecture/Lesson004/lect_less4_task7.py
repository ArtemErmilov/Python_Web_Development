# Позиционные и ключевые параметры

# При указании параметров функции вначале идут позиционные параметры. При
# вызове функции передаются значения без указания имени переменной-аргумента.
# Косая черта не является переменной. Это символ разделитель. После неё могут идти 
# как позиционные, так и ключевые параметры. Далее символ разделитель
# звёздочка указывает только на ключевые параметры.


def standard_arg(arg):
    """
    Пример обычной функции:
    """
    print(arg) # Принтим для примера, а не для привычки
standard_arg(42)
standard_arg(arg=42)

#Пример только позиционной функции:
def pos_only_arg(arg, /):
    """Пример только позиционной функции:"""
    print(arg) # Принтим для примера, а не для привычки

pos_only_arg(42)
pos_only_arg(arg=42) # TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

# Пример только ключевой функции:
def kwd_only_arg(*, arg):
    """Пример только ключевой функции:"""
print(arg) # Принтим для примера, а не для привычки

kwd_only_arg(42) # TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
kwd_only_arg(arg=42)


# Пример функции со всеми вариантами параметров:
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only) # Принтим для примера, а не для привычки

combined_example(1, 2, 3) # TypeError: combined_example() takes 2 positional arguments but 3 were given
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
combined_example(pos_only=1, standard=2, kwd_only=3) # TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'