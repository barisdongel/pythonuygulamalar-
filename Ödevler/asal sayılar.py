#Python Asal Sayıları Bulma Diziye aktarma

#Barış Ömer Döngel
#19410051042

asal = [] #asal adında boş dizi

#asal sayıları bulan algoritmay
for sayi in range(2 , 1000 + 1):
        for i in range(2, sayi):
            if (sayi % i) == 0: # eğer sayı i ye bölündüğünde sıfır ise sayi değişkenine alma "break" bırak.
                break
        else:#değilse
            asal.append(sayi) #bu sayıları asal dizisine at
print(asal)#asal dizisini yazdır
