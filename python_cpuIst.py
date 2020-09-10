import psutil

def cpu_bilgi():
    print("="*20, "CPU Bilgi", "="*20)

    print("Fiziksel Çekirdek: ", psutil.cpu_count(logical = False))
    print("Toplam Çekirdek: ", psutil.cpu_count(logical = True))

    cpufreq = psutil.cpu_freq()
    print(f"Maksimum frekans: {cpufreq.max:.2f}Mhz")
    print(f"Minimum frekans: {cpufreq.min:.2f}Mhz")
    print(f"Şuanki frekans: {cpufreq.current:.2f}Mhz")

    print("CPU çekirdek kullanımları: ")
    for i, yuzde in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {yuzde}%")
    print(f"Toplam Cpu Kullanımı: {psutil.cpu_percent()}%")

if __name__ == "__main__":
    cpu_bilgi()