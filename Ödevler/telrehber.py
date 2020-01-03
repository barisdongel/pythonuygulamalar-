"""
______________________________________________
|                                            |
|    Öğrenci Ad:    Barış Ömer Döngel        |
|    Öğrenci No:    19410051042              |
|                                            |
|____________________________________________|
"""

while True:#programımızın sürekli devam etmesi için bir döngü açtık
    print("_" * 40)
    secim = int(input("Yapılacak işlemi seciniz:\n 1)Rehberi gör\n 2)Rehbere Ekle\n 3)Kişi sil"))
    if secim == 1:
        dosya = open("rehber.txt", mode='r', encoding='utf-8') #dosyamızı okuma modunda oluşturduk
        print("_"*40)
        print(dosya.read())#dosyamızı okuyup ekrana yazdırdık
        print("_"*40)
        dosya.close()

    elif secim == 2:
        dosya = open("rehber.txt", mode='a', encoding='utf-8')#dosyamızı ekleme modunda oluşturduk
        yenikisisim = input("Eklemek istediğiniz kişinin ismi?:")
        yenikisino = input("Numarası?:")
        s = str(yenikisisim)#stringe dönüştürdük
        n = int(yenikisino)#integer'a dönüştürdük
        dosya.write(s+" :")#kişinin ismini ekledik
        dosya.write(str(n) + "\n")#kişinin numarasını ekledik
        print("Başarıyla eklendi")
    #bu kısmı büyük ölçüde stackoverflow'dan bakarak yaptım mantığını anladım ama açıklayamadım hocam :(
    elif secim == 3:
        with open("rehber.txt", "r+", encoding='utf-8') as f:
            new_f = f.readlines() #dosya içinde ki verileri satır satır açıyo ve değere atıyo
            f.seek(0)
            a = input("Silmek istediğiniz kullanıcının adını giriniz:")
            for line in new_f:#değer sayısı kadar bir döngü açıp line diye bir değişkene atıyor.
                if a not in line:#eğer silmek istediğimiz kullanıcı line da yoksa
                    f.write(line)#:((
            f.truncate()#:(((
    else:
        print("Hatalı seçim girdiniz. Lütfen yanda belirtilen numaraya göre seçiminizi yapınız.")

