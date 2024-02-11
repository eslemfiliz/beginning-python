# Ali, Beyza 
#  Ali= [4,7,2,9,10,3]
#  Beyza=[5,7,10,1,6,8]

# Ali 'nin toplam skoru yazılacak.
# Beyza 'nin toplam skoru yazılacak.
#  Ali kazandı/ Beyza kazandı/ Berabere

ali_skorlar= [4,7,2,9,10,3]
beyza_skorlar = [5,7,10,1,6,8]

skor_sayisi = len(ali_skorlar)

ali_toplam_puan=0
beyza_toplam_puan=0

for i in range(skor_sayisi):
    if ali_skorlar[i] > beyza_skorlar[i]:
        ali_toplam_puan += 1
    elif beyza_skorlar[i]> ali_skorlar[i]:
        beyza_toplam_puan += 1
print("Ali'nin toplam puanı: {}".format(ali_toplam_puan))
print("Beyzanın toplam puanı: %i"%(beyza_toplam_puan))

if ali_toplam_puan > beyza_toplam_puan:
    print("Ali kazandı.")
elif beyza_toplam_puan > ali_toplam_puan:
    print("Beyza kazandı.")
else:
    print("Berabere.")        