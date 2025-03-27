# name = "admin" # переменная
# from operator import truediv

# print("Hello, Python!!!")
# print(name)
# print("Hello,", name, "!")
# print("Hello,"+ name + "!")
# age = 20
# print(age)
# print(name + str(age)) # преобразовать в одному типу данных
# print(type(name))
# age = 15.2
# print(type(age))


# a = 4
# b = 5
# print(id(a)) # выводим адрес в памяти, где располагается переменная
# print(id(b))
# a = b # 5
# print(a)
# print(id(a))
# print(id(b))


# a = b = c = 1
# print(a)
# print(b)
# print(c)

# a, b, c = 5, "Hello", 9.2
# print(a)
# print(b)
# print(c)


# name = "admin"
# print(name)
#
# _first_name = "adm"
# print(_first_name)

# import keyword # ввести в консоли
# keyword.kwlist

# второй способ
# import keyword
# print(keyword.kwlist)
# ключевые слова ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',
# 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
# 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# константы, можно перезаписывать, записывают в верхнем регистре
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)


# name = "Никита"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.") # нужно приводить к одному типу данных
# print("Меня зовут ", name, ". Мне ", age, " лет.") # можно через запятую, но не корректно будут отображаться пробелы,
# запятая автоматически после себя добавляет пробел


# a = 1
# b = 2
#
# print("a:", a)
# print("b:", b)

# первый спобоб с помощью доп переменной:
# c = a # 1
# a = b # 2
# b = c # 1

# второй способ через множественное присваивание:
# a, b = b, a

# третий способ со сложением/вычитанием:
# a = a + b # 1 + 2 = 3
# b = a - b # 3 - 2 = 1
# a = a - b # 3 - 1 = 2

# print("a:", a)
# print("b:", b)


# print("строка "
#       "символов")
# print("строка \
#       символов")
# print('строка '
#       'символов')
# print('строка \nсимволов')
# print("\tДокумент \"file.txt\" находится по     пути: D\\folder\\file.txt") # экранируем кавычки
# print("\tДокумент \"file.txt\" находится по     пути: \rD\\folder\\file.txt") # возврат каретки удаляет что перед ним


# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + "___"
# print(s3 * 3) # умножение строк


# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 4)
# print(6 // 4) # целочисленное деление
# print(7 / 2)
# print(7 // 2)
# print(7 ** 2) # число 7 степень 2
# print(7 % 2) # остаток от деления


# a = 5
# b = 7
# c = 3
# res = a + b + c
# print("Сумма:", (a + b + c))
# print("Сумма:", res)
# print("Произведение:", (a * b * c))
# print("Среднее арифметическое:", (a + b + c)/3)
# print("Среднее арифметическое:", res/3)


# print(6 + 4 * 5 ** 2 + 7) # 113 сначала возведение в степень, потом умножение, +/- слева направо
# print((6 + 4) * (5 ** 2 + 7)) # 320


# num = 10
# num += 5 # 15
# print(num)
#
# num -= 3
# print(num) # 12
#
# num *=4 # 48
# print(num)
#
# num **= 2 # 2304
# print(num)


# РАЗВЕРНУТЬ ЧИСЛО
# num = 4321
# print("Исходное число:", num)
# a = num % 10  # остаток от деления 4321 на 10 = 1
# print("a:", a)
# num = num // 10  # 4321 // 10 = 432
# print(num)  # 432
# b = num % 10  # остаток от деления 432 на 10 = 2
# print("b:", b)
# num = num // 10  # 432 // 10 = 43
# print(num)
# c = num % 10  # остаток от деления 43 на 10 = 3
# print("c:", c)
# num = num // 10  # 43 // 10 = 4
# print(num)
# d = num
# print(num)
#
# print("Обратное число:", a * 1000 + b * 100 + c * 10 + d)
# print("Обратное число:", str(a) + str(b)+ str(c) + str(d))

# Второй вариант решения:
# num = 4321
# print("Исходное число:", num) # 4321
# res = num % 10 * 1000 # 1000
# num //= 10 # 4321/10 = 432
# res += num % 10 * 100 # 1000 + 2(остаток от деления 432/10) * 100 = 1200
# num //= 10 # 432/10 = 43
# res += num % 10 * 10 # 1200 + 3*10 = 1230
# num //= 10 # 43/10 = 4
# res += num % 10 # 1230 + 4
# print("Обратное число:", res)
#
# # Подставляем любые числа и он считает
# num = 5847
# print("Исходное число:", num)
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print("Обратное число:", res)


# num1 = "2"
# num2 = 3
# res = int(num1) + num2 # 5 - привели строку к числу
# print(res)
# res = num1 + str(num2) # 23 - привели число к строке
# print(res)


# print(3.8)
# print(int(3.8)) # отбрасывает дробное число
# print(round(3.8)) # округляет по законам математики
# print(type(round(3.8))) # сразу преобразовывает в целое число int
# print(round(3.891, 2)) # если передаем второе число - кол-во числе после запятых
# print(type(round(3.89154, 2))) # если указано второе число - приводит к типу float


# a = '5.2'
# b = 10
# # c = int(a) + b # тип данных int не воспринимает . и выдает ошибку, нужно преобразовать к типу данных float
# c = float(a) + b
# print(c)


# name = "Виктор"
# age = 28
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="", end="\n\n") # sep убирает все пробелы после запятой
# print("Новая строка") # end следующую строку не переносит


# name = input("Введите имя: ")
# print("Ваше имя:", name)


# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)


# print(2 * 3) # из учебника практика
# print(2 * 3.)
# print(2. * 3)
# print(2. * 3.)

# print(6 // 3)
# print(6 // 3.)
# print(6. // 3)
# print(6. // 3.)

# print("Tell me anything...")
# anything = input()
# print("Hmm...", anything, "... Really?")

# anything = input("Tell me anything...")
# print("Hmm...", anything, "...Really?")


# fnam = input("May I have your first name, please? ")
# lnam = input("May I have your last name, please? ")
# print("Thank you.")
# print("\nYour name is " + fnam + " " + lnam + ".")


# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# num4 = int(input("Введите четвертое число: "))
# sum12 = num1 + num2
# sum34 = num3 + num4
# print(sum12)
# print(sum34)
# res = sum12 / sum34
# print("Результат: ", round(res, 2))


# b1 = True # 1 неявное преобразование типов
# b2 = False # 0
# print(type(b1))
# print(type(b2))
# print(b1 + 5) # 1 + 5
# print(b2 + 5) # 0 + 5


# False => "" - пустая строка, 0, 0.0, False, None

# print(bool("python")) # true
# print(bool("")) # false
# print(bool(" ")) # true
# print(bool(5)) # true
# print(bool(0)) # false
# print(bool(0.1)) # true
# print(bool(0.0)) # false
# print(bool(False)) # false
# print(bool(None)) # false
#
# a = None # переменная без значения, оно придет позже
# print(a)
# print(type(a))


# print(7 == 7)
# print(2 + 5 == 7) # у арифм операторов приоритет выше, сначала вычисление потом равенство
# print(2 + 5 == 7 / 3)
# print(2 + 5 != 7 / 3)
# print(8 > 5)
# print(8 > 8)
# print(8 >= 8)
# print("привет" > "ПРИВЕТ")
# print("привет" < "ПРИВЕТ") # коды символов 112 > 80


# print(2 < 4 < 9) # true (2 < 4) && true (4 < 9) => true
# print(2 * 5 > 7 >= 4 + 3)
# print(3 * 3 <= 7 >= 2)


