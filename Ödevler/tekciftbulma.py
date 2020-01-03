tt= 0
ts= 0
ct= 0
cs= 0

for i in range(500,10000):
    if i % 2==0:
        ct += i
        cs += 1
    else:
        tt += i
        ts += 1
print("Tek adet",ts,"Tek toplam =", tt)
print("Çift adet",cs,"Çift toplam =", ct)
print("Tek Ortalama",tt/ts)
print("Çift Ortalama",ct/cs)