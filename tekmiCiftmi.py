adet = int(input("Kaç Adet Sorgu Yapılacak: "))
for i in range(adet):
    girilensayi = int(input("sayıyı giriniz: "))
    if  girilensayi % 2 == 0:
        print(girilensayi, " çifttir")
    else:
        print(girilensayi," Tektir")