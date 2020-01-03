isim = ["ali","ayşe","fatma","hasan"] #string dizileri
vize = [65,25,45,35]

print(isim)
print(vize)
print(isim[2])
print(isim[2:4])
print(vize[0])

#dizi uzunluğunu nasıl buluruz

dizi = [21,44,36,33,67,89,90,12]
print(len(dizi))

#dizi ortalaması almak

toplam = 0
ortalama = 0
for i in dizi:
    toplam += i

ortalama = toplam / len(dizi)
print("Toplam:",toplam)
print("Ortalama:",ortalama)

#diziye eleman ekleme

kuşlar = [] #boş dizi

#append komutu ile eleman ekliyoruz

kuşlar.append("kanarya")
kuşlar.append("kartal")
kuşlar.append("baykuş")
print(kuşlar)

#insert komutu (elemanı sıraya ekleme)

kuşlar.insert(0,"Serçe")
print(kuşlar)

#insert ile 2. elemanın yerine eleman ekledik. diğer elemanlar 1 sıra kaydı
kuşlar.insert(2,"Güvercin")
print(kuşlar)

#diziden eleman silmek
kuşlar.remove("Güvercin") #remove komutu ile güvercin stringini sildik
print(kuşlar)

#index numarasına göre eleman silmek
del kuşlar[2]
print(kuşlar)

#diziyi sıralama işlemi
sayilar = [23,54,2,647,84,3,18,79]
sayilar.sort()
print(sayilar)

#diziyi büyükten küçüğe sıralama
sayilar.reverse()
print(sayilar)

#ismimizi tersten yazma
isim = ["b","a","r","ı","ş"]
isim.reverse()
print(isim)

#stringi yukardan aşşağı yazmak
yazi = "Eskişehir'i çok seviyorum"
for i in yazi:
    print(i)

print()

#dizi elemanı saymak
model = [1999,2001,1999,2005,2008,1999,2000]
print(model.count(1999))