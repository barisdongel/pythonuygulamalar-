import random
print("Sayısal loto:")
loto = []
for i in range(6):
    x = random.randint(1,49)
    loto.append(x)
    if loto.count(x) > 1:
        loto.remove(x)
        loto.append(random.randint(1,49))
print(loto)

#2. yol
print("İkinci yoldan çözümü")

liste = [i for i in range(1,50)]
random.shuffle(liste)
print(liste[43:])