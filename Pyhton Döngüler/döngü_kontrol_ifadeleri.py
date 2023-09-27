"""
break
continue
"""
# a = 0
# while True:
#     a += 1
#     print(a)
#     if  a == 10000:
#         break
#         print("arttırıldı.")
# print("durdu.")


a = 0
while True:
    if a % 2 == 0:
        continue
    print(a)
    if  a < 100:
        break
    print("durdu.")