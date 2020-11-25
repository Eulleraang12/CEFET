def continuar():
    cont = str(input("deseja continuar? ( s ou n ): "))
    if cont == "n":
        import sys
        sys.exit()

from numpy import *
from numpy.linalg import inv
import pandas as pd
from numpy.core.multiarray import zeros
from numpy.core.numeric import newaxis

file = pd.read_excel(r"C:/Users/eulle/OneDrive - cefet-rj.br/Cefet Eng Eletrica/6°periodo/Computação Aplicada/Lista 2/DadosQ2.xlsx", engine="openpyxl")

print("\n \n Digite sua matriz A e b no arquivo excel, na primeira coluna vc pode começar a digitar a matriz A\n")
print(file)

while True:
    try:
        
        n = file.shape[0] - 1
        A = zeros((n,n))
        for i in range(n):
            for j in range(n):
                A[j][i] = file[i+1][j+1]
        
        print("\n \n Sua matriz A é: \n\n {}\n\n".format(A))
        
        c = zeros((n)) 
        b = c[:,newaxis]    
        
        for i in range(n):
            b[i] = file['b'][i+1]
        print("\n \n Sua matriz b é: \n\n {}\n\n".format(b))
        
        
        x = inv(A).dot(b)
    
        print("\n \n Logo a sua solução é: \n \n {} \n \n".format(x))
        
        continuar()
    
    except (ValueError,RuntimeError,TypeError,NameError):
        print("\n")
        print("arrume formatacao da planilha")
        continuar() 