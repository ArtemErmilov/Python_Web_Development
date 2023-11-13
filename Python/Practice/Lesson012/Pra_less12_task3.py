# Задание №3
# 📌 Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.

class Factorial:

    def __new__(cls, stop:int, start:int = 1, step:int = 1):
        instance = super().__new__(cls)
        instance.stop = stop
        instance.start = start
        instance.step = step
        instance.number = instance.factorial(start)
        return  instance
    
    def factorial(self, number:int):
        temp_num = 1
        for num in range(1,number):
            temp_num *= num
        return temp_num

    
    def __iter__(self):
        return self
    
    def __next__ (self):
        while self.start <= self.stop:
            for num in range(self.start,self.start+self.step):
                self.number *=num
                self.start += 1
                if (self.start > self.stop):
                    return self.number                
            return self.number
        raise StopIteration

i = Factorial(10,1,3)

for num in i:
    print(num)