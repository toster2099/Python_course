# 1. Отсортировать все атрибуты модуля string по алфавиту, в обратном порядке, вывести полученный список на печать.

import string
list_by_alphabetically = dir(string)
list_by_reverse_order = dir(string)
list_by_alphabetically.sort()
list_by_reverse_order.sort(reverse=True)
print(list_by_alphabetically)
print(list_by_reverse_order)

#2. Попросить пользователя ввести строку. Сформировать список символов, из которых состоит строка и вывести на печать. 
#(Если была введена строка "hello" , то на выходе будет результат ['h', 'e', 'l', 'l', 'o'] )

input_string = input("Введите строку:")
input_list = list(input_string)
print(input_list) 

#3. Написать скрипт, который предлагает пользователю ввести строку и добавляет символ «+» между каждой парой символом введенной строки, 
#выводит на печать полученную строку. (Если была введена строка "hello" , то на выходе будет результат 'h+e+l+l+o’). 
#Подсказка - воспользуйтесь методом join строк

input_string = input("Введите строку:")
print("+".join(input_string))

#4. Написать скрипт, который предлагает пользователю ввести строку, сортирует ее элементы в прямом, а потом в обратном порядке 
#и выводит на печать отсортированные строки.

random_string = list(input("Введите строку:"))
random_string.sort()
print(''.join(random_string))
random_string.sort(reverse=True)
print(''.join(random_string))

#5. Сформировать список из трех случайных трехзначных чисел, вывести на печать полученный список, отсортированный в прямом и обратном порядке.,

import random
first_digit = random.randint(100,999)
second_digit = random.randint(100,999)
thirt_digit = random.randint(100,999)
list_of_digits = [first_digit,second_digit,thirt_digit]
list_of_digits.sort()
print(list_of_digits)
list_of_digits.reverse()
print(list_of_digits)

#6. Сформировать тупл, элементами которого 5 последних атрибутов модуля string, выведите на печать. 
#Преобразовав полученный тупл в список, добавьте на позицию с индексом 2 строку ‘capwords’ и преобразуйте список обратно в тупл.  
#Выведите на печать.

import string
tuple_of_string = tuple(dir(string))[-5:]
print(tuple_of_string)
list_of_string = list(tuple_of_string)
list_of_string.insert(2,'capwords')
tuple_for_print = tuple(list_of_string)
print(tuple_for_print)

#7. Сгенерировать случайную строку из 10 символов с помощью функции random. и константы string.ascii_letters    

import string
import random
result = random.sample(string.ascii_letters,10)
print("".join(result))

#8. Написать скрипт, который просит пользователя ввести следующую информацию: имя и фамилию работника (один input), его должность, зарплату, возраст. 
#Вывести на печать анкету работника в формате: 
#Имя: <имя>, Фамилия: <фамилия>, возраст: <возраст>. Должность: <должность>. Зарплата: <зарплата>
#При выводе имени и фамилии удостоверьтесь, что они будут выведены с Большой Буквы независимо от того, как были введены пользователем, 
#также не забудьте очистить от лишних пробелов. При выводе зарплаты, иметь в виду, что интересующая нас точность - до копеек. 
#Использовать два варианта форматирования строк, на ваш выбор.

name_surname = input("Введите ваше имя и фамилия:")
result = name_surname.title()
position = input("Ваша должость:")
salary = float(input("Ваша зарплата:"))
age = input("Ваш возраст:")
name, surname = result.split(' ')
print(f"Имя:{name},Фамилия:{surname},возраст:{age}.Должность:{position}.Зарплата:{salary}")


#9. Написать скрипт, который генерирует случайные пароли случайной длины, не меньше 10 и не больше 20 элементов,  
# из символов - букв латинского алфавита в верхнем и нижнем регистре, цифр. 

import string
import random
lenghth_password_letters = random.randint(10,20)
result = random.sample(string.ascii_letters+string.digits,lenghth_password_letters)
print("".join(result))


#10. Написать скрипт, который генерирует список из 30 одинаковых элементов (случайное int число), 
#затем на базе этого списка формирует новый, заменив каждый третий элемент исходного списка на число 1000. 
#Вывести на печать исходный список и новый список.

import random
my_list = [random.randint(1,9)]*30
print(my_list)
my_list[::3] = [1000]*10
print(my_list[1:])
