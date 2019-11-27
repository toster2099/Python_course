#2. Написать скрипт, который генерируем два случайных дробных числа, 
# находит их произведение и выводит на печать результирующее число, 
# затем результирующее число, округленное но 4-х знаков и затем до 2х знаков

import random
second_value = random.uniform(1.00,100.00)
first_value = random.uniform(1.00,100.00)
result = first_value * second_value
print("Результат произведения:",result)
round_result = round(result,2)
round_result_two = round(result,4)
print("Результат округления до 4-х знаков", round_result_two,",","Результат округления до 2-х знаков",round_result)

# 3. Написать скрипт, который просит пользователя ввести любую строку 
# и выводит следующую информацию - 
# Длину строки, 
# минимальный и максимальный элемент строки 
# (при этом, выводить на печать также функцию, с помощью которой получено значение этих параметров). 
# То есть скрипт может генерировать примерно такой вывод - Length of input string is 1000 , function is <built-in function len>.

input_string = input("Введите строку:")
print("Количество символов в строке:",len(input_string),"function is",len)
print("Минимальный элемент строки:",min(input_string.lower()),"function is",min)
print("Максимальный элемент строки:",max(input_string),"function is",max)

#4. Написать скрипт, который просит пользователя ввести любую строку 
# и выводит на печать сначала первую половину строки, 
# потом - вторую. 
# Пример результат выполнения скрипта
# First half: qwert
# Second half: yuiop

input_string = str(input("Введите строку:"))
string_index = len(input_string) // 2
print("First_half:",input_string[0:string_index])
print("Second_half:",input_string[string_index:])

# 5. Вы перехватили секретное послание,
# VZoFPzGvXwtbR+guMLszPhfvZotHwDm-emryhEXAaBW+-AbMdmEK+ztGDWyIzSFvjaFrHLzhoRqgsQraUdnSBGykFWNLOxTVKM+ynHqsVrQGEiqdKULoDVZcsZ-BpTWkDVR+
# jSgrfQZhUAdWCxtwOmTBQo+qWOlYyvGxnNpZFlTSrmaesQOotBLnVw!gOUrhz+F-DctdKWvTGhMUopoSPyFAXdJnY+DGFZQbOVgzaqsGvWjtBrJjBWhAFgryaTtwginpEsWtAuOxbgI
# -ZVunVAIuklBqTlSGUnevwEMqayHKF+sebTCtWcnhzUelA+iM+ivKleqrjoLsmrtHZOGfnHOWXYJpDwU!
# известно, что агенты используют для шифрации-дешифрации простейший алгоритм - после каждой буквы исходной фразы, 
# добавляют определенное число случайных символов. Чтобы скрыть первую букву, добавили и перед ней такое же количество случайных символов. 
# Ваши специалисты узнали, что это число - 10. расшифруйте послание.

secret_key = "VZoFPzGvXwtbR+guMLszPhfvZotHwDm-emryhEXAaBW+-AbMdmEK+ztGDWyIzSFvjaFrHLzhoRqgsQraUdnSBGykFWNLOxTVKM+ynHqsVrQGEiqdKULoDVZcsZ-BpTWkDVR+jSgrfQZhUAdWCxtwOmTBQo+qWOlYyvGxnNpZFlTSrmaesQOotBLnVw!gOUrhz+F-DctdKWvTGhMUopoSPyFAXdJnY+DGFZQbOVgzaqsGvWjtBrJjBWhAFgryaTtwginpEsWtAuOxbgI-ZVunVAIuklBqTlSGUnevwEMqayHKF+sebTCtWcnhzUelA+iM+ivKleqrjoLsmrtHZOGfnHOWXYJpDwU!"
print(secret_key[10:-1:11])

#** 6. Написать скрипт, который просит пользователя ввести строку и 
# выводит на печать эту строку задом на перед. 
# (то есть при вводе hello скрипт генерирует вывод - olleh)

input_surname = str(input("Введите  вашу Фамилию:"))
print(input_surname[::-1])