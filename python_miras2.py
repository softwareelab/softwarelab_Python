class Birey:
    def __init__(self, ad:str, soyad:str, tcno:int):
        self.ad = ad
        self.soyad = soyad
        self.tcno = tcno


class Calisan(Birey):
    def __init__(self, ad:str, soyad:str, tcno:int, maas:float):
        super().__init__(ad, soyad, tcno)
        self.maas = maas
    def zamyap(self, miktar:float):
        self.maas += miktar

class Muhendis(Calisan):
    def __init__(self, ad:str, soyad:str, tcno:int, maas:float,
                 yabanci_diller:list, yazilim_dilleri:list):
        super().__init__(ad, soyad, tcno, maas)
        self.yabanci_diller = yabanci_diller
        self.yazilim_dilleri = yazilim_dilleri

    def yabanci_dilekle(self, yeni_dil:str):
        self.yabanci_diller.append(yeni_dil)

    def yazilim_diliekle(self, yeni_dil:str):
        self.yazilim_dilleri.append(yeni_dil)

class Muhasebeci(Calisan):
    def __init__(self, ad:str, soyad:str, tcno:int, maas:float,
                 bilinen_programlar:list):
        super().__init__(ad, soyad, tcno, maas)
        self.bilinen_programlar = bilinen_programlar

    def program_ekle(self, yeni_program):
        self.bilinen_programlar.append(yeni_program)





#ss alma alt kısmı

kac_calisan_eklenecek = int(input("Kaç çalışan eklenecek: "))
for i in range(kac_calisan_eklenecek):
    calisan_adi = str(input("{}. çalışan adı:"))
    calisan_soyadi = str(input("çalışan soyadı:"))
    calisan_tc = int(input("çalışan tc:"))
    calisan_maas = float(input("çalışan maas:"))
    calisan = Calisan(calisan_adi, calisan_soyadi, calisan_tc, calisan_maas)

print("calısanın bilgileri")
print(calisan_adi, calisan_soyadi, calisan_tc, calisan_maas)















