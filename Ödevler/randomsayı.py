#0 ile 100 arasında 1000 adet random sayı üretip diziye aktarma ve içinden yediye bölünenlerin toplamını ve ortalamasını bulan program.

#Barış Ömer Döngel
#19410051042

import random #random işlevini projemize ekledik

yt = 0 #7'ye bölünenlerin toplamı ve sayısı şeklinde 2 değişken açıp 0'a eşitledik
ys = 0

dizi = [] # boş bir dizi oluşturduk

for i in range(0,1000): #range aralığını 0 ile 1000 yaptık ki 1000 tane random sayı üretsin
    a = random.randint(0,100) #0 ile 100 arasında random sayılar ürettik ve "a" diye bir değişkene atadık
    dizi.append(a) # "a" değişkenini diziye '.append' komutu ile ekledik

print(dizi) #diziyi yazdırarak 1000 tane 0 ile 100 arasında random sayıyı gördük

for i in dizi: #diziyi for döngüsüne sokup...
    if i%7==0: #dizi içinde ki sayılardan 7 ye bölünenleri bulduk.
        yt += i #7'ye bölünenlerin toplamını bulmak için her bölünen sayıyı topladık.
        ys += 1 #7'ye bölünenlerin sayısını her seferinde 1 arttırarak sayıyı bulduk (ortalama bulurken kullanıcaz)

#ekrana yazdırma işlemleri felan
print("Yediye bölünen",ys,"adet sayı vardır")
print("Yediye bölünen toplamı =",yt)
print("Ortalama = ",yt/ys)