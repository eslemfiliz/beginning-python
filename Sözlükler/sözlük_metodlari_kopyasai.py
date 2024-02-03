sozluk = {"ad ": "Eslem" , "soyad " :"Filiz", "no": 123}
sozluk2= {"not":100}

# # print(sozluk)
# # sozluk.clear()
# # print(sozluk)

# # del sozluk["no"]
# # print(sozluk)

# liste = list(sozluk.items())
# print(liste)

# # for i in liste:
# #     print(i)

# for i, j in liste:
#     print(i)
#     print(j)

# a = sozluk.get("not", False)
# print(a)

sozluk.update(sozluk2)
print(sozluk)
print(sozluk2)