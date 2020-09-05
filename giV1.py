import cv2
import numpy as np

#resmi resim değişkenine aktardık, imread okuttuk
resim = cv2.imread("fotograf_ornekleri/ay1.jpg")

#resimi gri tonladık, imshow diyerek resmi göstermesini sagladık
resimGri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

#resmi bulanıklastırdık, imshow diyerek resmi göstermesini sagladık
resimBlur = cv2.GaussianBlur(resimGri, (5,5), 0)

#treshold resimdeki siyah ve beyazlık
# seviyelerini ortaya cıkartıyor kendi belirlediğimiz seviyelere göre atıyoruz
ret, resimThreshold= cv2.threshold(resimBlur, 130, 255, cv2.THRESH_BINARY)

#maskeleme işlemi
resimMask= cv2.bitwise_and(resim, resim, mask=resimThreshold)

resimHsv = cv2.cvtColor(resimMask, cv2.COLOR_BGR2HSV)
griAltSiniri = np.array([0, 0, 15])
griUstSiniri = np.array([255, 120, 255])
gri_Renk_Filtre_Sonuc = cv2.inRange(resimHsv, griAltSiniri, griUstSiniri)
sonuc = resim.copy()
cnts, hierarchy = cv2.findContours(gri_Renk_Filtre_Sonuc, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

maxWidth = 0
maxHeight = 0
maxIndex = -1
for t in range(len(cnts)):
    cnt = cnts[t]
    x, y, w, h = cv2.boundingRect(cnt)
    if (w > maxWidth and h > maxHeight):
        maxWidth = w
        maxHeight = h
        maxIndex = t

x, y, w, h = cv2.boundingRect(cnts[maxIndex])
cv2.rectangle(sonuc, (x,y), (x+w, y+h), (0,255,0), 2)
cv2.imshow("sonuc", sonuc)

#tusa basılana kadar ekrana göstermesini istedik
cv2.waitKey(0)