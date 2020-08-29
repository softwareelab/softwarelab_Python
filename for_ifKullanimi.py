harfler1 = "asdfghjkqwrety"
harfler2 = "oıuyrasşlkhfvx"
ayniolanlar = ""

for i in harfler1:
    if i in harfler2:
        ayniolanlar += i

for i in ayniolanlar:
    print(i, end="-")
