__author__ = 'Mackuson Evgeniya'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
number = int(input("Любое число от 0 до 15"))

while number<15:
    print(number)
    number = number + 1

print("Цикл завершён")




# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = 1
b = 5
temp = a
a = b
temp = b
print(a)




# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"







m = int(input("Укажите Ваш возраст"))
if m >= 18:
      print("Доступ разрешен")
else: print("Извините, пользование данным ресурсом только с 18 лет")
