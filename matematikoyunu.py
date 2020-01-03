import random
import time

skor = 0

def kontrol():
    if skor == -10:
        print("GAME OVER !!!")
        print("Yeni oyun 10 saniye sonra başlayacak...")
        time.sleep(10)
    if skor == 20:
        print("TEBRİKLER. OYUNU BİTİRDİN")
        print("Yeni oyun 10 saniye sonra başlayacak...")
        time.sleep(10)


def oyun():
    ilksayi = random.randint(1, 50)
    ikincisayi = random.randint(1, 50)
    a = random.randint(1, 3)
    global skor
    if a==1:
        topla = ilksayi+ikincisayi
        print("Toplama işlemi ->")
        print("Lütfen",ilksayi," ile",ikincisayi," nın toplamını yazınız.")
        cevap = int(input())
        if cevap == topla:
            print("Tebrikler doğru bildiniz.")
            time.sleep(1)
            skor = skor + 1
            print("Skorunuz :",skor)
            kontrol()
            oyun()
        else:
            print("Bilemediniz. Doğru cevap:",topla)
            time.sleep(1)
            skor = skor -1
            print("Skorunuz :", skor)
            kontrol()
            oyun()
    if a==2:
        cikar = ilksayi - ikincisayi
        print("Çıkarma işlemi ->")
        print("Lütfen",ilksayi," ile",ikincisayi," nın farkını yazınız.")
        cevap2 = int(input())
        if cevap2 == cikar:
            print("Tebrikler doğru bildiniz.")
            time.sleep(1)
            skor = skor + 1
            print("Skorunuz :",skor)
            kontrol()
            oyun()
        else:
            print("Bilemediniz. Doğru cevap:", cikar)
            time.sleep(1)
            skor = skor - 1
            print("Skorunuz :", skor)
            kontrol()
            oyun()
    if a==3:
        carp = ilksayi * ikincisayi
        print("Çarpma işlemi ->")
        print("Lütfen",ilksayi," ile",ikincisayi," nın çarpmımını yazınız.")
        cevap3 = int(input())
        if cevap3 == carp:
            print("Tebrikler doğru bildiniz.")
            time.sleep(1)
            skor = skor + 1
            print("Skorunuz :",skor)
            kontrol()
            oyun()
        else:
            print("Bilemediniz. Doğru cevap:", carp)
            time.sleep(1)
            skor = skor - 1
            print("Skorunuz :",skor)
            kontrol()
            oyun()
oyun()