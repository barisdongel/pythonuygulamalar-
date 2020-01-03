dizi = ["ahmet", "ayşe", "ali", "beril", "cihan", "deniz", "elif"]

print(dizi[0]) #Ahmet yazar
print(dizi[6]) #Elif yazar
print(dizi[len(dizi)-3]) #len dizi dizide ki eleman sayısını bulur o da 7 ye denk gelir -3 den sonra 4 kalır yani dizinin 4.elemanı cihanı yazdırır.
print(dizi[3][4])#dizinin 3. elemanının 4.elemanı olan l harfi
print(dizi[3],"-",dizi[len(dizi[0])]) #dizi 0'ın eleman sayısı 5. dizinin 3. elemanı ile 5. elemanını yazdırır.
print(dizi*2) #diziyi yan yana 2 defa yazdırır
print(dizi[dizi.count("beril")]) #dizide berilin kaç defa olduğuna bakar. cevap 1 sonra dizi [1] çalışır ve "ayşe" yazdırır
print(dizi.remove("ahmet"),dizi) #ahmeti diziden silip tekrar diziyi yazdırır