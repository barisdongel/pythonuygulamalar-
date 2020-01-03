import random
s = input("İsminizi küçük harfle giriniz:")
u = len(s)
rs = ""
sayac = 0

while True:
    for i in range(u):
        rs += chr(random.randint(97,122))
    print("deneme",sayac)
    print(rs+"\n")
    sayac+=1
    if rs==s:
        print("bulundu")
        break
    else:
        rs = ""