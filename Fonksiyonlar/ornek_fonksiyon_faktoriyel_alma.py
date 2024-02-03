# faktoryel
# 5! = 1*2*3*4*5
# negatif sayı olmayacak
# eger sıfır ise 1 döneceğiz

def faktoryel(x):
    sonuc = 1
    if x <0 or int(x)!= x :
        print("Sayının faktoriyeli yoktur!")
    elif x == 0:
        print(sonuc)
    else:
        while x > 1:
            sonuc *= x
            x -= 1
        print(sonuc)

x = float(input("Sayi giriniz:")) 

faktoryel(x)