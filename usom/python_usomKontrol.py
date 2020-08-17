from tkinter import *
import datetime

def kontrol_et():
    dosya=open("usom.txt", "r")
    icerik=dosya.read()
    dosya.close()
    ip=girdi.get()
    bugun=datetime.datetime.now()
    if str(ip) in icerik:
        dosya=open("log.txt", "a")
        yazi=str(ip)+" zararlı\nTarih:"+str(bugun)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("IP zararlıdır")
    else:
        dosya=open("log.txt", "a")
        yazi=str(ip)+" zararlı değil\nTarih:"+str(bugun)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("IP zararlı değil")

top = Tk()
top.title("Usom IP Kontrol")

B = Button(top,text="Kontrol et",command = kontrol_et)
B.place(x=50, y=50)
B.pack()

label1 = Label(top, text="Kontrol edilecek IP adresini giriniz:")
label1.place(x=50, y=80)
label1.pack()

girdi = Entry(top)
girdi.place(x=50, y=90)
girdi.pack()

v = StringVar()
girdi2 = Entry(top, textvariable=v)
girdi2.place(x=50, y=100)
girdi2.pack()

top.mainloop()