# a = 10
# b = 5
# c = a == b # в переменной булевое значение
# print(a, b, c)


# print(5 - 3 == 2 and 1 + 3 == 4)  # True and True => True
# print(5 - 3 == 2 and 1 + 3 < 4)  # True and False => False
#
# print(5 - 3 == 2 or 1 + 3 == 4)  # True or True => True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True or False => True
#
# print(not 9 - 5)  # False
# print(not 7 - 7)  # True

# a = 5
# print("a:", a)


# account = int(input("Enter how much you put: "))
# account = abs(account)
# if account > 0:
#     withdrawal = int(input("Enter how much you take: "))
#     withdrawal = abs(withdrawal)
#     if withdrawal < account:
#         account -= withdrawal
#         print("Here are your", withdrawal, ".")
#         print("There are", account, "left.")
#     else:
#         print("There are only", account, ".")
# else:
#     print("There are no money in piggy bank")


# cnt = 15
# if cnt < 10:
#     cnt += 1
#     print(cnt)


# age = int(input("Введите свой возраст: "))
# if age >= 18: # "20" >= 18
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")


# a = 5
# b = 5
# if a > b:
#     print("a > b")
# elif a == b:
#     print("a == b")
# else:
#     print("b > a")


# a = input("Введите первую сторону:")
# b = input("Введите вторую сторону:")
# c = input("Введите третью сторону:")
#
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or b == c or a == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")


# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5: # (day >= 1) and (day <=5)
#     print("Рабочий день - ")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день", end="")
#     if day == 6
#         print("суббота")
#     if day == 7
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")


# month = int(input("Введите номер месяца (цифрой): "))
# if month == 1 or month == 2 or month == 12:
#     print("Зима")
# elif 3 <= month <= 5: # month == 3 or month == 4 or month == 5
#     print("Весна")
# elif 6 <= month <= 8: # month == 6 or month == 7 or month == 8
#     print("Лето")
# elif 9 <= month <= 11: # month == 9 or month == 10 or month == 11
#     print("Осень")
# else:
#     print("Ошибка ввода данных")


# ВТОРОЙ ВАРИАНТ СО ВЛОЖЕННЫМИ УСЛОВИЯМИ
# month = int(input("Введите номер месяца (цифрой): "))
# if 1 <= month <= 12:
#     print("Время года: ", end="")
#     if month == 1 or month == 2 or month == 12:
#         print("Зима")
#     if 3 <= month <= 5: # month == 3 or month == 4 or month == 5
#         print("Весна")
#     if 6 <= month <= 8: # month == 6 or month == 7 or month == 8
#         print("Лето")
#     if 9 <= month <= 11: # month == 9 or month == 10 or month == 11
#         print("Осень")
# else:
#     print("Ошибка ввода данных")


# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9: # pass или ... - заглушка чтобы проверить пустое условие
#     print("На ветке ", end="")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if 5 <= n <= 9 or n == 0:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода")


# ВТОРОЙ ВАРИАНТ
# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ворон", end="")
#     if n == 1:
#         print("а", n)
#     if 2 <= n <= 4:
#         print("ы", n)
#     if 5 <= n <= 9 or n == 0:
#         print("", n)
# else:
#     print("Ошибка ввода")


# ТРЕТИЙ ВАРИАНТ
# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ворон", end="")
#     if n == 1:
#         print("а", n)
#     elif 2 <= n <= 4:
#         print("ы", n)
#     else:
#         print("", n)
# else:
#     print("Ошибка ввода")


# match выражение:
#     case шаблон_1:
#         действие_1
#     case шаблон_2:
#         действие_2
#     case _:
#         значение по умолчанию


# АНАЛОГ SWITCH
# password = "admin"
#
# match password:
#     case "admin":
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#     case _:
#         print("Пароль неверен")


# day = 'понедельник'
# time = 5
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 12 or 14 <= time <= 17:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")


# ТЕРНАРНОЕ ВЫРАЖЕНИЕ
# a, b = 30, 20
# print(a if a < b else b)


# a, b = 30, 0
# print("На 0 делить нельзя" if b == 0 else a / b)


# ИСКЛЮЧЕНИЯ
# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на 0")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки")
#     print("Нельзя делить на 0")
# else: # когда в блоке try не возникло исключение
#     print("Все нормально. Вы ввели", n, "и", m)
# finally: # выполняется в любом случае
#     print("Конец программы")


# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(str(n) + str(m))

# ВТОРОЙ ВАРИАНТ РЕШЕНИЯ
# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)


# ЦИКЛЫ

# while условие:
#     блок_кода

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1


# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1
#
# # ВТОРОЙ ВАРИАНТ РЕШЕНИЕ
# print()
# j = 2
# while j <= 20:
#     print(j, end=" ")
#     j += 2


# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# # ВТОРОЙ ВАРИАНТ РЕШЕНИЯ
# n = int(input("Укажите количество символов: "))
# print("*" * n)
#
# # ТРЕТИЙ ВАРИАНТ РЕШЕНИЯ
# n = int(input("Укажите количество символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1


# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
#
# while a <= b:
#     if a % 2:
#         print(a, end=" ")
#         res += a
#     a += 1
# print()
# print("Сумма нечетных чисел: ", res)


# n = input("Введите целое число: ")
#
# while type(n) is not int: # !=
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")


# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break


# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n
# print("Результат: ", res)


# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else: # выводится если цикл отработал без прерывания
#     print("Цикл окончен, i =", i)


# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)


# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# for element in collection:
# print(element)

# for i in "Hello":
#     print(i)
#
# for i in "Hello", "World":
#     print(i)


# range(start = 0 по умолчанию, можно не указывать, stop, step=1 по умолчанию, можно не передавать)
# второй параметр обязательно надо передавать
# print(range(1, 10, 2))
#
# for i in range(1, 10, 2):
#     print(i, end=" ")
#
#
# for i in range(10): # i = 0, i < 10, i += 1
#     print(i, end=" ")

# если хотим уменьшать все параметры:
# for i in range(10, 0, -2):
#     print(i, end=" ")

#
# print()
# j = 1
# while j < 10:
#     print(j, end=" ")
#     j += 2


# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")


# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")
#
# print()
#
# for i in range(11, 100, 11):
#     print(i, end=" ")
#
# print()
#
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")


# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("Конец цикла")


# for i in range(3):
#     if i == 1:
#         continue
#     print(i)
# else:
#     print("Конец цикла")


# вложенный цикл
# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")


# w = 12
# h = 4
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()


# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()


# string = [letter * 2 for letter in "Python"]
# print(string)
#
# for letter in "Python":
#     print(letter * 2, end="\t")


# num = [i for i in range(30) if i % 2 ==0]
# print(num)
#
# print()
#
# for i in range(30):
#     if i % 2 == 0:
#         print(i, end="\t")


# СПИСОК (list)
# nums = [8, 3, 9, 4, 1]
# print(nums)
# print(type(nums))
#
# num1 = list([8, 3, 9, 4, 1])
# print(num1)


# nums = [8, 3, 9, 4, 1, "one", True]
# print(nums)
# print(nums[0])
# print(nums[-5])
# print(nums[4])
# print(nums[-1])
# print(nums[-2])


# nums = [8, 3, 9, 4, 1]
# print(nums)
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)


