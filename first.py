# Дано натуральное число N. Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.

# 60 -> 2, 2, 3, 5

a = int(input("Введите целое число больше 0:   "))
b = a
list = []
count = 2
while a > 1:
    if a % count == 0:
        list.append(count)
        a = a/count
    else:
        simple += 1
print(f'{b} - > {list}')