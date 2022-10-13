
def add_vec(v1, v2):
    """
    Adds 2 matrices and returns the result
    :param A: mxl Matrix 
    :param B: lxn Matrix
    :return: mxn matrix product
    """
    
    if len(v1) != len(v2):
        print(v1)
        print(v2)
        raise("cannot add two different sized vectors")
    
    n = len(v1)
    v3 = [0]*n
    
    for i in range(n):
        v3[i] = v1[i]+v2[i]
    return v3
    

def add(A, B):
    """
    Adds 2 matrices and returns the result
    :param A: mxl Matrix 
    :param B: lxn Matrix
    :return: mxn matrix product
    """
    
    if type(A[0] != list and B[0] != list):
        return add_vec(A, B)
    
    n = len(A)
    if type(A[0] != list or len(A[0]) == 1):
        if type(B[0] == list and len(B[0]) != 1):
            print_matrix(A)
            print_matrix(B)
            raise("cannot add two different sized matrices")
            
        m = 1
        C = [0] * n
    else:
        C = [[0] * n for i in range(m)]
        
    for i in range(m):
        for j in range(n):
            if type(A[i]!=list and B[i]!=list):
                C[j] = A[j]*B[j]
            if type(B[i]!=list):
                C[j] = A[i][j]*B[j]
            elif type(A[i]!=list):
                C[i][j] += A[j]*B[i][j]
            else:
                C[i][j] += A[i][j]+B[i][j]
    return C

def mult_vec_const(v, c):
    """
    Multiplies 2 matrices and returns the result
    :param v: mxl Matrix 
    :param c: constant
    :return: mxl matrix product
    """
    l = len(v)
    
    C = [0]*l

    for k in range(l):
        C[k] = v[k]*c
    return C

def mult_const(A, c):
    """
    Multiplies 2 matrices and returns the result
    :param A: mxl Matrix 
    :param c: constant
    :return: mxl matrix product
    """
    m = len(A)
    
    if type(A[0]!=list):
        return mult_vec_const(A, c)
    
    l = len(A[0])
    
    C = [[0] * l for i in range(m)]

    for i in range(m):
        for k in range(l):
            C[i][k] += A[i][k]*c
    return C

def mult_vec(A, v):
    """
    Multiplies 2 matrices and returns the result
    :param A: mxl Matrix 
    :param v: vector length l
    :return: vector product length l
    """
    m = len(A)    
    
    l = len(A[0])
    
    if len(v) != l:
        print("Cannot multiply "+str(m)+"x"+str(l)+
            "matrix with vector of length "+ str(len(v)))
        return
        
    c = [0]*l
    for i in range(m):
        for k in range(l):
            c[k] += A[i][k]*v[k]
    return c
    


def mult(A, B):
    """
    Multiplies 2 matrices and returns the result
    :param A: mxl Matrix 
    :param B: lxn Matrix
    :return: mxn matrix product
    """
    if type(B)!=list:
        return mult_const(A, B)
        
    if type(B[0])!=list:
        return mult_vec(A, B)
    
    m = len(A)    
    
    n = len(B[0])
    
    l = len(A[0])

    if l != len(B):
        print("Cannot multiply " + str(l) + "x" + str(len(B)) + " matrix")
        return
   
    C = [[0] * n for i in range(m)]

    for i in range(m):
        for j in range(n):
            for k in range(l):
                C[i][j] += A[i][k]*B[k][j]
    return C
    

def mod(A, n):
    """
    Applies mod(n) to every element in matrix A
    :param A: matrix on which we will apply mod(n)
    :param n: number to use in mod function
    :return: matrix with updated values
    """
    for i in range(len(A)):
        if type(A[i]) != list:
            A[i] %= n
        else:
            for j in range(len(A[0])):
                A[i][j] %= n
    return A


def LU_decomp(A, b):
    """
    Solves Ax=b using the LU decomposition method
    :param A: matrix nxn
    :param b: vector of length n
    :return x: solved x values
    """
    n = len(A)
    if (len(A[0]) != n or len(b) != n):
        print("A not a square matrix or b not correct vector size")
        exit()
    L = [[0] * n for i in range(n)]
    U = [[0] * n for i in range(n)]
    d, w = [0]*n, [0]*n
    e, c, v, t = [0]*(n-1), [0]*(n-1), [0]*(n-1), [0]*(n-1)
    for i in range(n):
        for j in range(n):
            if i == j:
                d[i] = A[i][j]
                if i == 0 and j == 0:
                    w[0] = d[0]
                L[i][j] = w[i]
                U[i][j] = 1
            elif j == i-1:
                c[i-1] = A[i][j]
                v[i-1] = A[i][j]
                L[i][j] = v[i-1]
            elif i == j-1:
                e[i] = A[i][j]
                t[i]=e[i]/w[i]
                U[i][j] = t[i]
            w[i]=d[i]-v[i-1]*t[i-1]
    y = [0]*n
    z = [0]*n
    y[0] = b[0]/w[0]
    for i in range(1,n):
        y[i] = (b[i]-v[i-1]*y[i-1])/w[i]
    z[n-1] = y[n-1]
    for i in range(n-2,-1,-1):
        z[i] = y[i]-t[i]*z[i+1]
    return z

def print_matrix(A):
    """
    Prints matrix A in a readable format
    :param A: matrix to print
    """
    for r in A:
        print("|", end = " ")
        if r != list:
            print(r, end = " ")
        else:
            for e in r:
                print(e, end = " ")
        print("|")
    print()

if __name__ == "__main__":
    A = [[1,2,3],[4,5,6]]
    B = [[5],[6],[7]]
    print("A:")
    print_matrix(A)
    print("B:")
    print_matrix(B)
    C = mult(A,B)
    print("C:")
    print_matrix(C)
    C = mult(A,2)
    print("C:")
    print_matrix(C)
    
    # Driver code
    mat = [[2, -1, -2],
           [-4, 6, 3],
           [-4, -2, 8]]
    b = [30,4,5]
    
    print("mat:")
    print_matrix(mat)

    print(LU_decomp(mat,b))
    
