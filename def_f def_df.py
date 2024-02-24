def f(x):
    return x**3 - 4

def df(x):
    return 3*x**2

from newton import Newton

x = 10
f_x = f(x)
df_x = df(x)

aaa = Newton(f, df)
aaa.solve(x, 1e-10, 100)
