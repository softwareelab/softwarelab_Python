import cv2
import numpy as np
import os

kamera = cv2.VideoCapture(0)
kernel = np.ones((8,8), np.uint8)

while True:
    ret, kare = kamera.read()
    kesilmis_kare = kare[0:250, 0:250]
    kesilmis_kare_gri = cv2.cvtColor(kesilmis_kare, cv2.COLOR_BGR2GRAY)
    #kesilmis_kare_hsv = cv2.cvtColor(kesilmis_kare, cv2.COLOR_BGR2HSV)

    #alt_degerler = np.array([0, 5, 50])
    #ust_degerler = np.array([90, 255, 255])

    #renk_filtresi_sonucu = cv2.inRange(kesilmis_kare_hsv, alt_degerler, ust_degerler)
    #renk_filtresi_sonucu = cv2.morphologyEx(renk_filtresi_sonucu, cv2.MORPH_CLOSE, kernel)

    ret2, kesilmis_kare_threshold = cv2.threshold(kesilmis_kare_gri, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    #cv2.imshow("Kare", kare)
    #cv2.imshow("kesilmis kare",kesilmis_kare)
    #cv2.imshow("renk filtresi sonucu", renk_filtresi_sonucu)
    cv2.imshow("renk filtresi threshold", kesilmis_kare_threshold)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()