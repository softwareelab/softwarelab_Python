def func(islem):
    def toplama(*args):
        return sum(args)

    def cikarma(x, y):
        return x-y
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    def bolme(x,y):
        return x//y

    if islem == 'toplama':
        return toplama
    elif islem == 'cikarma':
        return cikarma
    elif islem == 'carpma':
        return carpma
    elif islem == 'bolme':
        return bolme
    else:
        print("yanlıs islem!")
        return None
x = func('toplama')
print(x(1,2,3,4,5,5))
x = func('cikarma')
print(x(5,1))
x = func('carpma')
print(x(1,5,5,2))
x = func('bolme')
print(x(20,5))