vize = int(input("Vize notunu giriniz:"))

while True:
    if vize < 0 or vize>100:
        print("Lütfen 0 ile 100 arasında bir değer giriniz.")
        vize = int(input("Vize notunu giriniz:"))
    else:
        break

final = int(input("Final notunu giriniz:"))
while True:
    if final <0 or final>100:
        print("Lütfen 0 ile 100 arasında bir değer giriniz")
        final = int(input("Final Notunuzu giriniz:"))
    else:
        break
print("Ortalamanız:",vize*0.4+final*0.6)