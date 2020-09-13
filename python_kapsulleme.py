import random

class Birey:
    def __init__(self, ad:str, soyad:str, tcno:int):
        self.ad = ad
        self.soyad = soyad
        self.tcno = tcno

#kapsullenmiş halini yazalım simdi

class Birey2:
    def __init__(self, ad:str, soyad:str, tcno:int):
        self.__ad = ad
        self.__soyad = soyad
        self.__tcno = tcno

    def get_tcno(self):
        return self.__tcno

    def get_name(self):
        return self.__ad

    def get_lastname(self):
        return self.__soyad

x = Birey2('Software', 'Lab', '12345678901')
print(x.get_name())