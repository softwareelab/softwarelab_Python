import random
random_sayi = round(random.random()*100)#0-100 arası
girilen_sayi = int(input("0-100 arası sayı giriniz:"))
while  random_sayi != girilen_sayi:
    if (girilen_sayi > random_sayi):
        print("Büyük bir sayı girdiniz!")
    else:
        print("Kücük bir sayı girdiniz!")
    girilen_sayi = int(input("0-100 arası sayı giriniz:"))
print("tebrikler sayıyı buldunuz!!")