
#class olusturulmasu
class Matematik:
    pi = 3.14
    euler = 2.72
    # self kelimesi kare_alan_bul methodun Matematik clasina ait oldugunu belirtiyor
    def kare_alan_bul(self,kenar_uzunlugu):
        return kenar_uzunlugu*kenar_uzunlugu
    
    pass 

#Class cagririlmasi
math = Matematik()

print(math)

print(math.kare_alan_bul(4))