from functools import reduce

a = [5, 13, 3, 7, 18, 19, 21, 45, 67, 34, 43, 73]

liste = list(map(lambda x:(x*2-1),a))
liste2 = list(filter(lambda x:x%3==0 or x%6==0,a))
liste3 = list(filter(lambda x:x<20,a))
liste4 = list(map(lambda x:x+5,liste3))
liste5 = reduce(lambda x,y:(x*y),a)

print("Tüm dizi elemanlarının 2 katının bir eksiği.")
print(liste)

print("3'e ve 6'ya tam bölünenler")
print(liste2)

print("20'den küçük olanlara 5 ekle")
print(liste4)

print(liste5/10)