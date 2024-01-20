"""
Harf büyütme küçültme metodları:
-capitalize,lower,upper,swapcase,litle
Sorgulama metodları:
-startswith,endswith,isalpha,isnumeric,isalnum,islower,isupper,istitle,isspace
Özellik metodları:
-len,max,min,count,find,index,rfind,rindex
Diğer metodlar:
-join,replace,center,ljust,lstrip,rstrip,split,strip
"""

# a = "merhaba"
# a = a.capitalize()
# print(a)
# # baş harfi büyüttü

# b = "eslem filiz"
# b = b.title()
# print(b)
# # iki kelimenin baş harflerini büyütür

# a= "Merhaba Dünya!"
# b="Python"

# # a.replace yer değiştiriyor
# a = a.replace("Dünya",b)
# print(a)

# a= "Python"
# a= a.center(20, "-")
# print(a)

# a= "Python"
# a= a.rjust(20, "-")
# print(a)

# a= "   Python   "
# a= a.strip()
# print(a)

a= "123,25,36,25,14,252,2"
b= a.split(",")
print(b)