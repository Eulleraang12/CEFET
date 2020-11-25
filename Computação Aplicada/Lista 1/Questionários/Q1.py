
def continuar():
    cont = str(input("deseja continuar? ( s ou n ): "))
    if cont == "n":
        import sys
        sys.exit()

while True:
    try:
        va = [ ]
        print("Digite os termos do vetor Va")
        for i in range(5):
            v = float(input("Digite o %d ° termo:" %(i+1)))
            va.append(v)
        print("Va = {}".format(va))

        
        vb = [ ] 
        print("Digite os termos do vetor Vb")
        for i in range(5):
            v = float(input("Digite o %d ° termo:" %(i+1)))
            vb.append(v)


        vr = [ ] 
        for i in range(5):
            vr.append(va[i])
            vr.append(vb[i])
        print(" ")
        print("Va = ",va)
        print("Vb = ",vb,"\n")
        print("O vetor resultante é:")
        print("Vr = {}".format(vr))
        print("\n")
        
        continuar()
    except (ValueError,RuntimeError,TypeError,NameError):
        print("\n")
        print("cheque as entradas do vetor")
        continuar()
        
