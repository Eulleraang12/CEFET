while True:
    try:
        l = input("Digite uma palavra: " )
        l = list(l)
        x=[ ]
        y=[ ]
        num = [ ] 
        for i in l:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
                x.append(i)
            elif ord(i) in list(range(49,57)):
                num.append(i)
            else:
                y.append(i)
        print("temos", len(x),"vogais", len(y),"consoantes e ", len(num),"numeros" )
    except:
        print( "digite uma letra")
               
    