# nums = [8, 3, 9, 4, 1]
# print(nums, id(nums))
# print(nums[0], id(nums[0]))
# print(nums[1], id(nums[1]))
# nums[1] = 256
# print(nums[1], id(nums[1]))
# print(nums, id(nums))
# #print(nums[5]) - # вышли за пределы списка - ошибка
# print("Длина списка:", len(nums))


# nums = [8, 3, 9, 4, 1]
# nums2 = [11, 12, 12]
# n = nums + nums2
# print(n)
# print(n * 2)
# print(n * 3)


# print(list("Hello"))
#
# print(range(10))
# print(list(range(10)))
# print(list(range(2, 10)))
# print(list(range(10, 2, -2)))


# [выражение for переменная in последовательность]

# a = [0 for _ in range(5)]
# print(a) # [0, 0, 0, 0, 0]
#
# a = ["*" for _ in range(5)]
# print(a)

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a) # [1, 4, 9, 16]


# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)


# второй вариант в одну строку
# a = [input("-> ") for i in range(int(input("n = ")))]
# print(a)


# a = list(range(10, 100, 10))
# print(a)
#
# for i in range(len(a)):
#     print(a[i] + 2, end=" ")
# print()
#
# for i in a:
#     print(i, end=" ")


# домашнее задание РЕШИЛА Я
# a = [input("-> ") for i in range(int(input("n = ")))]

# a = [0] * int(input("Введите количество элементов списка: "))
# for i in range(len(a)):
#     a[i] = int(input("-> "))
#     sum = 0
#     for num in a:
#         if num < 0:
#             sum += num
#     # while a[i] < len(a):
#     #     sum += a[i]
# print("Сумма отрицательных элементов:", sum)

# ДОМАШНЕЕ ЗАДАНИЕ НА УРОКЕ РАЗБОР
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print("Сумма отрицательных элементов:", s)

# ВТОРОЙ ВАРИАНТ ЧЕРЕЗ WHILE
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# s = 0
# i = 0
# while i < len(a):
#     if a[i] < 0:
#         s += a[i]
#     i += 1
# print("Сумма отрицательных элементов:", s)

# еще один вариант решения:
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# s = 0
# for v in a:
#     if v < 0:
#         s += v
# print("Сумма отрицательных элементов:", s)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
#
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
#
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
#
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
#
# for i in a:
#     if i > i - 1:
#         print(i, end=" ")


# n = list(range(21, 41))
# print("Список: ", n)
# k = s = 0
# for i in range(len(n)):  # range(0, len(a), 1)
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Количество четных элементов: ", k)
# print("Сумма нечетных элементов: ", s)


# второй вариант решения
# n = list(range(21, 41))
# print("Список: ", n)
# k = s = 0
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
# print("Количество четных элементов: ", k)
# print("Сумма нечетных элементов: ", s)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# k = s = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         s += a[i]
#         k +=1
# print("Среднее арифметическое: ", s / k)


# lst = [7, 9, 2, 1, 17]
# print(lst)
# lst[0], lst[1] = lst[1], lst[0]
# print(lst)


# срез
# список[start:stop:step]
#
# s = [9, 7, 2, 1, 17]
# print(s)
# print(s[1:4])
# print(s)
# print(s[:]) # от начала и до конца списка
# print(s[2:]) # со 2-го индекса и до конца
# print(s[:2]) # от начали и до 2-го не включая
# print(s[::2]) # от начала и до конца каждый 2 элемент
# print(s[::-1]) # развернет список
# print(s[0:-1]) # убирает последний элемент
# print(s[10:201]) # нет ошибки пустой список - если не существующие списки


# lst = list(range(1, 8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[::-7])
# print(lst[-1:])
# print(lst[3:4])
# print(lst[4:7])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])


# st = "Hello World"
# print(st[1:3])
# print(st[::-1])


# st = "123456"
# print(st[1:3])
# num = st[::-1]
# print(num)
# print(type(num))
# num = int(num)
# print(num)
# print(type(num))


# lst = list(range(1, 8))
# print(lst)
# lst[1:3] = [0, 0, 0, 0]
# print(lst)
# lst[1:2] = [20]
# print(lst)
# lst[1] = 40
# print(lst)
# lst[1] = [40, 8, 2]
# print(lst)
# lst[15:16] = [100]
# print(lst)
# print(len(lst))


# методы списков 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
# print(dir(list))

# lst = list(range(1, 8))
# print(lst)
# lst.append(99) # добавляет элемент в конец списка
# print(lst)
# lst.extend([1, 2, 3]) # добавляет список елементов в конец списка
# print(lst)
# lst.insert(0, 100) # первый параметр - индекс, второй параметр - сам элемент
# print(lst)


# s = []
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)
# print(s)


# a = [5, 9, 2, 1, 4, 3, 4, 2]
# b = [4, 2, 1, 3, 7]
# c = []
#
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)


# второй вариант
# a = [5, 9, 2, 1, 4, 3, 4, 2]
# b = [4, 2, 1, 3, 7]
# c = []
#
# for element in a:
#     if element not in c and element in b: # if element in b and element not in c
#         c.append(element)
# print(c)


# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# num = a.count(6)
# print(num)


# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(a)
# for i in a: # выводит сами значения
#     print(i, end=" ")
#
# print()
#
# for i in range(len(a)): # выводит (не) индексы а сколько чисел, чтобы получить элемент - обратиться по индексу
#     print(a[i], end=" ")


# a = [1, 2, 3, 4, 5, 6]
# b = [11, 22, 33,]
# c = []
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)


# a = [1, 2, 3]
# b = [11, 22, 33, 4, 5, 6]
# c = []
#
# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
#
# print(c)


# lst = [11, 1, 22, 2, 33, 3, 55, 66]
#
# lst[5:] = []
# print(lst)
#
#
#
#
# lst = [11, 1, 22, 2, 33, 3, 55, 66]
#
# lst[3:5] = []
# print(lst)
#
#
#
# lst = [11, 1, 22, 2, 33, 3, 55, 66]
#
# lst[:] = []
# print(lst)


# lst = [11, 1, 22, 2, 33, 3, 55, 66, 22]

# del lst[2]
# print(lst)

# lst.remove(22) # удаляет по значению первый элемент
# print(lst)
#
#
# last = lst.pop() # удаляет последний элемент из списка и возвращает его
# print(last)
#
# second = lst.pop(0) # удаляет элемент по индексу и может вернуть его, если индекса нет - то исключение
# print(second)
# print(lst)
#
# lst.clear() # удаляет все из списка
# print(lst)


# print("Введите элементы списка: ")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print("Введите индекс: ")
# k = int(input("k = "))
# a.pop(k)
# print(a)


# lst = [11, 1, 22, 2, 33, 3, 55, 66, 22, 33]
# value = 33
# if value in lst:
#     ind = lst.index(value, 5) # находит первый индекс
#     print(ind)
# print(lst)


# lst = [11, 1, 22, 2, 33, 3, 55, 66, 22, 33]
# a = lst.copy() # создает копию списка
# print(lst, id(lst))
# print(a, id(a))
#
# a.append(100)
# print(lst)
# print(a)
#
# lst[0] = 256
# print(lst)
# print(a)


# print(dir(list))

# lst = [11, 1, 22, 2, 33, 3, 55, 66, 22, 33]
# lst.reverse() # разворачивает список
# print(lst)

# lst = [11, 1, 22, 2, 33, 3, 55, 66, 22, 33]
# lst.sort(reverse=True)
# print(lst)
#
# s = ["Виталий", "Сергей", "Александр", "Анна"]
# s.sort(reverse=True)
# print(s)
#
# s = ["Виталий", "Сергей", "Александр", "Анна"]
# s.sort(reverse=False)
# print(s)
#
# s = ["Виталий", "Сергей", "Александр", "Анна"]
# s.sort(key=len, reverse=True)
# print(s)


