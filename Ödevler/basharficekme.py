#19410051042
#Barış Ömer Döngel

#normal çözüm
arananharf = "a","A" #aradığımız harfleri belirttiğimiz sınıf
liste = ["ali","veli","hüseyin","ahmet","deniz","cenk","Lale","Ayşe"] #liste
dizi = [] #boş dizi

for ilk in liste: #döngü açıp...
    if ilk.startswith(arananharf): #eğer arananharf listede ki kelimelerin ilk harferlinde var ise (bunu startswith ile yaptık.)
        dizi.append(ilk) #diziye aktarıyoruz

print(dizi)# diziyi yazdır.

#lambda ile çözümü
liste = ["ali","veli","hüseyin","ahmet","deniz","cenk","Lale","Ayşe"]
yeniliste = list(filter(lambda x : x[0] == "a" or x[0] == "A", liste))
print(yeniliste) #yenilisteyi yazdır


