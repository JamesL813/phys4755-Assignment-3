import math

def root(delta):
    delta, a, b, n = delta, 1, 2, 6 # delta, left, right bound, max steps
    dx, x = (b-a) / 10, (a+b) / 2   # guess in middle of a and b
    x =  secant(n, delta, x, dx)
    print("Root obtained: " + str(x))
    
# Method to carry out the secant search.
def secant(n, delta, x, dx):
    x1 = x + dx
    for k in range(n+1):
        if (abs(dx)<=delta):    # finish if step is too small
            break
        d =  f(x1) - f(x)
        x2 = x1-f(x1)*(x1-x)/d  # move guess by newton step
        x, x1 = x1, x2
        dx = x1-x
    if (k == n):
        print("Convergence not" + " found after " + str(n) + " iterations")
    return x1
    
# Method to provide function f(x)=exp(x)*log(x)-x*x.
# Changed to f(x)=e^(x^2)*ln(x^2)-x
def f(x):
    return math.exp(x**2) * math.log(x**2) - x
    

if __name__=="__main__":
    a, b, n = 1, 2, 500 # left, right bound, max steps
    dx, x = (b-a) / 10, (a+b) / 2   # guess in middle of a and b
    
    file = open("secant.csv", "w")
    file.write("delta,root\n")
    
    for d in range(-100, 0):
        r = secant(n, 10**(d/10), x, dx)
        print("Root obtained: " + str(r))
        file.write(str(10**(d/10)) + "," + str(r) + "\n")
