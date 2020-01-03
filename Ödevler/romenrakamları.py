# BARIŞ ÖMER DÖNGEL
# 19410051042

# Bu fonksiyon değeri Roman Sembolüne dönüştürüyor.
def value(r):
	if (r == 'I'):
		return 1
	if (r == 'V'):
		return 5
	if (r == 'X'):
		return 10
	if (r == 'L'):
		return 50
	if (r == 'C'):
		return 100
	return -1

def romanToDecimal(str):
	res = 0
	i = 0

	while (i < len(str)):
		s1 = value(str[i])

		if (i+1 < len(str)):
			s2 = value(str[i+1])

			if (s1 >= s2):

				res = res + s1
				i = i + 1
			else:

				res = res + s2 - s1
				i = i + 2
		else:
			res = res + s1
			i = i + 1

	return res

# Çalıştırma komutu
print(romanToDecimal(input("Roman rakamı giriniz:")))
