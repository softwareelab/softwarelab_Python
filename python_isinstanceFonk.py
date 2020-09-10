x = "Software Lab"

if isinstance(x, int):
    print("bu bir tam sayı")
elif isinstance(x, str):
    print("bu bir karakter dizisi")
elif isinstance(x, tuple):
    print("bu bir demet")
elif isinstance(x, list):
    print("bu bir liste")
else:
    print("bu baska bir sey")