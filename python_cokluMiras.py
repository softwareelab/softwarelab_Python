class Ebeveyn1:
    def __init__(self):
        self.sac_tipi = 'Dalgalı'
    def goz_rengi(self):
        return  'Kahverengi'

class Ebeveyn2:
    def __init__(self):
        self.sac_tipi = 'Kıvırcık'
    def sac_rengi(self):
        return 'Siyah'

class Ornek(Ebeveyn1, Ebeveyn2):
    pass

class Ornek2(Ebeveyn2, Ebeveyn1):
    pass



x = Ornek()
y = Ornek2()
print(x.sac_tipi)
print(x.goz_rengi())
print(y.sac_tipi)
print(y.sac_rengi())