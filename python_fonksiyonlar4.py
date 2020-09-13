def func(*args, **kwargs):
    isimsiz_arguman = args
    isimli_arguman = tuple(kwargs.items())
    return isimsiz_arguman, isimli_arguman
"""
önce isimsiz argumanları
sonra isimli argumanları yazdırdık
"""

x,y = func(1,2,3,4,5,6,7,8,9, username='softwarelab', password='deneme123')
print(x)
print(y)