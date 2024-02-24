from newton import Newton

def test_newton():
    f = lambda x: x**2 - 4
    df = lambda x: 2*x
    nm = Newton(f, df)
    assert nm.solve(10, 1e-10, 100) == 2
    assert nm.solve(-10, 1e-10, 100) == -2
