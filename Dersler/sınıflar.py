class ogrenci:
    ad = ""
    soyad = ""
    numara = 0
    vize = 0
    final = 0

    # fonksiyondan yazdırma
    def yazdir(self):
        print(self.ad,"-",self.soyad)

    def ortalama(self,vize,final):
        return vize*0.4+final*0.6

nesne = ogrenci()
nesne.ad = " Barış"
nesne.soyad = "Döngel"
nesne.numara = "19410051042"
nesne.vize = 85
nesne.final = 65

print(" Ad:",nesne.ad,"\n","Soyad:",nesne.soyad)
nesne.yazdir()
print("Ortalama =",nesne.ortalama(nesne.vize,nesne.final))

nesne2 = ogrenci()
nesne2.ad = "Cem"
nesne2.soyad = "Bağış"
nesne2.vize = 78
nesne2.final = 69
nesne2.yazdir()

if nesne.ortalama(nesne.vize,nesne.final)>nesne2.ortalama(nesne2.vize,nesne2.final):
    print(nesne.ad,"Ortalaması daha iyi")
else:
    print(nesne2.ad,"Ortalaması daha iyi")

