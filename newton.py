import math
import matrix

def newton(d) :
    delta = d
    dx = [1.0,1.0]
    
    max_steps = 100
    
    x0 = [3.0,9.0]
    _f = [0.0,0.0]
    
    x = x0     # Initial guess in the middle
 
    #while (sum(dx)/len(dx) > delta) :   # Finish if step is too small
   # Finish if step is too small    
    for k in range(max_steps):
        if sum(dx)/len(dx) < delta:
            break
        print(k)
        print("dx:"+str(dx))
        print(_f)
        _f = f(x)
        dx = matrix.LU_decomp(J(x), matrix.mult(_f,-1))
        print("n:"+str(matrix.mult(dx,-1)))
        
        x = matrix.add(x, matrix.mult(dx,-1))    # Move guess by newton step
        
        print("x:"+str(x))
        
    print("Iteration number: "  + str(k))
    print("Root obtained: "     + str(x))
    print("Estimated error: "   + str(dx))
    return x

# Method to provide function f(x)=exp(x)*log(x)-x*x.
def  f(x):
    if type(x[0]) != list:
        return [math.exp(x[0]**2.0) * math.log(abs(x[1])) - x[0]**2,
                math.exp(x[1])    * math.log(abs(x[0])) - x[1]**2]
    else:
        return [math.exp(x[0][0]**2.0) * math.log(abs(x[1][0])) - x[0][0]**2,
                math.exp(x[1][0])    * math.log(abs(x[0][0])) - x[1][0]**2]

# Method to provide the Jacobian derivative f'(x1, x2).
def  J(x):
    
    if type(x[0]) != list:
        return [[2*x[0]*(math.log(abs(x[1]))*math.exp(x[0]**2)-1), 
                 math.exp(x[0]**2.0)/x[1]],
                [math.exp(x[1])/x[0],
                 math.log(abs(x[0]))*math.exp(x[1])-2*x[1]]]
    else:
        return [[2*x[0][0]*(math.log(abs(x[1][0]))*math.exp(x[0][0]**2)-1), 
                 math.exp(x[0][0]**2)/x[1][0]],
                [math.exp(x[1][0])/x[0][0],
                 math.log(abs(x[0][0]))*math.exp(x[1][0])-2*x[1][0]]]
            

if __name__=="__main__":
    
    file = open("newton.csv", "w")
    file.write("delta,rx,ry\n")
    
    for d in range(-100, -8):
        r = newton(10**(d/10))
        print("Root obtained: " + str(r) + ",")
        if type(r)==list:
            file.write(str(10**(d/10)) + "," + str(r[0]) + "," + str(r[1]) + "\n")
