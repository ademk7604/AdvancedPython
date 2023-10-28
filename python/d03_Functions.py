print("Program tarted")

def ekranayazdir():
    print("Benim Kurem")
    pass

ekranayazdir()

print("Programm ended")
print("--------------")

def ekranayazdir1():
    print("Normal yazdir")
    pass

ekranayazdir1()
print("--------------")

def gelenyaziyiyazdir(geliyor):
    print(geliyor)
    pass

mesaj = "23.satirdaki yazi yazdiriliyor"
gelenyaziyiyazdir(mesaj)
print("--------------")

def ikinin_dor_katini_don():
    return 2*4

donen_sayi = ikinin_dor_katini_don()

print(donen_sayi)

print("**********")

def buyuk_olani_don(sayi_bir,sayi_iki):
    if sayi_bir>sayi_iki:
        return sayi_bir
    else:
        return sayi_iki
    pass

buyuk_sayi = buyuk_olani_don(1000,1001)

print(buyuk_sayi)

