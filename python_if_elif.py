yas = int(input("Yaşınızı Giriniz:"))
if (yas > 0):
    if (yas < 18):
        print("Yaşınız 18'den Küçük")
    elif (yas >= 18 and yas < 25):
        print("Yaşınız 18-24 arasında")
    elif (yas >= 25 and yas < 35):
        print("Yaşınız 25-34 arasında")
    else:
        print("Yaşınız 35 yada 35'den büyük")
elif (yas < 0):
    print("Yaşınız 0'dan küçük olamaz!")