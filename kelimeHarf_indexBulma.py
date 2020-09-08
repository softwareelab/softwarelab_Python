alfabe = " abcçdefgğhıijklmnoöprsştuüvyz"
kelime = input("kelime: ")

sozluk = {}
for i in kelime:
    sozluk[i] = alfabe.index(i)

print(sozluk)
