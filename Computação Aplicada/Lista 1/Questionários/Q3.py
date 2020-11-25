def continuar():
    cont = str(input("deseja continuar? ( s ou n ): "))
    if cont == "n":
        import sys
        sys.exit()

while True:
    try:
        nota1 = float(input("Nota da P1:"))
        nota2 = float(input("Nota da P2:"))
        media = (nota1+nota2)/2

        situacao = ['Aprovado','Reprovado',"Aprovado com Distincao"]

        if media >= 7:
            print("media de {:.3}, o aluno {}".format(media, situacao[0]))
        elif media < 7:
            print("media de {:.3}, o aluno {}".format(media, situacao[1]))
        elif media == 10:
            print("media de {:.3}, o aluno {}".format(media, situacao[2]))
            
        continuar() 
    except (ValueError,RuntimeError,TypeError,NameError):
        print("\n")
        print("cheque as entradas da nota")
        continuar()    