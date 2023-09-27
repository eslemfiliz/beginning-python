"""
AND (ve): Karşilastirilan her iki deger True ise sonucu True döndürür.
Diger durumlarda False döndürür.
OR (veya): Karsilastirilan her iki deger False ise sonucu False döndürür.
Diger durumlarda True döndürür.
NOT (degildir): Bool degeri tersine cevirir.
"""
a = 5
b = 3
c = 5

# print(a == b or a == c)
# print(a == b and a == c)
# print((a == b or a == c) and (a == b and a == c))

print(not(a == b or a == c))