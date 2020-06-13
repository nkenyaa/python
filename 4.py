n = int(input("Введите число: "))
i = []
while n>10:
    i.append(n%10)
    n//=10
m = max(i)
print(m)