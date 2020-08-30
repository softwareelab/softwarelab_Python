print("-----Menu-----")
#islem yapacak metotlar
def toplama():
    sayi1 = int(input("1. sayıyı giriniz: "))
    sayi2 = int(input("2. sayıyı giriniz: "))
    toplamaislemi = sayi1 + sayi2
    print("sonuc: ", toplamaislemi)

def cikarma():
    sayi1 = int(input("1. sayıyı giriniz: "))
    sayi2 = int(input("2. sayıyı giriniz: "))
    cikarmaislemi = sayi1 - sayi2
    print("sonuc: ", cikarmaislemi)

def bolme():
    try:
        sayi1 = int(input("1. sayıyı giriniz: "))
        sayi2 = int(input("2. sayıyı giriniz: "))
        bolmeislemi = sayi1 // sayi2
        print("sonuc: ", bolmeislemi)
    except ZeroDivisionError:
        print("Tanımsız! Bir sayıyı 0'a bölemezsiniz!")

def carpma():
    sayi1 = int(input("1. sayıyı giriniz: "))
    sayi2 = int(input("2. sayıyı giriniz: "))
    carpmaislemi = sayi1 * sayi2
    print("sonuc: ", carpmaislemi)

try:
    secim = int(input("1.Toplama\n"
                      "2.Çıkarma\n"
                      "3.Bölme\n"
                      "4.Çarpma\n"
                      "İşlem Seçiniz: "))
    if secim <= 0 or secim >=5:
        print("sadece 1-4 arası secim yapabilirsiniz!")
    else:
        # secim kararına göre işlemi yaptırma
        if secim == 1:
            toplama()
        elif secim == 2:
            cikarma()
        elif secim == 3:
            bolme()
        elif secim == 4:
            carpma()

except ValueError:
        print("Sadece rakam girebilirsiniz!")

