import cv2
import numpy as np
import os

kamera = cv2.VideoCapture(0)
kernel = np.ones((8,8), np.uint8)
fgbg = cv2.createBackgroundSubtractorMOG2()

def resimfarkbul(resim1,resim2):
    resim2 = cv2.resize(resim2, (resim1.shape[1], resim1.shape[0]))
    fark_resim = cv2.absdiff(resim1, resim2)
    fark_sayi = cv2.countNonZero(fark_resim)
    return fark_sayi
    #cv2.imshow("fark resim", fark_resim)

def veriyukle():
    veri_isimler = []
    veri_resimler = []

    dosyalar = os.listdir("veri/")
    for dosya in dosyalar:
        veri_isimler.append(dosya.replace(".jpg",""))
        veri_resimler.append(cv2.imread("veri/"+dosya, 0))
    return veri_isimler, veri_resimler

def siniflandir(resim, veri_isimler, veri_resimler):
    min_index = -1
    min_deger = resimfarkbul(resim,veri_resimler[0])
    for t in range(len(veri_isimler)):
        fark_deger = resimfarkbul(resim,veri_resimler[t])
        if(fark_deger<min_deger):
            min_deger=fark_deger
            min_index=t
    return veri_isimler[min_index]

veri_isimler, veri_resimler =veriyukle()
#veri_resim1 = cv2.imread("veri/bir.jpg", 0)




while True:
    ret, kare = kamera.read()
    kesilmis_kare = kare[0:250, 0:250]
    kesilmis_kare_gri = cv2.cvtColor(kesilmis_kare, cv2.COLOR_BGR2GRAY)
    kesilmis_kare_hsv = cv2.cvtColor(kesilmis_kare, cv2.COLOR_BGR2HSV)
    fgmask = fgbg.apply(kesilmis_kare)

    kesilmis_kare_canny = cv2.Canny(kesilmis_kare_gri, 100, 150)


    #kesilmis_kare_canny = cv2.dilate(kesilmis_kare_canny, kernel, iterations=1)
    #kesilmis_kare_canny = cv2.morphologyEx(kesilmis_kare_canny, cv2.MORPH_CLOSE, kernel)


    alt_degerler = np.array([0, 5, 50])
    ust_degerler = np.array([90, 255, 255])

    renk_filtresi_sonucu = cv2.inRange(kesilmis_kare_hsv, alt_degerler, ust_degerler)
    renk_filtresi_sonucu = cv2.morphologyEx(renk_filtresi_sonucu, cv2.MORPH_CLOSE, kernel)

    sonuc = kesilmis_kare.copy()
    ret2, kesilmis_kare_threshold = cv2.threshold(kesilmis_kare_gri, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cnts, hierarchy = cv2.findContours(kesilmis_kare_threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    max_genislik = 0
    max_uzunluk = 0
    max_index = -1
    for t in range(len(cnts)):
        cnt = cnts[t]
        x, y, w, h = cv2.boundingRect(cnt)
        if(w>max_genislik and h>max_uzunluk):
            max_uzunluk = h
            max_genislik = w
            max_index = t

    if (len(cnts)>0):
        x,y,w,h = cv2.boundingRect(cnts[max_index])
        cv2.rectangle(sonuc, (x, y), (x + w, y + h), (0, 255, 0), 2)
        el_resim = kesilmis_kare_threshold[y:y + h, x:x + w]
        cv2.imshow("el resim", el_resim)
        print(siniflandir(el_resim,veri_isimler,veri_resimler))



    cv2.imshow("sonuc", sonuc)



    #cv2.imshow("Kare", kare)
    #cv2.imshow("kesilmis kare",kesilmis_kare)
    #cv2.imshow("kesilmis kare Canny",kesilmis_kare_canny)
    #cv2.imshow("renk filtresi sonucu", renk_filtresi_sonucu)
    #cv2.imshow("renk filtresi threshold", kesilmis_kare_threshold)
    #cv2.imshow("a", fgmask)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()