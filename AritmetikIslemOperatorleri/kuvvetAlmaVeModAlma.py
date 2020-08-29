#Soru:Kullanıcıdan 2 adet sayı iste ve 1. sayının kuvveti olarak 2. sayıyı alın.
#Elde edilen sonucun dönde bölümünden kalan sayıyı ekrana yazdırın

#Adım 1: Sayıları aldık
sayi1 = int(input("Birinci sayıyı giriniz:"))
sayi2 = int(input("İkinci sayıyı giriniz:"))

#Adım 2: Birinci sayının kuvveti olarak ikinci sayıyı aldık
kuvvetAlindi = sayi1 ** sayi2
print("Burayı kontrol amaçlı kuvvet aldığını görmek için yaptık",kuvvetAlindi)

#Adım 3: Elde edilen sonucun 4'den bölümünden kalanını alma
modAlindi = kuvvetAlindi % 4

#Adım 4: Ekrana yazdırma
print("Sonuç: ",modAlindi)