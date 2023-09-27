"""
1- 87
2- 64 
3- 29
4- 62
5- 39
6- 55

"""

notlar = [87,64,29,62,39,55]

for n in notlar:
    if n < 40 :
        print(n)
    else:
        if n % 5 == 0:
            print(n)
        elif n % 5 >=3:
            print(n+(5-n%5))  
        else:
            print(n)                