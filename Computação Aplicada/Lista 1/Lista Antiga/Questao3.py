while True:
    try:
        n = int(input("Quantos notas teve?: "))
        x = [ ]
        for i in range(n):
            l = float(input("Digite o %d° nota: " % (i+1) ))
            x.append(l) 

        print("Sua média é: ", sum(x)/n )

    except:
        print("Nota é um número!")