# lst = [11, 1, 22, 2, 33, 3, 55, 66, 22, 33]
# lst.sort(reverse=True)
# print(lst)
#
# new_lst = sorted(lst, reverse=True) # не меняет старый список, создает новый
# print(new_lst)

# st = "Hello"
# new_lst = sorted(st, reverse=True)
# print(new_lst)
# print(st)


# ГЕНЕРАЦИЯ СЛУЧАЙНЫХ ДАННЫХ

# import random # в самый верх документа или после комментариев
# print(random.random()) # от 0 до 1
# print(random.randint(5, 10)) # от 5 до 10 - 10 включает
# print(random.randrange(10)) # от 0 до 10 - если 1 число, 10 не включает
# print(random.randrange(5, 10)) # от 0 до 10 - если 2 числа, от 1-го до последнего,  не включает
# print(random.randrange(5, 10, 2)) # от 5 до 10 (не включая) с шагом 2
# print(random.uniform(10.5, 25.5)) # вещественные числа


# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# s = [55, 66, 77, 88, 99, 5, 7, 9, 1, 2, 4, 3, 8]
# print(random.choice(city_list)) # случайное из списка - один
# print(random.choice(s)) # случайное из списка - один
# print(random.choices(city_list, k=3)) # 3 случайных - могут дублироваться
# print(random.choices(s, k=3)) # список случайных
# random.shuffle(city_list) # перемешивает
# random.shuffle(s) # перемешивает
# print(city_list)
# print(s)


# import random
#
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
#
#
# print(mas)
# print(len(mas)) # длина списка
# print(min(mas)) # мин элемент
# print(max(mas)) # максимальные элемент
# print(sum(mas)) # сумма элементов списка


# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# maximum = max(mas)
# print("Max =", maximum)
# mas.remove(maximum)
# mas.insert(0, maximum)
#
# print(mas)


# import random
# mas = [random.randint(0, 10) for i in range(10)]
# print(mas)
# print(2 in mas)
# print(2 not in mas)


# lst = []
# # if len(lst) == 0:
# #     print("Список пустой")
#
# print(bool(lst))
#
# if not lst:
#     print("Список пустой")
# else:
#     print("В списке есть элементы")


# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# print(len(m))
# print(m[1])
# print(m[1][2])

# print("Вариант 1")
# for row in range(len(m)): # row 0 1 2
#     for col in range(len(m[row])): # col 0 1 2 3
#         print(m[row][col], end="\t")
#     print()
#
# print("Вариант 2")
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()


# МОДУЛИ

# import math
# print(math.sqrt(4)) # корень
# print(math.ceil(3.2)) # округление в верхнюю сторону
# print(math.ceil(3.8)) # округление в нижнюю сторону

# import math as m
# print(m.sqrt(4))
# print(m.ceil(3.2))
# print(m.ceil(3.8))

# from math import *
#
# print(m.sqrt(4))
# print(m.ceil(3.2))
# print(m.ceil(3.8))


# from math import sqrt, ceil, ceil
#
# print(m.sqrt(4))
# print(m.ceil(3.2))
# print(m.ceil(3.8))

# import math
# print(dir(math))


# from math import pi
# # print(pi)
#
# radius = int(input("Введите радиус окружности: "))
# print("Длина окнужности: ", round(2 * pi * radius, 2))


# import time


# import locale
# print(time.time())
# print(time.ctime())
# print(time.ctime(547))
# print(time.localtime())
# res = time.localtime()
# print(res.tm_year, "-0", res.tm_mon, "-0", res.tm_mday, sep="")
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))
#
# locale.setlocale(locale.LC_ALL, "ru")
# print(time.strftime("Сегодня: %B %d, %Y, %A", time.localtime(54546)))


# import time
# start = time.time()
# pause = 5
# print("Программа запущена")
# time.sleep(pause)
# result = time.time() - start
# print("Программа выполнена за", result, "секунд")


# import time
# start = time.monotonic()
# pause = 5
# print("Программа запущена")
# time.sleep(pause)
# result = time.monotonic() - start
# print("Программа выполнена за", result, "секунд")


# a = 5
# for i in range(a, -1, -1):
#     time.sleep(1)
#     print(i)


# s = [9, 7, 9, 7, 4, 3, 0, 5, 4 ,1]
# # s.sort() # сортирует исходных список
# a = sorted(s) # не меняет исходный список, делает новый список
# print(a)
# print(s)


# ФУНКЦИИ
# print()
#
#
# def hello(name, age):
#     print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
#
#
# hello("Irina", 28)
# hello("Ivan", 15)


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")


# def print_line(count, a, b):
#     # print((a + b) * count)
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# print_line(9, "+", "-")
# print_line(7, "X", "0")


# def get_sum(a, b):
#     print("Hello")
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)


# def max_value(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(max_value(9, 6))
# print(max_value(9, 16))


# def add(x, y):
#     if x > y:
#         return x - y
#     else:
#         return y + x
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# print(add(a, b))


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# # ВТОРОЙ ВАРИАНТ РЕШЕНИЯ
# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def is_first_big(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
# print(is_first_big(10, 5))
# print(is_first_big(5, 10))
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if is_first_big(a, b):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше первого")


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")


# def func(a, b=0):
#     return a + b
#
#
# print(func(2, 5))
# print(func(b=2, a=5)) # именнованный параметр
# print(func(2)) # позиционный параметр


# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
#
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 is lst2)
#
# a = "Hello"
# b = "Hello"
# print(a, id(a))
# print(b, id(b))
# print(a == b)
# print(a is b)


# lst1 = [1, 2, 3] # изменяемый тип данных (есть еще не изменяемый)
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))
# lst1.pop(1)
# print(lst1, id(lst1))


# a = "Hello" # неизменемый тип данных
# print(a, id(a))
# a = a + "!"
# print(a, id(a))


# a = 5
# print(a, id(a))
# a = a + 3
# print(a, id(a))


# КОРТЕЖ TUPLE

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
#
# print(lst[1])
# print(tpl[1])
#
# lst[1] = 50
# print(lst)
#
# tpl[1] = 50
# print(tpl)


# a = 1, 2, 3, 4, 5
# print(a, type(a))


# a = list("Hello")
# print(a, type(a))
# a = tuple("Hello")
# print(a, type(a))


# a = (1, 2, 3, 4, 5)
# print(a[2])
# print(a[1:3])


# print([i for i in range(10)])
# print(tuple(i for i in range(10)))

# from random import randint
#
# # print(tuple(input("->") for i in range(5)))
# print(tuple(randint(50, 100) for i in range(10)))
# print([i ** 2 for i in range(10)])


# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# # print(len(t3))
#
# print(t3.count("l"))
# print(t3.count("a"))
#
# print(t3.index("l", 4))
#
# if "a" in t3:
#     print(t3.index("a"))
# else:
#     print("Такого элемента нет")


# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
#
# for i in t3:
#     print(i, end=" ")


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) == 1:
#             return tpl[tpl.index(el):]
#         else:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first:second + 1]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# t = (True, 11, "Python", (4, 5, 6), ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# print(t, id(t))
# t[4].append("hi")
# print(t, id(t))


