# # liste = [1,2,3,4,5]

# # for eleman in liste:
# #     print(eleman)

# toplam = 0

# liste= [1,2,3]

# for eleman in liste:
#     toplam = toplam + eleman
#     print("Toplam {}: Eleman :{}".format(toplam,eleman)) 
# print(toplam)    

liste = [2,1,10,2,23,1,56,3]
 
total = 0
for i in liste:
    if (not (i % 2 == 0)):
        total += i
 
print(total)