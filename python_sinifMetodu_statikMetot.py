class Ucak:
    ucaklar = list()
    def __init__(self):
        pass
    @classmethod
    def ucak_sayisini_goster(cls):
        print(len(cls.ucaklar))

    @staticmethod
    def staticmetotcalisti():
        print("static metot calıstı")

Ucak.ucak_sayisini_goster()
Ucak.staticmetotcalisti()