def cift_sayilar(sayi):
    liste=[]
    for i in range(1, sayi, 1):
        if (i % 2 == 0):
            liste.append(i)
    return liste