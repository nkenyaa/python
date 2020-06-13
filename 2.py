sec = int(input("Укажите время в секундах: "))
a = sec//3600
sec %= 3600
b = sec//60
sec %= 60
print("%d:%d:%d" % (a,b,sec))