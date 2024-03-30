print("""**********
Beden Kitle Endeksi Hesaplama 


************
""")

boy = float(input("Boyunuzu Giriniz:"))
kilo = int(input("Kilonuzu Giriniz:"))

bki =  kilo / (boy ** 2)

if (bki < 18.5):
    print("Zayıf:")
elif (18.5<bki<25):
    print("Normal:")
elif (25<bki<30):
    print("Fazla Kilolu:")
elif (bki>30):
    print("Obez:")            
