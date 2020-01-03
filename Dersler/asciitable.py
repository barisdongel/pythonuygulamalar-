#karakterlerin dec-oct-hex karşılıklarına ulaşabileceğimiz bir tablodur.
import random
print(chr(64))#@
print(chr(65))#A
print(chr(66))#B
print(chr(67))#C

print(ord("D"))#68
print(ord("E"))#69
print(ord("F"))#70
print(ord("G"))#71

c = ''
s = ""
for i in range(5):
    c = chr(random.randint(65,90))
    s += c

print(s)