#Kullanıcının istediği boyutlarda rastgele sayılardan oluşan iki matrisi toplayalım.

import random

satir = int(input("Satır sayısı ?:"))
sutun = int(input("Sütun sayısı ?:"))

    #matrisin ilk değerini 0 ile doldurma
m1 = [[0 for i in range(sutun)] for j in range(satir)]
m2 = [[0 for i in range(sutun)] for j in range(satir)]
toplam = [[0 for i in range(sutun)] for j in range(satir)]

print(m1,"\n")

for i in range(satir):
    for j in range(sutun):
        m1[i][j] = random.randint(0,5)
        m2[i][j] = random.randint(0,5)

#m1 yazdırıyo
for i in range(satir):
    print(m1[i])

print()

for i in range(satir):
    print(m2[i])


print()
#matrisleri toplama

for i in range(satir):
    for j in range(sutun):
        toplam[i][j] = m1[i][j] + m2[i][j]

for i in range(satir):
    print(toplam[i])