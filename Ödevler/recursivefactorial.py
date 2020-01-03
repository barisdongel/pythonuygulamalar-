#19410051042
#Barış Ömer Döngel

#recursive
def fac(n):
    return 1 if (n < 1) else n * fac(n-1)
print (fac(int(input("Bir sayı giriniz:"))))