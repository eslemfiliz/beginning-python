# len - listenin uzunluğunu verir.
# max - listenin maksimum elemanını verir.
# min - listemin minimum elemanını verir.
# enumerate - listenin herbir elemanı indexi ile beraber tuple olarak döndürür.


# liste = [1,2,3,4,5,6,7,8]
# liste_uzunluk = len(liste)
# print(liste_uzunluk)

liste = [1,2,3,4,5,6,7,8]

for index, eleman in enumerate(liste):
    print(" index", index)
    print("eleman",eleman) 