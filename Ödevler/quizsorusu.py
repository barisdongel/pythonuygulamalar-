dizi = []

a = int(input("Birinci sayıyı giriniz:"))
b = int(input("İkinci sayıyı giriniz:"))
c = int(input("Üçüncü sayıyı giriniz:"))

dizi.append(a)
dizi.append(b)
dizi.append(c)

dizi.sort()
print("En büyük sayıdan ortanca sayının farkı:", dizi[2]-dizi[1])