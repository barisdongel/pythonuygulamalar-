#global ve local değişkenler

a = 5

def fonksiyonum():
    a = 2 #başlangıç değeri atadık
    a = a + 5
    print("Fonksiyonun içinde a",a)

fonksiyonum()

x = 5
y = 3

def kuvvet(x,y):
    return x**y

print(kuvvet(x,y))