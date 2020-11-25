while True:
    try:
        n = int(input("Quantos termos o seu vetor: "))
        x = [ ]
        for i in range(n):
            l = float(input("Digite o %d° do vetor : " % (i+1) ))
            x.append(l)
        print(x)
    except:
        print("Digite um numero!")
    
          