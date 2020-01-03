"""
#sorgusuz hali
x = int(input("Hangi yılda doğdunuz ?"))
print(2019-x," Yaşınızdasınız")

y = int(input("Kaç yaşındasın"))
print(2019-y," Yılında doğdun")
"""
#sorgulu hali
tarih = 2019
def yashesapla():
    x = int(input("Hangi yılda doğdunuz ?"))
    if x >= tarih or x < 0 :
        print("Mantıksal olarak hatalı bir değer girdiniz. Lütfen şimdiki tarihden düşük bir tarih giriniz ve negatif değer girmeyiniz.")
        yashesapla()
    elif x <= 1900:
        print(tarih-x," Yaşındasın. Biraz yaşlıymışsın")
    else:
        print(tarih-x," Yaşındasın.")
yashesapla()