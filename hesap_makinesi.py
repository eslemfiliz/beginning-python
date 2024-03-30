print("""**********
Hesap Makinesi Programı


İşlemler;

1. Toplama

2. Çıkarma

3. Çarpma
      
4. Bölme
**************                           
""")
a = int(input("Birinci Sayıyı giriniz:"))
b= int(input("İkinci Sayıyı Giriniz:"))

işlem = input("İşlemi giriniz:")

if işlem == "1":
    print("{} ile {} in toplamı {} dir".format(a,b,a+b))

if işlem == "2":
    print("{} ile {} in farkı {} dır".format(a,b,a-b))   
if işlem == "3":    
     print("{} ile {} çarpımı {} dir".format(a,b,a*b))
if işlem == "4":
    print("{} ile {} bölümü {}dir".format(a,b,a/b))       