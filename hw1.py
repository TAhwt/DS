# Условие:
# Создать список
# заполнить созданный список элементами различных типов данных
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе



# создаем список
my_list = []
# создаем элементы разных типов данных
my_int = int(1)
my_float = float(-2.5)
my_str = str("строка текста")
# заполняем список
my_list.append(my_int)
my_list.append(my_float)
my_list.append(my_str)
# определяем индекс каждого элемента
index_first = my_list.index(my_int)
index_second = my_list.index(my_float)
index_third = my_list.index(my_str)
# вытаскиваем элемент по определенным индексам
element1 = my_list[index_first]
element2 = my_list[index_second]
element3 = my_list[index_third]
# проверяем тип данных
print(f"{type(element1)}, {type(element2)}, {type(element3)}")
