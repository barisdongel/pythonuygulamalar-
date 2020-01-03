#sıralama algoritması (bubblesort)
liste =[3,9,2,1,11,7]
u=len(liste)
i=0
j=0
swap=0
for i in range(u-2):
    j = i+1
    for j in range(u-1):
      if liste[j]>liste[j+1]:
          swap = liste[j]
          liste[j]=liste[j+1]
          liste[j+1]=swap

print(liste)