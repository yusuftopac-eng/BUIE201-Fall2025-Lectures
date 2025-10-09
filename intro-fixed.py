x = 2

def f(x):
    x = x + 4
    print(x)  # LINE:1

print(x)  # LINE:2

def g(x):
    f(x)  # ← Hata buradaydı, f() yerine f(x) olmalı
    x = x + 10
    print(x)  # LINE:3

g(x)
f(x + 3)
# LINE:4