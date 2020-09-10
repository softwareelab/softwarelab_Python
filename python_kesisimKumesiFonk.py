a = {1,2,3,4,5,'a', 'b','c',9,6,4}
b = {1,5,'a',9,4}

def kesisim(a:set,b:set):
    kesisim_kumesi = set()

    for a_eleman in a:
        for b_eleman in b:
            if a_eleman == b_eleman:
                kesisim_kumesi.add(a_eleman)
    if kesisim_kumesi:
        return kesisim_kumesi
    else:
        return False

print(kesisim(a,b))