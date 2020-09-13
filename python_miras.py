class Calisan:
    def __init__(self, ad, soyad, tc_no):
        self.ad = ad
        self.soyad = soyad
        self.tc_no = tc_no
        self.maas = 3000


class A_blok(Calisan):
    def __init__(self, ad, soyad, tc_no):
        """
        bizim kodumuz kısa oldugu icin yeniden yazabildik
        lakin kodumuz bu kadar kısa değil de daha fazla olsaydı
        hepsini yeniden mi yazacaktık = 'HAYIR!'
        bunun için önce fonksiyonu cağıracağız
        sonrasında miras alınan sınıfa ait metotları kullanmak
        içn super() fonksiyonunu kullanacagız:
        super().__init__(ad, soyad, tc_no)
        """

        #self.ad = ad
        #self.soyad = soyad
        #self.tc_no = tc_no

        #güncellemek istedigimizi yazdık
        super().__init__(ad, soyad, tc_no)
        self.maas = 4000

class B_blok(Calisan):
    pass


softwarelab = A_blok('Software', 'Lab', '12345678912')
softwarelab2 = B_blok('Software2', 'Lab2', '21987654321')


print("-----Software 1 bilgiler-----")
print("-----Software 1 maas bilgisini yükselttik-----")
print(softwarelab.ad)
print(softwarelab.soyad)
print(softwarelab.tc_no)
print(softwarelab.maas)
print("-----Software 2 bilgiler-----")
print(softwarelab2.ad)
print(softwarelab2.soyad)
print(softwarelab2.tc_no)
print(softwarelab2.maas)