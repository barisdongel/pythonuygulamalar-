# Sıfır ve 1000 arasındaki Fibonacci sayılarını bulan ve bir diziye aktaran program

#Barış Ömer Döngel
#19410051042

#3 tane değişken oluşturup 2 sini 1 den 1 tanesini 0 dan başlattık
a = 1
b = 1
c = 0

dizi = [] #boş dizi

while c < 1000: # c 1000 den küçük olana kadar devam etsin
    c = a+b # c = 1+1 c = 2
    a = b # 1 = 1
    b = c # (b)  1 = 2 (c) ve / (a) 2 = (b) 1+1 (c) / (a) 3 = (b) 1+2 (c) / (a) 5 = (b) 2+3 (c) / (a) 8 = (b) 3+5 (c)  şeklinde devam eden bir algoritma kurduk.
    dizi.append(a) #a değişkenini diziye attık çünkü toplamı en sonunda a ya atıyoruz. BKZ:15.satır

print(dizi) #diziyi ekrana yaz


#NOT : Neden teker teker bulup diziye teker teker atadığı algoritma ile ilgili aslında. Daha sağlam bi algoritma kuramadığım için böyle oldu :(