#miras alma, kalıtım

class hayvanlar():
    htur = ""
    hcografya = ""

class kus(hayvanlar):
    kanat_uzunlugu = 0
    agirlik = 0

class avcı(kus):
    tur = ""

nesne = avcı()
nesne.htur = "KUŞ"
nesne.hcografya = "ABD"
nesne.tur = "Kartal"
nesne.agirlik = 50
nesne.kanat_uzunlugu = 1

def oku():
    print("*"*30)
    print("Hayvan türü: ",nesne.htur)
    print("Kuş türü: ",nesne.tur)
    print("Ağırlığı: ",nesne.agirlik)
    print("Coğrafyası: ",nesne.hcografya)
    print("Kanat uzunluğu: ",nesne.kanat_uzunlugu)
    print("*"*30)
oku()