# распаковка кортежа
# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # print(user)
# # print(user[0])
# # print(user[1])
# # print(user[2])
# # first_name, year, married = user
# # print(first_name)
# # print(year)
# # print(married)
#
# first_name, year, married = get_user()
# print(first_name)
# print(year)
# print(married)


# lst = [1, 2, 3, 4, 5]
# print(lst, type(lst))
# tpl = tuple(lst)
# print(tpl, type(tpl))
# lst2 = list(tpl)
# print(lst2, type(lst2))
# lst2.append(6)
# tpl2 = tuple(lst2)
# print(tpl2, type(tpl2))


# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
#
# print(countries)
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", население = ",  country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")


# tpl = tuple(input('Введите строку: '))
# print(tpl)
# lst = []
# for i in range(len(tpl)):
#     if tpl[i] not in lst:
#         lst.append(tpl[i])
# print(lst)
# for i in range(len(lst)):
#     print('Количество', lst[i], '=', tpl.count(lst[i]))


# МНОЖЕСТВО (set) - хранит набор уникальных элементов, в рандомном порядке

# s = {"red", "yellow", "green", "yellow", "green"}
# print(s)
# print(type(s))
# print(len(s))


# a = ()
# print(a, type(a))
#
# a = {} # dict словарь
# print(a, type(a))
#
# a = set() # пустой сет только так создать
# print(a, type(a))
#
# a = set("hello")
# print(a, type(a))


# s = {i for i in range(10)}
# print(s)
#
# s = {i * i for i in range(10)}
# print(s)


# lst = [10, 2, 2, 2, 3, 3, 8, 8, 9, 9, 9, 10]
# # st = {i for i in lst if i % 2 == 0}
# # print(st)
# st = set(lst)
# print(st)
# lst2 = list(st)
# print(lst2)


# t = {"red", "yellow", "green"}
# print("green" in t)
# print("blue" in t)


# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# print([i for i in lst if "a" in i])
# print({i for i in lst if "a" in i})
# # print(tuple("A" if i[0] == "a" else "B" for i in lst))
# # print(tuple("A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst))
# print(["A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == "c"])


# вторая запись того что выше
# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# lst2 = []
# for i in lst:
#     if i[1] == "c":
#         if i[0] == "a":
#             lst2.append("A" + i[1:])
#         else:
#             lst2.append("B" + i[1:])
#
# print(lst2)


# print(dir(set))

# a = {"red", "yellow", "green"}
# print(a)
# a.add("black") # добавление элементов
# print(a)

# a.remove("yellow") # удаляет по значению
# print(a)

# a.remove("blue")  # KeyError
# print(a)

# el = "blue"
# if el in a:
#     a.remove("blue")
# print(a)
#
# el = "green"
# if el in a:
#     a.remove("green")
#     print(a)

# a.discard("yellow") # удаляет по значению и не выбрасывает исключение если элемента нет
# print(a)

# a.discard("blue")
# print(a)

# a.pop() # удаляет первый элемент из множества (любой)
# print(a)
#
# a.clear() # очистка множества
# print(a)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b) # {0, 1, 2, 3, 4}
# c = a | b # {0, 1, 2, 3, 4}
# print(c)

# a |= b # {0, 1, 2, 3, 4} перезаписал в существующий сет
# print(a)

# c = a & b
# print(c)

# c = a - b
# print(c)

# a -= b
# print(a)

# c = a ^ b
# print(c)

# a ^= b
# print(a)


# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print("Кол-во уникальных элементов:", len(s))
# print("Min:", min(s))
# print("Max:", max(s))


# s1 = "Hello"
# s2 = "How are you"
#
# a = set(s1) & set(s2)
# print(a)
#
# for i in a:
#     print(i, end="")


# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1} # подмножество a
# c = a <= b
# print(c)


# frosenset
# s = frozenset([1, 2, 3, 4, 5])
# print(s)
#
# a = frozenset({"Hello", "world"})
# print(a)


# СЛОВАРЬ (dict)

# lst = ["one", "two"]
# d = {"first": "one", "second": "two"}
#
# print(lst[1])
# lst[1] = ("ten")
# print(lst)
#
# d["second"] = "ten"
# print(d)


# d = {}
# d = dict(a="Hello", b="world")
# print(d)
# print(type(d))

# d1 = {"a": "Hello", "b": "world"}
# print(d1)


# d = {0: "text", "one": 45, (1, 2): [2, 3, 4, 5], True: 1, False: 0, "a": "Кортеж"} # ключи только неизменяемые типы данных
# print(d)


# user = [
#     ["a", 1],
#     ["b", 2],
#     ["c", 3],
# ]
#
# print(user)
# new_dict = dict(user)
# print(new_dict)


# d = {i : i ** 2 for i in range(1, 8)}
# print(d)
#
# # print(3 in d) # через оператор in - проверяем наличие ключа
# # print(25 in d)
#
# del d[3] # удаляется и ключ и значение
# print(d)
#
# key = 8
# # if key in d: # защита, если ключа не существует, он его удалять не будет и ошибки не будет
# #     del d[8] # ошибка ключа, такого не существует
#
# # второй вариант удаления ключа без ошибки
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом", key, "нет в словаре")
# print(d)


# d = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
#
# res = 1
#
# for key in d:
#     #print(key, ":", d[key])
#     res *= d[key]
#
# print(res)


# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# print(d)

# d = {i: input("->") for i in range(1, 5)}
# print(d)
#
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)


# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core-i5-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core i5-3450", 5, 6400],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n == "0":
#         break
#     else:
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print("Значение не корректное. Введите число")
#         else:
#             print("Такого ключа нет")
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")


# МЕТОДЫ СЛОВАРЕЙ

# d = {"A": 1, "B": 2, "C": 3}
#
# #print(dir(dict))
# print(d)
#
# print(d.keys()) # список ключей
# print(d.values()) # список значение
# print(d.items()) # список ключей и значений в виде кортежа
#
# for i in d:
#     print(i)
#
# for i in d.values():
#     print(i)
#
# for i, j in d.items():
#     print(i, ":", j)


# d = {"A": 1, "B": 2, "C": 3}
# d2 = d.copy() # возвращается копия словаря
# print("D =", d)
# print("D2 =", d2)
# d2["B"] = 5
# print("D =", d)
# print("D2 =", d2)


# d = {"A": 1, "B": 2, "C": 3}
# print(d)
# # d.clear() # удалили все элементы из словаря
# #item = d.pop("B") # удаление элемента по ключу
# # item = d.pop("D", "Такого ключа нет в словаре") # не ключа
# # item = d.pop("B", "Такого ключа нет в словаре") # не ключа
# item = d.popitem() # удаляет последний элемент и возвращается кортеж из ключа и значения
# print(d)
# print(item)


# d = {"A": 1, "B": 2, "C": 3}
# print(d)
# # print(d["W"])
# # value = d.get("W", "Такого ключа нет в словаре") # получает значение по заданному ключу
# # print(value)
# item = d.setdefault("B", 5) # по заданному ключу устанавливает значение по умолчанию
# print(d)
# print(item)


# d = {"A": 1, "B": 2, "C": 3}
# # d2 = {"R": 7, "Q": 9, "B": 100}
# d2 = [("R", 7), ("Q", 9)]
# print(d)
# print(d2)
# #d3 = d | d2
# d.update(d2)
# print(d)


# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# new_d = dict()
# new_d["name"] = d.pop("name")
# new_d["salary"] = d.pop("salary")
# print(d)
# print(new_d)


# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# d["location"] = d.pop("city")
# print(d)


