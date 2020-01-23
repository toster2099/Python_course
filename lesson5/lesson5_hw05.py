# Задачи из слайда:

# Задание 1
# 1) Необходимо хранить информацию о курсе доллара (840), евро (978), злотых (985) относительно гривны (980) и курс евро относительно доллара.
# В словаре должно быть четыре элемента - курс доллара относительно гривны - 25.6, курс евро относительно гривны - 28.2, курс злотых к гривне - 6.5, и курс
# евро к доллару - 1.1

USD_UAH = (840,980)
EUR_UAH = (978,980)
ZLO_UAH = (985,978)
EUR_USD = (978,840)
currency_USD_UAH = [1,25.6]
currency_EUR_UAH = [1,28.2]
currency_ZLO_UAH = [1,6.5]
currency_EUR_USD = [1,1.1]
currency = {USD_UAH : currency_USD_UAH, EUR_UAH : currency_EUR_UAH, ZLO_UAH : currency_ZLO_UAH, EUR_USD : currency_EUR_USD}
print(currency)

# Задание 2
# 2) Необходимо распарсить строку(выбрать одну) и сохранить в словарь информацию о персоне. Для хранения имени, использовать вложенный
# словарь с ключами first_name, last_name. Для хранения информации о зарплате использовать словарь с ключами - amount и currency.
# На выходе должен быть словарь вида
#  {'name': {'first_name': 'Harry', 'last_name': 'Potter'}, 'age': 30,
# 'profession': 'auror', 'salary': {'amount': 127.45, 'currency': 'galeon'}}

variable_1 = "harry potter; 30; 127.45 galeon; auror"
pars_one, pars_two = variable_1.split(";",1)
value_first_name, value_last_name = pars_one.split(" ",1)
first_name, last_name = value_first_name.title(),value_last_name.title()
value_age, value_other = pars_two.split(";",1)
one, value_profession = value_other.split(";",1)
value_amount, value_currency = one.split()
profession = value_profession.strip()
age = int(value_age)
amount = float(value_amount)
dictionary_one = {"first_name":first_name,"last_name":last_name}
dictionary_two = {"amount":amount,"currency":value_currency}
total_dictionary = {"name":dictionary_one,"age":age,"profession":profession,"salary":dictionary_two}
print(total_dictionary)

variable_1 = "harry potter; 30; 127.45 galeon; auror"
pars_one, pars_two, pars_three, pars_four = variable_1.split(";",3)
list1,list2,list3 = pars_two.split(),pars_three.split(),pars_four.split()
value_amount, value_currency = list2[0],list2[1]
name, surname = pars_one.split()
name, surname = name.title(), surname.title()
age = list1[0]
value_age = int(age)
value_amount = float(value_amount)
value_position = list3[0]
dictionary_name = {"first_name":name,"last_name":surname}
dictionary_money = {"amount":value_amount,"currency":value_currency}
total_dictionary = {"name":dictionary_name,"age":age,"profession":value_position,"salary":dictionary_money}
print(total_dictionary)

# Задания для выполнения дз телеграм

# 2. написать скрипт для генерации словаря для шифра Цезаря, https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%A6%D0%B5%D0%B7%D0%B0%D1%80%D1%8F
# Выбрать шаг, например 3. Ключи - символы латинского алфавита, в нижнем регистре. Значения - тоже символы, соответствующие ключам согласно шифру.
# То есть скрипт должен формировать словарь вида {‘a’: ‘d’, ‘b’: ‘e’, ‘c’: ‘f’, … , ‘z’: ‘c’ }

import string
a = string.ascii_lowercase
keys_of_value = list(a)
sequence_without_abc = list(a[3::])
end_of_the_sequence = a[:3]
sequence_without_abc.extend(end_of_the_sequence)
total_dictionary = dict(zip(keys_of_value,sequence_without_abc))
print(total_dictionary)

# 4) Написать скрипт, который будет создавать новый файл с именем new.txt втекущей директории, записывать в него три строки - первую строку с
# помощью метода write, а две другие - с помощью метода writelines. Закрытьфайл. Открыть файл в режиме чтения и вывести на печать все его содержимое.

with open('new.txt', 'w') as f:
    f.write('first string ')
    f.writelines('second string ')
    f.writelines('third string')
    f.close()
with open('new.txt', 'r') as f:
    lines = f.readlines()
    print(lines,type(lines))

# Задачи из мини-екзамена которые я не сделал
# 5. Зашифровать слово hello шифром Цезаря со сдвигом 4. (* и расшифровать зашифрованное, проверить)

variable = "hello"
slice_one = variable[3:]
slice_two = variable[:3]
list_for_code = list(slice_one+slice_two)
list_for_code = tuple(list_for_code)
original = tuple(variable)
code_name = (zip(original,list_for_code))
print(code_name)
decoded_name = str(zip(list_for_code,original))
print(decoded_name)

# 6. Необходимо распрасить информацию о продукте из файла products.txt в словарь вида. 
# {«name»: str, «produced»: {«country»: str, «city»: str}, min_price: {currency, amount}, max_price: {currency, amount} }
# Валюта currency в результирующем словаре должна быть числовым кодом, согласно соответствию curr_ codes = {«uah»: 980, «rub»: 643}

with open ('products.txt', 'r') as f:
     line = f.readlines()
     result = line[0].split(";")
     name_prod,geographic = result[0], result[1]
     country, city = geographic.split()
     result_two, result_three = result[2],result[3]
     min_price, max_price = result_two.split(" "),result_three.split(" ")
     min_price,max_price = float(min_price[1]), float(max_price[1])
     currency = int("980")
     city_dict = {"country":country,"city":city}
     min_price_dict,max_price_dict = {currency:min_price}, {currency:max_price}
     total_dict = {"name":name_prod,"produced":city_dict,"min_price":min_price_dict,"max_price":max_price_dict}
     print(total_dict)



