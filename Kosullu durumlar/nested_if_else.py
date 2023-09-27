#  iç içe koşullar
liste1 = [1,2,3,4,]
liste2 = [5,6,7,8,9]

a,b = 1,5

if a in liste2 :
    if b in liste2 :
        print("a liste2 de var. b liste2 de var.")   
    else: 
        print("a liste2 de var. b liste2 de yok")    
else : 
    if a in liste1:
        print("a liste1 de var. b liste1 de yok.")

    else : 
        if b in liste1:
            print("b liste1 de var. a liste1 de yok.")            