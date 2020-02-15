# Задание 1. 
# Сгенерировать список из 10 случайных чисел. Вывести на печать
# Упорядочить в порядке возрастания. Вывести на печать отсортированный список.

import random
new_list = []
for item in range(10):
    item = random.randint(1,100)
    new_list.append(item)
print(new_list)
new_list.sort(reverse=False)
print(new_list)

# Задание 2.
# Сформируйте словарь с информацией о валютах и выведите на печать ключ и соответствующее значение по примеру:
# print(f“{key} => {value}”)
# Взять  три валюты: (980 → UAH), (840 → USD), (643 → RUB)

currency_dict = {980:"UAH",840:"USD",643:"RUB"}
for key,value in currency_dict.items():
    print(f"{key} => {value}")

#Задание 3
# Распарсить файл с информацией о плательщиках в список словарей вида {name: str, amount: float, currency: int}, вывести на печать полученный список.
# Содержимое файла:
# Remus Lupin;329.76 USD;2018-08-20 19:36:32;out;
# Severus Snape;397 USD;2018-08-20 20:22:26;out;
# Lucius Malfoy;847.44 USD;2018-08-20 22:51:55;out;
# Ron Weasley;929.93 USD;2018-08-20 19:33:58;out;
# Sirius Black;573.58 USD;2018-08-20 06:47:05;out;
# Harry Potter;930.93 USD;2018-08-20 18:08:20;out;

total_dict = {}
total_list = []
with open('Harry.txt') as f:
    lines = f.readlines()
for line in lines:
    splitted = line.split(";")
    currency_result = splitted[1]
    amount,currency = currency_result.split(" ")
    amount,currency = float(amount),str(currency)
    total_dict = {"name":splitted[0],"amount":amount,"currency":currency}
    total_list = [total_dict]
    print(total_list)
  
# Задание 4
# Написать скрипт который просит ввести  пароль,пока  не введет пароль password

secret = "password"
input_password = ""
while input_password != secret:
    input_password = input("Input the password please!:")
    print("Invalid password!")
print("The password is correct")





