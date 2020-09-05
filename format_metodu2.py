veriler = list()
yazarlar = list()
kitaplar = list()
sayfalar = list()

with open('veriler.csv') as file:
    for i in file.readlines():
        veriler.append(i[:-1])

for i in veriler:
    line = i.split(',')
    yazarlar.append(line[0])
    kitaplar.append(line[1])
    sayfalar.append(line[2])


metin = "{:<20} {:<20} {:<4}"

for i in range(len(yazarlar)):
    print(metin.format(yazarlar[i], kitaplar[i], sayfalar[i]))