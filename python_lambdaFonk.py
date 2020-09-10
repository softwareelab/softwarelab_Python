#lambda kullanarak
dizi = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x % 2 == 0, dizi)))



#lambda kullanmadan
dizi = [1,2,3,4,5,6,7,8,9]
def cift_mi(x):
    return x % 2 == 0
print(list(filter(cift_mi, dizi)))