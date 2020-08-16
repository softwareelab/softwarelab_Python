#dosya oluşturmak için
# a= append
file = open("dosya2.txt", "a")#dosyayı olusturduk - dosyanın sonuna ekleme yapar
file.write("Python Dosya Yazdirma\n")#dosyaya yazdırdık - alt alta yazması için \n
file.close()#dosyayı kapattık
#dosyayı okumak için r=read
file = open("dosya2.txt", "r")
print("dosya2.txt okunuyor")
veri = file.read()#file içindekileri okuyup veriye aktardık
print(veri)#veri ekrana yazdırıldı
file.close()
