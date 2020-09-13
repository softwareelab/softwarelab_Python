import time
now = time.time()
print(time.gmtime())
print(time.localtime())
print(time.asctime())

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
print("işlem bitti")