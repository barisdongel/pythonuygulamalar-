#python da dictionary kullanımı
#bir küme içindeki verilerin değerleri karşılıklı tutulabilir

# (:)'nın sağında ki veriyi verir.

dict = {1:"bir",2:"iki",3:"üç",4:"dört",5:"beş"}
print(dict[1])

dict = {"ayşe":54, "ali":45}
print(dict["ali"])

#kullanıcıdan alınan sayıyı yazı ile yazmak
while True:
    sayi = int(input("Üç basamaklı bir sayı giriniz:"))
    if (sayi>99 and sayi<1000):
        break
    else:
        print("Lütfen 3 basamaklı bir sayı girin!")

s = str(sayi)#sayıyı rahat parçalamak için stringe çevirdik
yuzler = int(s[0])#basamak değerini alıyoruz
onlar = int(s[1])
birler = int(s[2])

ydict = {1:"yüz",2:"ikiyüz",3:"üçyüz",4:"dörtyüz",5:"beşyüz",6:"altıyüz",7:"yediyüz",8:"sekizyüz",9:"dokuzyüz"}
odict = {1:"on",2:"yirmi",3:"otuz",4:"kırk",5:"elli",6:"altmış",7:"yetmiş",8:"seksan",9:"doksan",0:""}
bdict = {1:"bir",2:"iki",3:"üç",4:"dört",5:"beş",6:"altı",7:"yedi",8:"sekiz",9:"dokuz",0:""}

print(ydict[yuzler],odict[onlar],bdict[birler])