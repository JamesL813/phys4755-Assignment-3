import math

# Method to integrate over f(x) with the adaptive Simpson rule.
def  simpson2(a, b, delta, step, maxstep):
    h = b-a
    c = (b+a) / 2
    fa = f(a)
    fc = f(c)
    fb = f(b)
    s0 = h*(fa + 4*fc + fb) / 6
    s1 = h*(fa + 4*f(a + h / 4) + 2*fc + 4*f(a + 3*h / 4) + fb) / 12
    step += 1
    if (step >= maxstep):
        print("Not converged after " + str(step) + " recursions")
        return s1
    else:
        if (abs(s1-s0) < 15*delta):
            return s1
        else:
            return simpson2(a, c, delta / 2, step, maxstep) + simpson2(c, b, delta / 2, step, maxstep)
# Method to provide the integrand f(x).
def  f(x):
    return math.exp(-x**2)


if __name__=="__main__":
    n = 100
    delta = 1.0E-6
    k = 0
    a = 0
    b = math.pi
    
    file = open("simpsons_adapt.csv", "w")
    file.write("delta, S\n")

    for i in range(-150,-90):
        delta = 10**(i/10)
        s = simpson2(a, b, delta, k, n)
        file.write(str(delta)+","+str(s)+"\n")
    print("S = " + str(s))
