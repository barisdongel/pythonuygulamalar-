# python da küme (set kavramı)

kume = {2, 3, 5, 6, 9}  # kümeler { tanımlar
print(kume)

A = {"ali", "ayşe", "ahmet", "ali", "cengiz"}  # bir küme de bir elemean yalnızca 1 defa olur.
print(A)

B = {"ali", "betül", "deniz", "elif", "ahmet"}
print(B)

# A'dan B kümesini çıkartacak. (.differance(değişken)) şeklinde de kullanılabilir
print(A - B)

# Toplama (.union(değişken)) toplama işlemi yapar
print(A.union(B))

dizi = [2,3,3,5,5,5,6,7,8,8,9,9]
k=set(dizi)
print(k)

#kümeyi diziye çevirmek.
C = {"ali","ayşe","betül","cengiz"}
D = list(C)
print(D)

stringDizisi = ["Konya'yı çok seviyorum"]
stringSet = set(stringDizisi)
print(stringSet)

#stringedeki tekrar eden harfleri kaldırmak
print(set("Konya'yı çok seviyorum"))