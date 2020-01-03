#yapıcı fonksiyon

class dortgen():
    en = 0
    boy = 0

    def __init__(self): #constructer method. Default olarak kullanıcı girmemiş olsa bile değişkenlere değer verir.
        self.en = 10
        self.boy = 20

    def cevre(self,en,boy):
        return 2*en+2*boy

nesne = dortgen()
print(nesne.boy,nesne.en)
print(nesne.cevre(8,10))