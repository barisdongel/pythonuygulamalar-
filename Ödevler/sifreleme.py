"""
Barış Ömer DÖNGEL
19410051042
"""
import random

length = 6 #Uzunluğunu belirttik
numbers = (48, 58) #48,58 arasında ki ascii(sayı) değerlerini
uppercases = (65, 91) #65,91 arasında ki ascii(büyük harf) değerlerini
lowercases = (97, 123) #97,123 arasındaki ascii(küçük harf) değerlerini aldık

#for döngüsünün mantığı da her elemanı liste içinde ayrı ayrı elemanlara dönüştüryo
ascii_numbers = [x for x in range(numbers[0], numbers[1])]#numbers listesinin 0ıncı ve 1. elemanını (0 dan 9'a kadar rakamları)
ascii_uppercases = [x for x in range(uppercases[0], uppercases[1])]#uppercase listesinin 0ıncı ve 1. elemanını(A dan Z'ye kadar harfleri)
ascii_lowercases = [x for x in range(lowercases[0], lowercases[1])]#lowercase listesinin 0ıncı ve 1. elemanını(a dan z'ye kadar harfleri) ascii_ listelerine aldık

must_number = random.choice(ascii_numbers)#ascii_numbers listesinden random bir değer aldık ve must_number adında bir değişkene atadık
must_uppercase = random.choice(ascii_uppercases)#ascii_uppercases listesinden random bir değer aldık ve must_uppercases adında bir değişkene atadık
must_lowercase = random.choice(ascii_lowercases)#ascii_lowercases listesinden random bir değer aldık ve must_lowercases adında bir değişkene atadık
other_random = random.sample(ascii_numbers + ascii_uppercases + ascii_lowercases, k = length - 3)#other_random diye bir değişken açıp içerisine random.sample ile karışık 3 adet rakam kharf ve bharf aldık.

password_chars = [must_number, must_uppercase, must_lowercase] + other_random #tüm değişkenlerimizi bir listeye atadık ve en son karmaşık liste olan other_random'u listeye atadık.
password_chars = [chr(x) for x in password_chars]#listeyi chr ile karaktere dönüştürdük.
random.shuffle(password_chars)#listeyi karıştırdık
password = "".join(password_chars)#liste elemanları arasında ki boşlukları sildik

print("Şifreniz :",password)
