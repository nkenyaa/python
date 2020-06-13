q = float(input("Введите свой результат: "))
c = float(input("Введите свою цель: "))
d = 0
while q<c:
    q *= 1.1
    d += 1
print(d)