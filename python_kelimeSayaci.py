from sys import argv, exit
from os.path import isdir, isfile, islink, exists


class KelimeSayaci:
    @staticmethod
    def argumanlari_kontrol_et(option):
        izinverilen_args = '-l', '-w', '-c', '--help'
        if option in izinverilen_args:
            return True
        else:
            return False

    @staticmethod
    def yardim_sayfasi():
        msg: """
        Kelime Sayacı --- Yardım Sayfası
        Kelime Sayacı, dosyalarınızda kaç satır, kelime ve karakter olduğunu
        gösteren, Python ile kodlanmış bir programdır.
        
        Examples:
        wdc -l example.txt
        wdc -w example.txt
        wdc -c example.txt
        wdc example.txt
        
        -l:\t Dosyadaki satır sayısını gösterir
        -w:\t Dosyadaki kelime sayısını gösterir
        -c:\t Dosyadaki karakter sayısını gösterir
        
        Herhangi bir parametre kullanılmadığındaaa tüm bilgiler gösterilir.
        
        """
        return msg

    @staticmethod
    def dogrula(file):
        if not exists(file):
            return 4
        if isfile(file):
            return 1
        if isdir(file):
            return 2
        if islink(file):
            return 3

    @staticmethod
    def satir_say(file=None, data=None):
        if not data:
            #eğer ki verilmiş bir data yoksa
            with open(file) as f:
                data = f.read()

        l = data.count('\n') + 1
        if data[-1] == '\n':
            l -= 1
        return l


    @staticmethod
    def kelime_say(file=None, data=None):
        if not data:
            with open(file) as f:
                data = f.read()
        data = data.replace('\n', ' ')
        w=len(data.split(' '))
        return w


    @staticmethod
    def harf_say(file=None, data=None):
        if not data:
            with open(file) as f:
                data = f.read()

        c = len(data)
        return c


def main():
    if len(argv) == 2:
        file_or_arg = argv[1]
        if file_or_arg == '--help':
            print(KelimeSayaci.yardim_sayfasi())
            exit()

        if KelimeSayaci.dogrula(file_or_arg) == 1:
            with open(file_or_arg) as f:
                data = f.read()
            result = "{} {} {} : '{}'".format(KelimeSayaci.satir_say(data=data),
                                              KelimeSayaci.kelime_say(data=data),
                                              KelimeSayaci.harf_say(data=data),
                                              file_or_arg)

            print(result)

        elif KelimeSayaci.dogrula(file_or_arg) == 2:
            print("Bu bir dizin!")
            exit()
        elif KelimeSayaci.dogrula(file_or_arg) == 3:
            print("Bu bir link!")
            exit()
        else:
            print("Biçim tanınmıyor!")
            exit()
    elif len(argv) == 3:
        file = argv[2]
        option = argv[1]
        if KelimeSayaci.dogrula(option) and KelimeSayaci.dogrula(file):
            if option == '-l':
                result = "{} :'{}'".format(KelimeSayaci.satir_say(file=file), file)
                print(result)

            elif option == '-w':
                result = "{} :'{}'".format(KelimeSayaci.kelime_say(file=file), file)
                print(result)

            elif option == '-c':
                result = "{} :'{}'".format(KelimeSayaci.harf_say(file=file), file)
                print(result)

            else:
                print(KelimeSayaci.yardim_sayfasi())
        else:
            print(KelimeSayaci.yardim_sayfasi())
    else:
        print(KelimeSayaci.yardim_sayfasi())


if __name__ == '__main__':
    main()
else:
    pass
