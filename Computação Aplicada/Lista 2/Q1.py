def continuar():
    cont = str(input("deseja continuar? ( s ou n ): "))
    if cont == "n":
        import sys
        sys.exit()

from numpy import *
from numpy.linalg import inv

while True:
    try: 
        # Ax=b >> x = A-¹b
        n = int(input("Digite a dimensão do seu sistema linear nxn, digite n: "))
        print("seu sistema é {} x {}".format(n,n))
        
        print("Vamos fazer a matriz A, sabendo que Ax = b")
        
        
        A = zeros((n,n))
        for i in range(n):
            for j in range(n):
                aij = float(input(" a{}{} = ".format(i+1,j+1)))
                A[i][j] = aij
                
        print("Vamos fazer a matriz b, sabendo que Ax = b")
        c = zeros((n)) 
        b = c[:,newaxis]    
        for j in range(n):
            a1j = float(input("a1{} = ".format(j+1)))
            b[j]= a1j
    
            
        x = inv(A).dot(b)
    
        print("\n \n Logo a sua solução é: \n \n {} \n \n".format(x))
        
        continuar()
    
    except (ValueError,RuntimeError,TypeError,NameError):
        print("\n")
        print("cheque as entradas")
        continuar()    