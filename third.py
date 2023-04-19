# Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
# 3 -> 3.142

def findlength(b):
    count = 0
    while b < 1:
        b = b * 10
        count += 1
    return(count)


a = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862
b = float(input("Введите число или дробь"))
if b >= 1:
    print(round(a, int(b)))
elif b == 0:
    print("Введите число, отличное от нуля")
elif b < 1:
    b = int(findlength(b))
    print(round(a, b))
