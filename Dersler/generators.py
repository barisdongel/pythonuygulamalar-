#üreteçler

def uretec():
    sayi = 0
    print(sayi,". adım")
    yield sayi #yield , return yerine kullanırı

    sayi += 1
    print(sayi, ". adım")
    yield sayi

    sayi += 1
    print(sayi, ". adım")
    yield sayi

a=uretec()

next(a)
next(a)
next(a)
#next(a) stopiteration hatası veriri

b = uretec()
for x in b:
    print(x)