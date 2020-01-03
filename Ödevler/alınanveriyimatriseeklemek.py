dizi = []
sayi = 0

for i in range(9):
    sayi = int(input("Bir sayı:"))
    dizi.append(sayi)

dizi.sort()
matris=[[0 for i in range(3)] for j in range(3)]

for i in range(3):
    matris[0][i]=dizi[i]
    matris[1][i]=dizi[i+3]
    matris[2][i]=dizi[i+6]

print(matris)