#Пользователь вводит время в секундах.
#Переведите время в часы, минуты и секунды и
#выведите в формате чч:мм:сс.
#Используйте форматирование строк.

time_from_user = int(input('Введите время в секундах: '))
my_hours = time_from_user // 3600
my_minuts = (time_from_user - my_hours * 3600) // 60
my_seconds = (time_from_user - my_hours * 3600 - my_minuts * 60)
print(my_hours, ':', my_minuts, ':', my_seconds)
print(f"{my_hours}:{my_minuts}:{my_seconds}")