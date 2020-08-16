sayi1 = int(input("ilk sayıyı giriniz:"))
sayi2 = int(input("ikinci sayıyı giriniz:"))

secim = int(input("1.Toplama\n"
                  "2.Çıkartma\n"
                  "3.Bölme\n"
                  "4.Çarpma\n"
                  "5.Mod alma\n"))
if (secim < 0 or secim > 5):
    print("Seçiminiz 1- 5 arası olmalı!")
elif (secim == 1):
    toplama = sayi1 + sayi2
    print("Sonuç:",toplama)
elif (secim == 2):
    if(sayi1 < sayi2):
        print("İlk sayı İkinci sayıdan Kücük"
              "Çıkartma işlemi başarısız!")
    else:
        cikartma = sayi1 - sayi2
        print("Sonuç:",cikartma)
elif (secim == 3):
    bolme = sayi1 // sayi2
    print("Sonuç:",bolme)
elif (secim == 4):
    carpma = sayi1 * sayi2
    print("Sonuç:",carpma)
elif (secim == 5):
    modalma = sayi1 % sayi2
    print("Mod:",modalma)