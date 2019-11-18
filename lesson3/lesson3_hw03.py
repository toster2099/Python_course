#2. Написать скрипт, который генерируем два случайных дробных числа, 
# находит их произведение и выводит на печать результирующее число, 
# затем результирующее число, округленное но 4-х знаков и затем до 2х знаков

import random
first_value = random.uniform(1.00,100.00)
second_value = random.uniform(1.00,100.00)
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

# Коментарий к реализации:
# Я реализовал задачу двукратным вызовом функцци print,с технической точки зрения это не совсем оптимально
# так как код будет выполнятся дольше но так как при условии если я бы вложил все аргументы в о дну функцию
# тогда код вышел бы длинным и плохо читабельным,а это считается признаком плохого тона.

input_string = str(input("Введите строку:"))
min_value = min(input_string)
max_value = max(input_string)
print("Количество символов в строке:", len(input_string),",","Минимальный элемент строки:",min_value,",","Максимальный элемент строки:",max_value)
print("function is",len)

#4. Написать скрипт, который просит пользователя ввести любую строку 
# и выводит на печать сначала первую половину строки, 
# потом - вторую. 
# Пример результат выполнения скрипта
# First half: qwert
# Second half: yuiop

# Реализация 1. Простая

input_string = str(input("Введите строку:"))
lengh_string = len(input_string)
string_index = int(lengh_string / 2)
print("First_half:",input_string[0:string_index])
print("Second_half:",input_string[string_index:])

# Реализация 2 Более сложная,запутанная и противоречит философии пайтон, но так как первоначально
# начал так реализовывать решил завершить начатое.
# a - проверяется остаток от деления на 2. Возмоный результат или 0 или 1
# b - делим общее количестов введенных символов на 2
# c - плюсуем остаток от деления к результату деления общего к-ва введенных символов на 2 

input_string = str(input("Введите строку:"))
lengh_string = len(input_string)
a = float(lengh_string % 2)
b = int(lengh_string / 2)
c = int(b + a)
print(type(c))
print("First_half:",input_string[0:c])
print("Second_half:",input_string[c:])


# 5. Вы перехватили секретное послание,
# VZoFPzGvXwtbR+guMLszPhfvZotHwDm-emryhEXAaBW+-AbMdmEK+ztGDWyIzSFvjaFrHLzhoRqgsQraUdnSBGykFWNLOxTVKM+ynHqsVrQGEiqdKULoDVZcsZ-BpTWkDVR+
# jSgrfQZhUAdWCxtwOmTBQo+qWOlYyvGxnNpZFlTSrmaesQOotBLnVw!gOUrhz+F-DctdKWvTGhMUopoSPyFAXdJnY+DGFZQbOVgzaqsGvWjtBrJjBWhAFgryaTtwginpEsWtAuOxbgI
# -ZVunVAIuklBqTlSGUnevwEMqayHKF+sebTCtWcnhzUelA+iM+ivKleqrjoLsmrtHZOGfnHOWXYJpDwU!
# известно, что агенты используют для шифрации-дешифрации простейший алгоритм - после каждой буквы исходной фразы, 
# добавляют определенное число случайных символов. Чтобы скрыть первую букву, добавили и перед ней такое же количество случайных символов. 
# Ваши специалисты узнали, что это число - 10. расшифруйте послание.

# Реализация скорее выглядит как пример как не нужно писать код. Если чесно то застопорился с решением данной задачи. В дальнейшем подумаю над
# лучшим способом реализации и по другому ее решу.


secret_key = "VZoFPzGvXwtbR+guMLszPhfvZotHwDm-emryhEXAaBW+-AbMdmEK+ztGDWyIzSFvjaFrHLzhoRqgsQraUdnSBGykFWNLOxTVKM+ynHqsVrQGEiqdKULoDVZcsZ-BpTWkDVR+jSgrfQZhUAdWCxtwOmTBQo+qWOlYyvGxnNpZFlTSrmaesQOotBLnVw!gOUrhz+F-DctdKWvTGhMUopoSPyFAXdJnY+DGFZQbOVgzaqsGvWjtBrJjBWhAFgryaTtwginpEsWtAuOxbgI-ZVunVAIuklBqTlSGUnevwEMqayHKF+sebTCtWcnhzUelA+iM+ivKleqrjoLsmrtHZOGfnHOWXYJpDwU!"
a = (secret_key[10:11])
b = (secret_key[21:22])
c = (secret_key[32:33])
d = (secret_key[43:44])
e = (secret_key[54:55])
f = (secret_key[65:66])
g = (secret_key[76:77])
h = (secret_key[87:88])
i = (secret_key[98:99])
k = (secret_key[109:110])
l = (secret_key[120:121])
m = (secret_key[131:132])
n = (secret_key[142:143])
o = (secret_key[153:154])
p = (secret_key[164:165])
q = (secret_key[175:176])
r = (secret_key[186:187])
s = (secret_key[197:198])
t = (secret_key[208:209])
u = (secret_key[219:220])
v = (secret_key[230:231])
w = (secret_key[241:242])
x = (secret_key[252:253])
y = (secret_key[263:264])
z = (secret_key[274:275])
za = (secret_key[285:286])
zb = (secret_key[296:297])
zc = (secret_key[307:308])
zd = (secret_key[318:319])
ze = (secret_key[329:330])
zf = (secret_key[340:341])
zg = (secret_key[351:352])
print(a+b+c+d+e+f+g+h+k+l+m+n+o+p+r+s+t+u+v+w+x+y+z+za+zb+zc+zd+ze+zf+zg)



#** 6. Написать скрипт, который просит пользователя ввести строку и 
# выводит на печать эту строку задом на перед. 
# (то есть при вводе hello скрипт генерирует вывод - olleh)

input_surname = str(input("Введите  вашу Фамилию:"))
print(input_surname[::-1])