# d = {
#     "first": {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "second": {
#         4: "four",
#         5: "five"
#     }
# }
# print(d)
#
# # for x in d:
# #     print(x)
# #     for y in d[x]:
# #         print("\t", y, ": ", d[x][y], sep="")
#
#
# for x in d:
#     print(x)
#     for i, j in d[x].items():
#         print("\t", i, ": ", j, sep="")


# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# d["salary"] = 100
# d["location"] = d.pop("city")
# print(d)
# lst = list(d.items())
# print(lst)


# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# # print({k: v for k, v in d.items()})
# print({v: k for k, v in d.items()})


# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# print({k: v for k, v in d.items() if v <= 2})


# d = {i: i * 5 for i in [10, 20, 30, 40, 50]}
# print(d)
#
# s = "Hello"
# d1 = {i: i * 3 for i in s}
# print(d1)


# lst = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# s = None
#
# for i in lst:
#     if type(i) is str: # type(i) == str
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
#
# print(d)


# zip([], []) объединяет элементы последовательно

# d = dict(zip([1, 2, 3], ["one", "two", "three"]))
# print(d)
#
# d = list(zip([1, 2, 3], ["one", "two", "three"], [True, False, True]))
# print(d)

# a = [1, 2, 3]
# b = ["one", "two", "three"]
# d = {k: v for k, v in zip(a, b)}
# print(d)


# a = [1, 2, 3]
# c = list(zip(a))
# print(c)


# one = {"name": "Igor", "surname": "Pavlov", "job": "Consultant"}
# two = {"name": "Irina", "surname": "Vetrova", "job": "Manager"}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)


# lst = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*lst)
# print(a)
# print(b)


# letter = ['b', 'a', 'd', 'c']
# number = [3, 4, 2, 1]
# d = dict(zip(letter, number))
# print(d)
#
# data = sorted(zip(letter, number))
# print(d)
#
# data = sorted(d.items())
# print(data)


# data1 = list(zip(letter, number))
# print(data1)
# data1.sort()
# print(data1)
#
# d2 = dict(data1)
# print(d2)
#
# data2 = list(zip(number, letter))
# print(data2)
# data2.sort()
# print(data2)
# d3 = {v: k for k, v in data2}
# print(d3)


# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# one = {"один": 1, "два": 2} # объединили 2 словаря в 1
# two = {"три": 3, "четыре": 4}
# print({**one, **two}) # объединили 2 словаря в 1


# colors = ["red", "yellow", "green"] # нумерация текущих элементов
# i = 1
# for color in colors:
#     print(i, ") ", color, sep="")
#     i += 1
# print()
# for j, color in enumerate(colors, 10):
#     print(j, ") ", color, sep="")


# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
#
# for i, (k, v) in enumerate(d.items(), 1):
#     print(i, ") ", k, ": ", v, sep="")


# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(1, 2, 3))
# print(func())


# def summa(*params):
#     # return params
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(7, 8, 9))


# def average(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#
#     res = []
#     for num in args:
#         if num < sr:
#             res.append(num)
#
#     return res
#
#
# print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(average(3, 6, 1, 9, 5))


# def func(a, b, *args):
#     return a, args
#
#
# print(func(5, 6))
# print(func(1,2, 3, 4, 5))


# def scores(student, *score):
#     print("Student Name:", student)
#     for i in score:
#         print(i)
#
#
# scores("Igor", 5, 5, 4, 3, 3, 5)
# scores("Ivan", 4, 3, 3)


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(st="python"))


# def info(**data):
#     for k, v in data.items():
#         print(k, ":", v)
#     print()
#
#
# info(name="Irina", surname="Vetrova", age=22)
# info(name="Igor", phone="47897897654", email="igor@mail.ru", age=22)


# def func1(*args): # кортеж
#     print("args:", args)
#     print(args[0])
#
#
# def func2(**kwargs): # словарь
#     print("kwargs:", kwargs)
#     print(kwargs["one"]) # обращаясь к ключу - получаем значение
#
#
# func1(1, 2, 3, 4, 5, 6)
# func2(one=123, two=456)


# ОБЛАСТИ ВИДИМОСТИ (SCOPE)

# name = "Tom" # глобальная переменная - в глобальной области видимости
#
#
# def hi():
#     # name = "Sam" # локальная переменная - перезапишет переменную выше
#     global name # сделали локальную переменную - глобальной, перезаписывается и дальше уже она
#     name = "Sam"
#     surname = "Jonson" # локальная переменная - область видимости только внутри функции
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
# print(name)
# hi()
# bye()
# # print(surname) - # тут мы ее уже не увидим
# print(name)


# import builtins
#
# name = dir(builtins) # самая глобальная область видимости
#
# for t in name:
#     print(t)


# print = 5
#
# lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(sum(lst))



# x = 4
#
#
# def func():
#     x = 2 # 2 enclosed
#
#     def inner():
#         print("x =", x) # 4
#         print(x + 3) # 5
#
#     inner() # 3
#
# func() # 1 отработает первой





# ВЛОЖЕННЫЕ ФУНКЦИИ

# def outer(a):
#     def inner():
#         print("Hello", a)
#
#     inner()
#
#
# outer("World")



# def fun1():
#     a = 6 # 2
#
#     def fun2(b):
#         a = 4 # 5
#         print("Сумма: ", a + b) # 6
#
#     print("a:", a) # 3
#     fun2(3) # 4
#
#
# fun1() # 1




# x = 25
#
#
# def fn():
#     global t
#     a = 30
#     def inner():
#         nonlocal a # не локальная, перезаписывает значение на уровень выше в функции
#         a = 35
#         print("a =", a)
#
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)





# def fn1():
#     x = 25
#
#     def fn2():
#         # x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x =", x) # 33 -> 55
#
#     fn2()
#     print("fn1.x =", x) # 25
#
#
# fn1()




# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))



# ЗАМЫКАНИЕ одна внешняя функция возвращает внутренню, но ее при этом не вызывает

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
# func1 = outer(5) # вернули вложенную в функцию в переменную func1 и она стала функцией
# print(func1(10))
#
# func2 = outer(6)
# print(func2(10))





# def func1():
#     a = 1
#     b = ("line")
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "!"
#         return a, b, c
#
#     return func2
#
# func = func1()
# print(func())




# def func(city):
#     n = 0
#
#     def inner():
#         nonlocal n
#         n += 1
#         print(city, n)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res1()
# res1()
# res1()
# res2 = func("Сочи")
# res2()
# res2()
# res1()
# res1()
# res2()





# АНОНИМНЫЕ ФУНКЦИИ (lambda-выражения)

# def func(x, y):
#     return x + y
#
#
# print(func(1, 2))
#
# print((lambda x, y: x + y)(1, 2))
#
# # func = lambda x, y: x + y
# #
# # print(func(1, 2))
#
#
# func = (lambda x, y: x + y)(1, 2)
# print(func)




# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a=1, b=2, c=3: a + b + c)())



# print((lambda *args: sum(args))(1, 2, 3, 4))



# tpl = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in tpl:
#     print(t("abc___"))






# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = outer(42)
# print(f(3))
#
#
#
# def outer(n):
#     return lambda x: n + x
#
# f = outer(42)
# print(f(3))
#
#
# outer = lambda n: lambda x: n + x
# f = outer(42)
# print(f(3))
#
#
# print((lambda n: lambda x: n + x)(42)(3))



# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))



# d = {"b": 10, "a": 15, "c": 4}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# print(dict(lst))



