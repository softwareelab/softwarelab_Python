import platform

def system_informations():
    print("="*20, "System Information", "="*20)
    uname = platform.uname()
    print(f"Sistem: {uname.system}")
    print(f"Bilgisayar Adı: {uname.node}")
    print(f"Sürüm: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Mimari: {uname.machine}")
    print(f"İşlemci: {uname.processor}")

if __name__ == "__main__":
    system_informations()