#recursive (özyinelemeli) fonksiyon
#fonksiyonun kendi kendini çağırması

"""def faktoriyel(n):
    if n == 1 or n == 0:
        return 1
    elif n<0:
        print("Pozitif değer giriniz.")
    else:
        return n * faktoriyel(n-1)

a = int(input("Faktöriyelini almak istediğiniz sayı ?:"))

print(faktoriyel(a))
"""
import random
#bir dizide bulunuan elemanlarıon toplamını recursive fonksiyon ile gerçekleştirinizi
liste = [random.randint(0,15) for i in range(random.randint(1,15))]
def topla(liste):
    if len(liste)==1:
        return liste[0]
    else:
        return liste[0] + topla(liste[1:])

print(liste)
print(topla(liste))