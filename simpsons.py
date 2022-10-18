import math

# The method of the Simpson rule in nonuniform meshes.
def  simpson(x, y) :
    n = len(y) - 1
    h = [0.0]*(n)
    for i in range(n):
        h[i] = x[i + 1] - x[i]
    s = 0
    for i in range(1, n, 2):
        a = h[i]*h[i]
        b = h[i]*h[i-1]
        c = h[i-1]*h[i-1]
        d = h[i] + h[i-1]
        alpha = (2*a + b - c) / h[i]
        beta = d*d*d / b
        gamma = (-a + b + 2*c) / h[i-1]
        s += alpha*y[i+1] + beta*y[i] + gamma*y[i-1]
    # Add the last slice separately for an even n+1
    if ((n + 1) % 2 == 0) :
        alpha = h[n-1] * (3 - h[n-1] / (h[n-1] + h[n-2]))
        beta = h[n-1] * (3 + h[n-1] / h[n-2])
        gamma = -h[n-1] * h[n-1] * h[n-1] / (h[n-2]*(h[n-1] + h[n-2]))
        return (s + alpha*y[n] + beta*y[n-1] + gamma*y[n-2]) / 6
    else:
        return s / 6

def fn(x):
   return math.exp(-x**2) 

if __name__=="__main__":
    n = 25 
    
    s = []
    h = 0.1
    alpha = 0.1
    
    file = open("simpsons.csv", "w")
    file.write("n,S\n")
    

    for n in range(1, 20):
        
        x = []
        f = []
        for i in range(n+1):
            x.append(h * math.exp(alpha*i**2))
            f.append(fn(x[i]))
        s.append(simpson(x, f) * 2)
        file.write(str(n)+","+str(s[n-1])+"\n")

    print("The integral is: " + str(s))

