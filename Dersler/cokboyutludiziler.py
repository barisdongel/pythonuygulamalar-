#Çok Boyutlu Diziler (Matrisler)
#dizi = [[],[],[]]

matris = [[0,1,2],[3,4,5],[6,7,8]]
a = [["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"],["Mat","Mat","Fen","Fen","Bed","Bed","Müzik"],[],[],[],[]]
for i in range(7):
    print(a[i])
# 0 1 2
# 3 4 5
# 6 7 8

print(matris[0][0])
print(matris[1][1])

print()

#matris'i alt alta yazdırma işlemi
"""for i in range(3):
    for j in range(3):
        print(matris[i][j])

print()"""

#matris'i matris şeklinde 3b yazdırmak
for i in range(3):
        print(matris[i])

print()