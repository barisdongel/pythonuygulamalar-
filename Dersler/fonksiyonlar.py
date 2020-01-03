#fonksiyonların temel amacı kod tekrarını önlemek
dizi = []
def berrin():
    for i in range(3):
        x = int(input("20'den küçük sayı giriniz:"))
        if  x <= 20:
            dizi.append(x)
        else:
            print("20 Den büyük bir değer giriniz")
    print(dizi)
#yukarıdaki fonksiyon değer almıyor değer döndürmüyor
berrin()
"""
#değer alan fonksiyon
def merhaba(isim):
    print("Merhaba",isim)
merhaba("Barış")

#değer alan ve döndüren fonksiyon

def carpim(a,b):
    return a*b #döndürülecek değer return ile girilir.
c = carpim(5,6)
print(c)
print(carpim(7,7))"""