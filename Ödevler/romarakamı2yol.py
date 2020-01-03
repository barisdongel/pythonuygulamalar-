#0-100arası roma rakamları

s = {"I":1,"V":5,"X":10,"L":50,"C":100}

rr=input("Roma rakamı giriniz:")
u =len(rr) - 1
d = s[rr[u]]
id = 0

for i in range(u):
    id = s [rr[i]]
    if d <= id:
        d += id
    else :
        d -= id
print(d)