import cv2
import numpy as np

video = cv2.VideoCapture("video_ornekleri/trafik.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel=np.ones((5,5), np.uint8)

class Koordinat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Sensor:
    def __init__(self, Koordinat1, Koordinat2, karegenislik, kareuzunluk):
        self.Koordinat1 = Koordinat1
        self.Koordinat2 = Koordinat2
        self.karegenislik = karegenislik
        self.kareuzunluk = kareuzunluk
        self.maskeAlani = abs(self.Koordinat2.x - self.Koordinat1.x) * abs(self.Koordinat2.y - self.Koordinat1.y)
        self.maske= np.zeros((kareuzunluk, karegenislik, 1), np.uint8)
        cv2.rectangle(self.maske, (self.Koordinat1.x, self.Koordinat1.y), (self.Koordinat2.x, self.Koordinat2.y), (255), thickness=cv2.FILLED)
        self.durum = False
        self.algilananAracSayisi = 0

def GolgeSil(video):
    rgb_planes = cv2.split(video)
    dst = np.zeros(shape=(5, 2))
    result_planes = []
    result_norm_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((7, 7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        norm_img = cv2.normalize(diff_img, dst, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
        result_planes.append(diff_img)
        result_norm_planes.append(norm_img)
    result = cv2.merge(result_planes)
    result_norm = cv2.merge(result_norm_planes)
    return result_norm

sensor1 = Sensor(Koordinat(495, 395), Koordinat(560, 450), 1280, 720)
font = cv2.FONT_HERSHEY_SIMPLEX
while (1):
    ret, kare = video.read()
    arkaplansilinmis = fgbg.apply(kare)
    arkaplansilinmis = cv2.morphologyEx(arkaplansilinmis, cv2.MORPH_OPEN, kernel)
    cnts, hierarchy = cv2.findContours(arkaplansilinmis, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    sonuc = kare.copy()
    doldurulmusVideo = np.zeros((kare.shape[0], kare.shape[1], 1), np.uint8)
    for cnt in cnts:
        x, y, w, h = cv2.boundingRect(cnt)
        if  (w>30 and h>30):
            cv2.rectangle(sonuc, (x,y), (x+w, y+h), (0,255,0), thickness=4)
            cv2.rectangle(doldurulmusVideo, (x,y), (x+w, y+h), (255), thickness=cv2.FILLED)
    sensor1_maskeSonuc = cv2.bitwise_and(doldurulmusVideo, doldurulmusVideo, mask=sensor1.maske)
    sensor1_beyazPikselSayisi = np.sum(sensor1_maskeSonuc == 255)
    sensor1_oran = sensor1_beyazPikselSayisi / sensor1.maskeAlani
    print(sensor1_oran)
    if (sensor1_oran >= 0.10 and sensor1.durum == False):
        cv2.rectangle(sonuc, (sensor1.Koordinat1.x, sensor1.Koordinat1.y), (sensor1.Koordinat2.x, sensor1.Koordinat2.y),
                      (0, 255, 0), thickness=cv2.FILLED)
        sensor1.durum = True
    elif (sensor1_oran <= 0.10 and sensor1.durum == True):
        cv2.rectangle(sonuc, (sensor1.Koordinat1.x, sensor1.Koordinat1.y), (sensor1.Koordinat2.x, sensor1.Koordinat2.y), (0, 0, 255), thickness=cv2.FILLED)
        sensor1.durum = False
        sensor1.algilananAracSayisi += 1
    else:
        cv2.rectangle(sonuc, (sensor1.Koordinat1.x, sensor1.Koordinat1.y), (sensor1.Koordinat2.x, sensor1.Koordinat2.y), (0, 0, 255), thickness=cv2.FILLED)

    cv2.putText(sonuc, str(sensor1.algilananAracSayisi), (sensor1.Koordinat1.x, sensor1.Koordinat1.y + 60), font, 3, (255,255,255))
    cv2.imshow("sonuc",sonuc)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
video.release()
cv2.destroyAllWindows()