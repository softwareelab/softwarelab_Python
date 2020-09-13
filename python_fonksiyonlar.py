def func(a, b):
    return sum((a,b))

x = func

print(x(5,2))

print('x ID:', id(x))
print('func ID:', id(func))