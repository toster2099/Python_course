#Задание 2: Дописать скрипт с урока, переименовать переменные чтоб они имели смысл(если нужно). 
# Использовать функцию print, передавая в неё несколько аргументов, 
# избегая явной конкатенации( пример - print(“my name is”, name)  )-как разбирали на уроке. 
#Добавить скрипт в гитхаб как lesson2.py, отправить мне ссылку 
 
#Результатом скрипта может быть примерно следующее
#Integer number: 20
#Float number: 22.56889
#Is integer number bigger than float number: False

import random
int_number = random.randint(0,100)
print('Integer number:',int_number)
float_number = random.uniform(1.0,100.0)
print('Float number:',float_number)
result = int_number > float_number
print('Is int number bigger than float number:',str(result))

#Задание 3:  Написать скрипт, который будет генерировать случайное bool значение и выводить его на печать

import random
random_bool = random.randint(0,1)
print(bool(random_bool))

#Задание 4:Написать скрипт, который просит пользователя ввести число, а потом степень, 
#в которую его нужно возвести и выводит на печать результат вычисления и его тип. 
#Для возведения в степень использовать оператор ** и функцию math.pow, сравнить результат.

#Реализация: 1

number = int(input("Введите число: "))
power = int(input("Введите степень: "))
result = number**power
print(result,type(result))

#Реализация:2

import math
number = int(input("Введите число: "))
power = int(input("Введите степень: "))
result = math.pow(number,power)
print(result,type(result))

#Задание 5:Написать скрипт, которые генерирует случайное число, выводит его на печать, выводит на печать квадрат числа и выводит ответы на вопросы, 
# Is Числе больше 10?: (True | False) Квадрат числа больше 500?: (True | False) 

import random
number = random.randint(1,30)
result = number**2
answer1 = number > 10
answer2 = result > 500
print("Случайное число:",number,",","Квадрат числа:",result)
print("Is случайное число больше 10?:",answer1,",","Квадрат числа больше 500?:",answer2)

# Задание 6: С помощью встроенных функций hex, oct, написать скрипт, который просит пользователя ввести число, 
# а затем выводит его на экран в 16ти-ричном представлении(hex) и восьмеричном (oct).  
# Скрипт должен корреткно обрабатывать вариант, когда пользователь ввел число float, а не только int. 
# Не использовать if или какие-то другие конструкции, только то, что мы изучали!

number = int(float(input("Введите число:")))
hex_number = hex(number)
oct_number = oct(number)
print(hex_number,oct_number)