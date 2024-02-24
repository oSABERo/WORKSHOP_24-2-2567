# workshop_24-2-2567

# Import the Newton class from the newton module
from newton import Newton

# Define a test function for the Newton class
def test_newton():
    # Define a function f and its derivative df
    f = lambda x: x**2 - 4
    df = lambda x: 2*x

    # Create an instance of the Newton class with f and df
    nm = Newton(f, df)

    # Assert that the Newton method finds the roots of the function correctly
    assert round(nm.solve(10, 1e-10, 100), 10) == 2
    assert round(nm.solve(-10, 1e-10, 100), 10) == -2

# Define the Newton class
class Newton:
    # Initialize the Newton class with a function and its derivative
    def __init__(self, f, df):
        self.f = f
        self.df = df
    
    # Display the function and its derivative at a given point
    def display(self, x):
        print(f'f({x}) = {self.f(x)}')
        print(f'df({x}) = {self.df(x)}')
    
    # Solve for the root of the function using the Newton method
    def solve(self, x, tol, max_iter):
        # Iterate up to max_iter times
        for i in range(max_iter):
            # If the derivative at x is zero, print a message and break the loop
            if self.df(x) == 0:
                print('df(x) is zero')
                break
            # Update x using the Newton method formula
            x = x - self.f(x) / self.df(x)
            # Display the function and its derivative at the new x
            self.display(x)
            # If the absolute value of the function at x is less than the tolerance, break the loop
            if abs(self.f(x)) < tol:
                break
        # Return the found root
        return x

# Define a function f and its derivative df
def f(x):
    return x**3 - 4

def df(x):
    return 3*x**2

# Import the Newton class from the newton module
from newton import Newton

# Define a starting point x
x = 10
# Calculate the function and its derivative at x
f_x = f(x)
df_x = df(x)

# Create an instance of the Newton class with f and df
aaa = Newton(f, df)
# Solve for the root of the function starting from x
aaa.solve(x, 1e-10, 100)