# def func(i):
#     return i[1]
#
#
# d = {"b": 10, "a": 15, "c": 4}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=func)
# print(lst)
# print(dict(lst))




# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}
# ]
# res = sorted(players, key=lambda item: item["last name"])
# print(res)
#
# res = sorted(players, key=lambda item: item["rating"], reverse=True)
# print(res)
#
# res = sorted(players, key=lambda item: item["rating"])
# print(res)



# lst = [lambda x, y: x + y,
#        lambda x, y: x - y,
#        lambda x, y: x * y,
#        lambda x, y: x / y
#        ]
# print(lst[0](12, 6))
# print(lst[2](12, 6))




# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье")
#
# }
#
# d[2]()


# print((lambda  a, b: a if a > b else b)(5, 3))
# print((lambda  lst: [i * 2 for i in lst])([1, 2, 3, 4, 5, 6]))



# map(function, iterables), filter(function, iterables)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(mult, lst)))
# print(tuple(map(mult, lst)))
#
# print(list(map(lambda t: t * 2, lst)))




# t = (2.88, -1.75, 100.55)
#
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))
# print(tuple(map(round, t)))
# print(tuple(map(str, t)))




# st = ['a', 'b', 'c', 'd', 'e', 'w']
# num = [1, 2, 3, 4, 5]
# print(dict(map(lambda x, y: (x, y), st, num)))
# print(list(map(lambda x, y: (x, y), st, num)))




# st = ['a', 'b', 'c', 'd', 'e', 'w']
# num = [1, 2, 3, 4, 5]
# tpl = (True, False, False, True, True)
# print(list(map(lambda a, b, c: (a, b, c), st, num, tpl)))
# print(list(map(lambda a, b, c: a + str(b) + str(c), st, num, tpl)))
# print(set(map(lambda a, b, c: (a, b, c), st, num, tpl)))




# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda a, b: a + b, l1, l2)))


# lst = [input("->") for i in range(5)]
# print(lst)
# lst = (list(map(int, lst)))
# print(lst)




# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
#
# print(tuple(filter(lambda s: len(s) == 3, t))) # только true, изменить элементы не может, просто фильтрует
# print(tuple(filter(lambda s: s * 3, t))) # 'abcdabcdabcd' не меняет элемент, а переносит в новую



# lst = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# print(list(filter(lambda s: s > 75, lst)))




# from random import randint
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
# print(list(filter(lambda a: (a >= 10) and a <= 20, lst)))
# print(list(filter(lambda a: 10 <= a <= 20, lst)))



# nums = [45, 55, 60, 37, 100, 105, 220]
# print(list(filter(lambda s: s % 15 == 0, nums)))
# print(list(filter(lambda s: not s % 15, nums)))



# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10)))))
#
# print([x ** 2 for x in range(10) if x % 2])



# ДЕКОРАТОРЫ

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello) # функция передается как параметр функции


# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())





# def my_decorator(func):
#     def func_wrapper():
#         print("Код до функции")
#         func()
#         print("Код после функции")
#
#     return func_wrapper


# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()




# def my_decorator(func): # декорирующая функция
#     def func_wrapper():
#         print("Код до функции")
#         func()
#         print("Код после функции")
#
#     return func_wrapper
#
# @my_decorator  # декоратор
# def func_test(): # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# func_test()



# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())




# def cnt(fn):
#     count = 0
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()



# def outer(fn):
#     def inner(args1, args2):
#         print("Данные:", args1, args2)
#         fn(args1, args2)
#
#
#     return inner
#
# @outer
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Ветрова")




# def outer(fn):
#     def inner(*args, **kwargs):
#         print("args:", args)
#         print("kwargs", kwargs)
#         fn(*args, **kwargs)
#
#
#     return inner
#
# @outer
# def print_data(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, end="\n\n")
#
#
# print_data("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_data("Владимир", "Екатерина", "Виктор")




# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)



# def multiply(arg): # в arg приходит 3 из декоратора
#     def my_decorator(func): # в func приходит return_num
#         def wrap(*args, **kwargs): # в wrap приходит 5 - то что передаем в return_num
#             return arg * func(*args, **kwargs)
#         return wrap
#     return my_decorator
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
# print("Результат:", return_num(5))




# СТРОКИ

# print(bin(18))  # 0b10010 - двоичная система счисления
# print(oct(18))  # 0o22 - восьмеричная система счисления
# print(hex(18))  # 0x12 - шестнадцатеричная система счисления
# print(0b10010)
# print(0o22)
# print(0x12 + 0b10010 + 4)

# Unicode



# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# print(e * 3)
# print("y" in e)
# print("a" in e)
# print(e[-1])
# print(e[1:3])



# def chang_char_to_str(s, old, new):
#     s2 = ""
#
#     i = 0
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#
#         i += 1
#
#     return s2
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# str2 = chang_char_to_str(str1, "N", "P")
# print(str1)
# print(str2)





# префиксы перед строкой
# print("Привет")
# print(u"Привет")


# print("C:\\file.txt")
# print(r"C:\file.txt\\"[:-1])
# print(r"C:\file.txt" + "\\")



# def avg(fn):
#     def wrap(*args):
#         st = ""
#         for i in args:
#             st += str(i) + ", "
#         print("Среднее арифметическое:", st[:-2], "=", fn(*args) / len(args))
#
#     return wrap
#
#
# @avg
# def summa(*args):
#     st = ", ".join(map(str, args))
#     print("Сумма чисел:", st, "=", sum(args))
#     return sum(args)
#
#
# summa(2, 3, 3, 4)


# print(b"a1b2c2")


# name = "Дмитрий"
# age = 25
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")


# x = 10
# y = 5
# print(f"{x=}, {y=}")
# print("x=", x, ", y=", y, sep="")
#
# print(f"{x} x {y} / 7 = {round(x * y / 7, 2)}")
# print(f"{x} x {y} / 7 = {x * y / 7:.3f}")

# num = 74
# print(f"{{{{{num}}}}}")

# dir_name = "folder"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)


# st = ("Однострочный "
#       "текст")
# print(st)
#
# s = """Многострочный
# текст
# """
# print(s)
#
# s1 = '''Многострочный
# текст
# '''
# print(s1)
#
#
# """Многострочный комментарий
# текст
# """
#
# "Однострочный комментарий"


# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     res = n ** 2
#     return res
#
#
# print(square(5))
# print(square.__doc__)
# print(len.__doc__)
# print(min.__doc__)
# print(max.__doc__)
# print(sum.__doc__)


# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)


# print(ord('a'))
# print(ord('#'))
# print(ord('п'))

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# st = "Test string for me"
# arr = [ord(x) for x in st]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))
# print(chr(1057))

# a = 97
# b = 122
#
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")


# from random import randint
#
# SHORTEST = 6
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(SHORTEST, LONGEST)
#     result = ""
#     for i in range(rand_len):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
#
# print("Случайный пароль:", random_password())

# print(dir(str))

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
#
# s = "hello, WORLD! I am learning Python."
# print(s.count("h", 1, -4))
# # print(s.lower().count("i"))
#
# print(s.find("Python"))
# print(s.find("h", 1, -4))
# print(s.find("h"))
# print(s.rfind("h"))
#
# print(s.index("h", 1, -4))
# print(s.rindex("h"))

# st = "один два"
# # st = input("-> ")
# one = st[:st.find(" ")]  # st[:4]
# two = st[st.find(" ") + 1:]  # st[4:]
# res = two + " " + one
# print(res)

# st = "один два"
# print(st[st.find(" ") + 1:] + " " + st[:st.find(" ")])

