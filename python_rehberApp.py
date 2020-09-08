rehber = {
    'kisi1': '0555 555 55 55',
    'kisi2': '0544 444 44 44',
    'kisi3': '0533 333 33 33'
}
while True:
    print("""
    [1] Numara Ekle
    [2] Numara Sorgula
    [3] Nurama Sil
    [4] Numara Güncelle
    [Q] Çık    
    """)
    secim = input("işlem seciniz: ")
    if secim == '1':
        ekle_ad = input("kisinin adını giriniz: ")
        ekle_no = input("kisinin numarasını giriniz: ")
        rehber[ekle_ad] = ekle_no
    elif secim == '2':
        anahtar = input("İsim: ")
        if anahtar in rehber.keys():
            print(rehber[anahtar])
        else:
            print("böyle bir kişi yok!")
    elif secim == '3':
        silinecek_kisi = input("silinecek kisinin adını giriniz: ")
        rehber.pop(silinecek_kisi)
    elif secim == '4':
        guncellenmek_istenen_kisi = input("güncellemek istediğiniz kisinin adı")
        if guncellenmek_istenen_kisi in rehber.keys():
            guncellenen_numarasi = input("Yeni numarayı giriniz: ")
            rehber[guncellenmek_istenen_kisi] = guncellenen_numarasi
            print("guncelleme işlemi basarılı!")
        else:
            print("böyle bir kayıt mevcut değil!")
    elif secim == 'Q' or secim == 'q':
        break
    else:
        print("hatalı numara!")