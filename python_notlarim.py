print("deneme\ndeneme2")
print("{} + {} = {}".format(2,3,2 + 3))
#yorum satırı bu sekilde bırakılır
"""
coklu yorum satırı kullanımı 3 tırnaktan olusur
"""

#toplama yaptık
a = 3
b = 5
c = a+b
print(c)
#integer


#string
d="python"
print(d)

#liste
e=[1,2,3,4,5,"python"]
print(e)

#tuple
f=(1,2,3,4,5,"python")
print(f)


#sözlük - dict
g={"elma":3, "armut":4, "kiraz":5}
print(g)


#boolean
h= False
print(h)

print(type(a))#int
print(type(b))#int
print(type(c))#int
print(type(d))#str
print(type(e))#list
print(type(f))#tuple
print(type(g))#dict
print(type(h))#bool


print(a,b,d)


#matematik operatörleri
print(3+4)
print(10-4)
print(3*5)
print(15/3)#5.0 verecek cıktı olarak , eger .0 kısmını istemiyorsak cift // kullanmalıyız
print(15//3)
print(10%4) #mod alma



#string toplama
a = "Python "
b="Programlama "
c="Dili"
d= a+b+c
print(d)


#yıldızlar
print("* " *1)
print("* " *2)
print("* " *3)
print("* " *4)
print("* " *5)
print("* " *6)






a="Python"
b=[1,2,3,4,5,6,7]
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(len(a)) #len() içinde kac eleman oldugunu belirtiyor
print(len(b))
print(a[0:2])#0. indexten basla, 2.index dahil değil , ekrana yaz
print(a[2:])#2. indexten basla, sonuna kadar al
print(a[:4])#bastan basla, 4. indexe kadar al



#sözlük
a={"elma":3, "armut":5, "kiraz":6}
print(a["kiraz"])
print(a["elma"])
print(a["armut"])


"""
#kullanıcıdan input alma
yas = input("yaşınızı girin: ")
print("yasınız",yas)

#tür belirtmezsek string gibi yan yana ekleme işlemi yapacak
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

print("toplam",a+b+c)

"""


"""
#if elif else

yas= int(input("yaşınızı girin"))
if yas < 18:
    print("18 den kücük")
elif yas>18 and yas < 25:
    print("18 - 25 arası")
elif yas > 25 and yas < 30:
    print("25-30 arası")
else :
    print("yas 30 dan büyük")
    
and / or kullanarak kosullandırma yapabiliriz


#true işlemi false yapar/false işlemini true yapar
if(not (3<4)):
print("Evet")
  
"""


"""
#döngü yapıları
#while
i = 1
while (i < 1000):
    print("i:", i)
    i *= 2
    #i = i +1
    #i += 1
"""

print("-------------------------------------------")
print("-------------------------------------------")
print("-------------------------------------------")
print("-------------------------------------------")



#break-continue
"""
i = 0
while(i<10):
    if i==5:
        break
    print("i:",i)
    i +=1
"""
"""
i = 0
while(i<10):
    #3 ve 5 oldugunda döngüyü atlayıp devam edecek, 
    # ekran cıktısında 3 ve 5 yer almayacak
    if i==3 or i ==5:
        i += 1
        continue
    print("i:",i)
    i +=1
"""



#for dongusu
"""
a=[1,2,3,4,5,6]
for i in a:
    print(i)
print("---------------")
b="python"
for karakter in b:
    print(karakter)
"""


"""    
#range kullanımı aralıktaki değerleri yazdırır
for sayi in range(20,30):
    print(sayi)
print("------------")
#range kullanımı aralıktaki değerleri yazdırır
#,2 dedigimiz 2 şer atlayarak yazdırır
for sayi in range(0,100,2):
    print(sayi)
"""



"""
#fonksiyon tanımlama
def selamla():
    print("Merhaba")


#fonksiyonu cagırma
selamla()

"""
"""
#değer gönderme
def selamla(isim):
    print("Merhaba", isim)
selamla("Deneme")
"""

"""
#değere bir veri aktardık
#biz cagırırken değer göndermezsek bize varsayılanı gönderecek
def selamla(isim = "isimsiz"):
    print("Merhaba", isim)
selamla("Deneme")
selamla()
"""
"""
def toplama(a,b,c):
    print("Toplam:", a+b+c)
toplama(3,4,5)
"""


"""
def toplama(a,b,c):
    return a+b+c
a= toplama(3,4,5)
print(a)
"""


liste = [1,2,3,4,5,6]
a="araba"
#baslangıc değeri a ile baslıyor mu
print(a.startswith("a"))#true değerini döndürür
print(a.startswith("b"))#false değerini döndürür
#bitiş değeri a ile baslıyor mu
print(a.endswith("a"))#true değerini döndürür
print(a.endswith("b"))#false değerini döndürür

#a harflerini o harfine dönüştürecek
print(a)
a=a.replace("a", "o")
print(a)

#liste sonuna ekleme
liste.append("python")
print(liste)
#son elemanı cıkarır
#içine index değeri girersek o değeri listeden cıkartır
liste.pop()
liste.pop(3)
print(liste)



print("----------------------")
print("----------------------")
print("----------------------")

"""
#dosya acmak için
file = open("dosya.txt", "w")#dosyayı olusturduk- dosyayı üzerine yazar
file.write("Python Dosya Yazdirma")#dosyaya yazdırdık
file.close()#dosyayı kapattık


file = open("dosya2.txt", "a")#dosyayı olusturduk- dosyanın sonuna ekleme yapar
# a= append
file.write("Python Dosya Yazdirma\n")#dosyaya yazdırdık- alt alta yazması için \n
file.close()#dosyayı kapattık

#dosyayı okumak için r=read
file = open("dosya2.txt", "r")
print("dosya2.txt okunuyor")
veri = file.read()
print(veri)
file.close()

"""

"""
file=open("dosya2.txt","r")
for satir in file:
    print(satir)
file.close()
"""




#OOP-NTP
class Account:
    def __init__(self,isim,numara,bakiye):
        self.self_isim = isim
        self.self_numara = numara
        self.self_bakiye = bakiye
    def hesapBilgileri(self):
        print("İsim: ",self.self_isim)
        print("Numara: ",self.self_numara)
        print("Bakiye: ",self.self_bakiye)
    def paraCek(self,miktar):
        if (self.self_bakiye - miktar < 0):
            print("Bakiyeniz Yeterli Değil")
        else:
            self.self_bakiye -= miktar
            print("Yeni Bakiye: ",self.self_bakiye)
    def paraYatir(self,miktar):
        self.self_bakiye += miktar
        print("Yeni Bakiye: ", self.self_bakiye)
account = Account("Mert Erdem", 123456, 1000)

account.hesapBilgileri()
print("------------")
print("Para çekme işlemi")
account.paraCek(800)
print("------------")
print("Para yatırma işlemi")
account.paraYatir(1000)














