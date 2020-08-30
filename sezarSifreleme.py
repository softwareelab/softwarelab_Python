alfabe = "abcçdefgğhıijklmnoöprsştuüvyzxwq abc"
cumle = input("Cümle: ")
yenicumle = ""
for i in cumle:
    print("Harf -->", i, "   ---Gerçek index -->", alfabe.index(i),
          "   ---Şifrelenmiş index -->", alfabe.index(i) + 3, "   ---Şifreli karakter -->",
          alfabe[alfabe.index(i) +3])
    indeks = alfabe.index(i)
    yenicumle += alfabe[indeks + 3]
print(yenicumle)