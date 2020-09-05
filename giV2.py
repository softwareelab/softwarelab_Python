import cv2
import numpy as np

video = cv2.VideoCapture("video_ornekleri/ay_video1.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel=np.ones((5,5), np.uint8)
while (1):
    ret, kare = video.read()
    arkaplansilinmis = fgbg.apply(kare)
    arkaplansilinmis = cv2.morphologyEx(arkaplansilinmis, cv2.MORPH_OPEN, kernel)
    sonuc = kare.copy()

    cnts, hierarchy = cv2.findContours(arkaplansilinmis, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for cnt in cnts:
        x, y, w, h = cv2.boundingRect(cnt)
        if  (w>30 and h>30):
            cv2.rectangle(sonuc, (x,y), (x+w, y+h), (0,255,0), thickness=4)


    cv2.imshow("sonuc",sonuc)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

video.release()
cv2.destroyAllWindows()