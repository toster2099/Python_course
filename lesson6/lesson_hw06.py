# Задание 1
# Написать в редакторе скрипт, который предлагает пользователю ввести произвольное число. Если число кратно 3, 
# то выводить на печать сообщение Число {} кратно 3. Если число не кратно 3, выводить на печать - Число {} не кратно 3.
# В конце работы скрипта выводить на печать текст - До свидания!
# Обратите внимание на отступы! Текст До свидания должен выводиться при любых условиях.

# value_int = 3
# input_int = int(input("Введите пожалуйста число:"))
# if input_int == value_int:
#     print(f"Число {input_int} кратно {value_int}")
# elif input_int != value_int:
#     print(f"Число {input_int} не кратно {value_int}")
# print("До свидания!")

# Задание 2
# Написать в редакторе скрипт, который предлагает пользователю ввести произвольное число. 
# А затем просить пользователя указать, в каком представлении вывести число - бинарном, 8-миричном, 16-ричном.
# Если введена буква b или В - в бинарном. Если o, O - 8-миричном, h или H - 16-ричном. 
# Если ни один из вариантов - сообщение об ошибке, Укажите желаемый формат - h, H или b, B или o, O.
# В конце работы скрипта выводить на печать текст - До свидания!
# Обратите внимание на отступы! Текст До свидания должен выводиться при любых условиях.

# int_bin, int_bin_two = "b", "B"
# int_oct, int_oct_two = "o", "O"
# int_hex, int_hex_two = "h", "H"
# input_digit = int(input("Введите число:"))
# input_format = input("В каком представлении вывести число - бинарном(b.B), 8-миричном(o,O), 16-ричном(h,H)?:")
# if input_format == int_bin or input_format ==int_bin_two:
#     result = bin(input_digit)
#     print(f"Введенное число {input_digit} в бинарном представлении -  {result}")
# elif input_format == int_oct or input_format ==int_oct_two:
#     result = oct(input_digit)
#     print(f"Введенное число {input_digit} в 8-миричном представлении -  {result}")
# elif input_format == int_hex or input_format ==int_hex_two:
#     result = oct(input_digit)
#     print(f"Введенное число {input_digit} в 16-ричном представлении -  {result}")
# else:
#     print("Ошибка ввода. Укажите желаемый формат - h, H или b, B или o, O")
# print("До свидания!")

# Задание 3
# Есть список животных, нужно определить какое животное загадал пользователь. Животные с условиями:
# Птица(bird) - может летать, есть перья
# Насекомое(insect) - может летать, нет перьев, не мышь )
# Мышь(bat) - может летать, нет перьев, мышь 
# Рыба(fish) - не может летать, живет в воде
# Млекопитающее(mammal) - не может летать, не живет в воде, есть ноги.
# Змея(snake) - не может летать, не живет в воде, нет ног.
# Вопросы - через input (y, Y или n, N). Нужно узнать, что загадал пользователь.
# Пример вопроса - Загаданное животное умеет летать? И так далее.

# secret_animal = ["птица","насекомое","мышь","рыба","млекопитающее","змея"]
# yep, no = "y", "n"
# answear_yep, answear_no = yep.title(), no.title()
# question = input("Загаданное животное умеет летать?:")
# if question == answear_yep:
#     question = input("У Загаданного животного есть перья?:")
#     if question == answear_yep:
#         print(f"Загаданное животное: {secret_animal[0]}") 
#     elif question == answear_no:
#         question = input("Загаданное животное - мышь?:")
#         if question == answear_yep:
#             print(f"Загаданное животное: {secret_animal[2]}")
#         elif question == answear_no:
#             print(f"Загаданное животное: {secret_animal[1]}")
# elif question == answear_no:
#     question = input("Загаданное животное живет в воде?:")
#     if question == answear_yep:
#         print(f"Загаданное животное: {secret_animal[3]}")
#     elif question == answear_no:
#         question = input("У загаданного животного есть ноги?:")
#         if question == answear_yep:
#             print(f"Загаданное животное: {secret_animal[4]}")
#         elif question == answear_no:
#             print(f"Загаданное животное: {secret_animal[5]}")

# Задание 4
# 4. Написать скрипт, который предлагает пользователю ввести число, проверяет, 
# если пользователь ввел символы, отличные от цифр (вспомнить подходящие методы строк) - то генерирует случайное число, 
# пишет, что число сгенерировано. Выводит на печать число(сгенерированное или введенное) и его квадрат

# import string
# import random
# value = input("Введите число:")
# if value in string.ascii_lowercase or value in string.ascii_uppercase:
#     random_digit = random.randint(1,100)
#     print(f"Число: {random_digit} сгенерировано")
#     print(f"квадрат числа {random_digit} =",random_digit**2)
# elif value in string.digits:
#     input_digit = int(value)
#     print(f"Ввеенное число {input_digit}")
#     print(f"квадрат числа {input_digit} =",input_digit**2)
# else:
#     input_digit = int(value)
#     print(f"Ввеенное число {input_digit}")
#     print(f"квадрат числа {input_digit} =",input_digit**2) 

# Задание 5 Попросите пользователя ввести имя файла. 
# Поддерживаемые расширения - txt, log, py. Если введено неподдерживаемое расширение, отображать ошибку. 
# Подсчитать количество слов в файле, предварительно убедившись, что файл существует с помощью функции модуля os, os.path.exists. 
# Если файл не существует, отображать ошибку
# Пример использования функции

# Пока что нашел решение этой задачи.

# import os
# a = os.path.exists(r"/home/bondar/Python_course/lesson6/task5.txt")
# print(a)
# result = os.path.exists(r"/home/bondar/Python_course/lesson6/task5")
# print("Файл test.txt существует?:", result)