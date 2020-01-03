#lambda fonksiyonlar

ikikat = lambda x:x*2

c = ikikat(8)
print(c)

#listeden tek sayıları filtrelemek
liste =[1,2,3,4,5,6,7,8,9,0]

yeni_liste = list(filter(lambda x:(x%2==1),liste))
print(yeni_liste)

#map ile verileri güncellemek
yeni_liste2 = list(map(lambda x:(x+3),liste))

print(yeni_liste2)

#reduce kullanımı
#reduce python 3+ ile functools modülüne aktarılması
from functools import reduce
toplam = reduce(lambda x,y:(x+y),liste)
print(toplam)