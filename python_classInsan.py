class Insan:
    def __init__(self, ad, soyad, cinsiyet):
        #self.ad ile ad değişkeni aynı değişken değillerdir
        #self.ad nesnenin (classın) her yerinde kullanılabilirken
        #ad değişkeni ise sadece bu metot içerisinde kullanılabilir
        self.ad = ad
        self.soyad = soyad
        self.cinsiyet = cinsiyet

ornekler = list()

for i in range(5):
    ad = input("adınız: ")
    soyad = input("soyadınız: ")
    cinsiyet = input("cinsiyetiniz: ")
    ornekler.append(Insan(ad, soyad, cinsiyet))

for i in ornekler:
    print("classtaki isimler= ",i.ad)

