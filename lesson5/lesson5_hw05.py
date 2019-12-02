# 1) Необходимо хранить информацию о курсе доллара (840), евро (978), злотых (985) относительно гривны (980) и курс евро относительно доллара.
# В словаре должно быть четыре элемента - курс доллара относительно гривны - 25.6, курс евро относительно гривны - 28.2, курс злотых к гривне - 6.5, и курс
# евро к доллару - 1.1

# USD_UAH = (840,980)
# EUR_UAH = (978,980)
# ZLO_UAH = (985,978)
# EUR_USD = (978,840)
# currency_USD_UAH = [1,25.6]
# currency_EUR_UAH = [1,28.2]
# currency_ZLO_UAH = [1,6.5]
# currency_EUR_USD = [1,1.1]
# currency = {USD_UAH : currency_USD_UAH, EUR_UAH : currency_EUR_UAH, ZLO_UAH : currency_ZLO_UAH, EUR_USD : currency_EUR_USD}
# print(currency)

# 2) Необходимо распарсить строку(выбрать одну) и сохранить в словарь информацию о персоне. Для хранения имени, использовать вложенный
# словарь с ключами first_name, last_name. Для хранения информации о зарплате использовать словарь с ключами - amount и currency.
#  {'name': {'first_name': 'Harry', 'last_name': 'Potter'}, 'age': 30,
# 'profession': 'auror', 'salary': {'amount': 127.45, 'currency': 'galeon'}}


variable_1 = "harry potter; 30; 127.45 galeon; auror"
#variable_2 = "ross geller; 34; 6500.45 usd; paleontologist"
var_1 = str(variable_1.split(' '))
print(var_1)
var_2 = str(var_1.split(';'))
print(var_2)
#var_2 = str(var_1.split(' '))
#print(var_2[0])


