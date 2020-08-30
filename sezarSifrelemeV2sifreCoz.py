k_alfabe = "abcçdefgğhıijklmnoöprsştuüvyzxwq +-*\\/)({}&%$#^'!abc"
b_alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZXWQ ABC"

cumle = input("Cümle: ")
yenicumle = ""
for i in cumle:
    if i in k_alfabe:
        indeks = k_alfabe.index(i)
        yenicumle += k_alfabe[indeks - 3]
    elif i in b_alfabe:
        indeks = b_alfabe.index(i)
        yenicumle += b_alfabe[indeks - 3]
    else:
        print("bu karakter alfabe düzeninde mevcut değil!")
        print("çevrilebilen kısım: ", yenicumle)
        quit()
print(yenicumle)