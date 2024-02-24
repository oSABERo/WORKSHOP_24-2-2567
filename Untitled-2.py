class NewtonMethod:
    def __init__(self, f, df):
        self.f = f
        self.df = df

    def solve(self, x0, tol=1e-10, max_iter=100):
        x = x0
        for i in range(max_iter):
            dx = x -self.f(x) / self.df(x)
            x += dx
            if abs(self.f(x)) < tol:
                return x
        raise ValueError('Newton method did not converge')