# s = "hello, WORLD! I am learning Python."
# print(s.startswith("hello"))
# print(s.startswith("I am", 14))
# print(s.find("I am"))
#
# print(s.endswith("Python."))


# print("abc123".isalnum())  # состоит ли строка из букв и цифр
# print("abc!123".isalnum())
# print("abc".isalnum())
# print("123№".isalnum())

# print("ABCabcП".isalpha())  # состоит ли строка из букв
# print("ABC%abc".isalpha())

# print("123".isdigit())  # # состоит ли строка из цифр
# print("123@".isdigit())


# print('aab'.islower())  # находятся ли в строке буквы в нижнем регистре, допускается наличие других символов
# print('123aab!№;'.islower())
#
# print("ABC".isupper())  # находятся ли в строке буквы в верхнем регистре, допускается наличие других символов
# print("123AвBC!!".isupper())

# print("py".center(10))
# print("py".center(10, "-"))
# print("py".center(1))


# print("    py".lstrip())
# print("py    ".rstrip())
# print("    py    ".strip())
#
# print("https://www.python.org".lstrip("/:htps"))
# print("https://www.python.org.www".lstrip("/:htps").rstrip(".w"))
# print("https://www.python.org.www".strip("/:htps.w"))


# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(str1.replace("Nython", "Python", 2))


# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '99']))
#
# print(":".join("Hello"))


# s = "Hello"
# print(s[::-1])



# # s = "I am learning Python. hello, WORLD!"
# s = input("Введите строку: ")
# # print(s.rfind('h') + 1)
# a = s[:s.find('h')]  # s[:17]
# b = s[s.find('h'):s.rfind('h') + 1]  # s[17:23]  # hon. h
# c = s[s.rfind('h') + 1:]  # s[23:]
# print(a + b[::-1] + c)


# print("Строка разделенная пробелами".split()) # список из строки
# print("www.python.org.ru".split(".", 2))


# s = input("Введите ФИО: ").split()
# print(s)
# print(f"{s[0]} {s[1][0]}. {s[2][0]}.")


# s = input("Введите числа через пробел: ").split()
# print(s)
# num = list(map(int, s))
# print(num)
# print(sum(num))






# РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ

import re


# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel_lo] Wor-ld 200000000000000"
# # print(dir(re))
# reg = "\\."
# reg = r"\."
# print(re.findall(reg, s))  # возвращает список совпадений с шаблоном
# print(re.search(reg, s))  # возвращает только первое совпадение с шаблоном
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# print(re.split(reg, s))  # возвращает список, который разбит по заданному шаблону
# print(re.sub(reg, "!", s))  # поиск и замена

# reg = r"[205]"
# reg = r"[0-9]"
# reg = r"[12][0-9][0-9][0-9]"
# reg = r"[а-яА-Я]"
# reg = r"[А-яЁё.\]\[-]"
# reg = r"[A-Za-z]"
# reg = r"[^0-9]"
# print(re.findall(reg, s))

# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15T19:49. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg, st))


# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel_lo] Wor-ld 200000000000000"
# reg = r"\d"  # [0-9]
# reg = r"\D"  # [^0-9]
# reg = r"\s"  # [ ]
# reg = r"\S"  # [^ ]
# reg = r"\w"  # [А-яA-Za-z0-9_]
# reg = r"\W"  # [^А-яA-Za-z0-9_]
# reg = r"\AЯ ищу"
# reg = r"Wor-ld\Z"
# reg = r"\Bния"
# reg = r"\w+"
# reg = r"20*"
# print(re.findall(reg, s))

# Кол-во повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1 повторения

# d = "Цифры: 7, +17, --42, 0013, 0.3"
# reg = r"[+-]?[\d.]+"
# print(re.findall(reg, d))

# st = "05-03-1987 # Дата рождения"
#
# print("Дата рождения:", re.sub(r"\s#.+", "", st))
# print(re.sub("-", ".", st))
#
# print("Дата рождения:", re.sub(r"\s#.+", "", re.sub("-", ".", st)))

# st = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
# # reg = r"\w+\s*=\s*\w+\s*\w*\.?\w*\.?"
# # reg = r"\w+\s*=\s*\w+[\s\w.]*"
# reg = r"\w+\s*=[^;]+"
# print(re.findall(reg, st))
# print(re.split(r";\s", st))


# st = "12 сентября 2025 год 456 789456123"
# # reg = r"\d{4}"
# # reg = r"\d{2,4}"
# reg = r"\d{,4}"
# # reg = r"\d{4,}"
# print(re.findall(reg, st))


# st = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, st))


# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel_lo] Wor-ld 200000000000000"
# reg = r"^\w+\s\w+"
# reg = r"\w+\s\w+$"
# print(re.findall(reg, s))

# def validate_login(login):
#     return re.findall(r"^[a-zA-Z0-9_-]{3,16}$", login)
#
#
# print(validate_login("Python_master"))
# print(validate_login("Pyt"))




# import re
# from tkinter.font import names
#
# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))
#
# text = "hello world"
# print(re.findall(r"\w\+", text))
# print(re.findall(r"\w\+", text, re.DEBUG))

# text = "helLo worLd"
# print(re.findall(r"l", text, re.IGNORECASE))


# text = """
# one
# two
# """

# print(re.findall(r"one.\w+", text))
# print(re.findall(r"one.\w+", text, re.DOTALL))

# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))

# print(re.findall("""
# [a-z.-]+  # part 1
# @         # @
# [a-z.]+   # part 2
# """, "test@mail.ru", re.VERBOSE))

# text = """Python,
# python,
# PYTHON
# """
# reg = "(?mi)^python"
# print(re.findall(reg, text))


# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))
#
#
# st = "12 сентября 2025 год 456 789456123"
# # reg = r"\d{4}"
# # reg = r"\d{2,4}?"
# # reg = r"\d{,4}?"
# reg = r"\d{4,}?"
# print(re.findall(reg, st))

# *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий|Василий"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0f, double = 8.0, int"
# # reg = r"int\s*=\s*\d[\w.]*|float\s*=\s*\d[\w.]*"
# reg = r"(?:int|float)\s*=\s*\d[\w.]*"
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5"
# reg = r"([a-z]+)(\d+)"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE))

# s = "5 + 7*2 - 4"
# reg = r"\s*[+*-]\s*"
# print(re.split(reg, s))
#
# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))


# s = "18-01-2021"  # 1900-2099
# reg = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# print(re.findall(reg, s))
# print(re.search(reg, s))
# print(re.search(reg, s).group())


# s = "Word2016, PS6, AI5"
# reg = r"([a-z]+)(\d+)"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE).group())
# m = re.search(reg, s, re.IGNORECASE)
# print(m[1])
# print(m[2])
# print(m[0])

# s = "Самолет прилетает 10/23/2025. Будет рады вас видеть после 10/24/2025."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "yandex.com and yandex.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))


# Рекурсия

# def elevator(n):  # 0
#     if n == 0:  # базовый случай
#         print("Вы в подвале")
#         return
#     # print("=>", n)
#     elevator(n - 1)  # стек 5 4 3 2 1
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
# def sum_list(lst):  # [9]
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25


# def to_str(n, base):  # n = 15, base = 16
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # 'F' + 'E'
#
#
# print(to_str(254, 16))

# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
# print(names)
# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))


# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
#
#
# def count_items(item_list):  # ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
#     count = 0  # 10
#     for item in item_list:  #
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


print("Текст в локальном репозитории")