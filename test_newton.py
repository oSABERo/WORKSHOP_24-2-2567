from newton import Newton

def test_newton():
    f = lambda x: x**2 - 4
    df = lambda x: 2*x
    nm = Newton(f, df)
    assert round(nm.solve(10, 1e-10, 100), 10) == 2
    assert round(nm.solve(-10, 1e-10, 100), 10) == -2
