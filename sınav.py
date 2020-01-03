#ilk soru (kullanıcıdan 2 tane sayı alıp büyük olan sayı tek ise 1 ekleyip 2 ye bölen çift ise 2 ye bölen program)
dizi = []
x = int(input("1.sayı"))
y = int(input("2.sayı"))

x = dizi.append(x)
y = dizi.append(y)
dizi.sort()

if dizi[1]%2==0:
    a = dizi[1]/2
    print(a)
else:
    b = dizi[1]+1
    print(b/2)

#son soru
import random
dizi = []
for i in range(20):
    dizi.append(random.randint(0,100))
matris = [[0 for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        matris[i][j] = dizi[random.randint(0,19)]
print(matris)

