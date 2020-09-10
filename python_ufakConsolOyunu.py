from random import randint

class Asker:
    def __init__(self):
        self.can = randint(30, 70)
        self.hasar = randint(30, 90)
        self.canli_mi = True

    def oldu_mu(self):
        self.canli_mi = False

    def hasar_aldi(self, alinan_hasar:int):
        if alinan_hasar >= self.can:
            self.oldu_mu()
        else:
            self.can -= alinan_hasar

class Oyuncu:
    def __init__(self):
        self.can = randint(600, 800)
        self.hasar = randint(30, 90)
        self.canli_mi = True

    def oldu_mu(self):
        self.canli_mi = False

    def hasar_aldi(self, alinan_hasar:int):
        if alinan_hasar >= self.can:
            self.oldu_mu()
        else:
            self.can -= alinan_hasar

askerler = [Asker() for i in range(10)]
oyuncu = Oyuncu()

while True:
    print("-----Oyuncu Bilgileri-----")
    print("Oyuncu Sağlık: {}  ---Oyuncu Hasar: {}".format(oyuncu.can, oyuncu.hasar))
    print("\n-----Askerler-----")

    for numara, asker in enumerate(askerler):
        if asker.canli_mi:
            print("{}. Asker --- Can değeri: {} --- Hasar değeri: {}".format(numara, asker.can, asker.hasar))


    secilen_asker = int(input("Saldırı için seçilen asker: "))
    if secilen_asker > len(askerler) - 1 or secilen_asker < 0:
        print("Girilen asker numarası yanlış!")
        continue
    else:
        askerler[secilen_asker].hasar_aldi(oyuncu.hasar)
        if askerler[secilen_asker].canli_mi == False:
            askerler.remove(askerler[secilen_asker])

        if askerler:
            saldiran_asker = randint(0, len(askerler)-1)
            oyuncu.hasar_aldi(askerler[saldiran_asker].hasar)
        else:
            print("Tebrikler! Tüm düşmanlar öldü, kazandın!")
            quit()