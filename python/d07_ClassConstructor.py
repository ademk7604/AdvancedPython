
class Araba:
    marka = "Mercedes"
    teker_sayisi = 4
    motor_gucu = 750
    motor_hacmi = 2300
    # __init__ initialize yani baslangic degeri, construtor idir. yani yapici methodu
    # Bu class ilk cagrildiginda once burasi calisir ilk degerler atanir
    
    def __init__(self,marka,teker_sayisi,motor_gucu,motor_hacmi):
        self.marka = marka
        self.teker_sayisi = teker_sayisi
        self.motor_gucu = motor_gucu
        self.motor_hacmi = motor_hacmi
        pass
    pass

Opel = Araba("Opel",4,250,1200)
Renault = Araba("Renault",5,500,1700)

print("----")



