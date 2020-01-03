#kapsulleme

class siparis():
    def __init__(self):
        self.__fiyat = 700

    def fiyatYaz(self):
        print(self.__fiyat)

    def setfiyat(self,fiyat):
        self.__fiyat = fiyat

    def getfiyat(self):
        return self.__fiyat

nesne = siparis()
nesne.fiyatYaz()

nesne.setfiyat(1000) #fiyatı değiştiriyoruz
nesne.fiyatYaz()
print(nesne.getfiyat())