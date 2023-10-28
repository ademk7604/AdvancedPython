okulnumarasi = 84

okuladi = "Istanbul otaokulu"

#dictionary veri tipi

ogrenci = {
    "okulNo":84,
    "okulAdi": "Buyuk Istanbul Ortaokulu",
    "sinavNotu": 71.2
}

print(ogrenci["okulNo"])
print(ogrenci["sinavNotu"])
print("-------------")
ogrenciler = {
    "ogrenci1": {
        "okulNo":80,
        "okulAdi": "Buyuk Istanbul Ortaokulu",
        "sinavNotu": 71.2
    },
    "ogrenci2": {
        "okulNo":87,
        "okulAdi": "Istanbul Ortaokulu",
        "sinavNotu": 88
    }
}

print(ogrenciler["ogrenci2"]["okulNo"])