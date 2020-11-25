def continuar():
    cont = str(input("deseja continuar? ( s ou n ): "))
    if cont == "n":
        import sys
        sys.exit()
while True:
    try:
        mes = [ "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"]
        temp = [ ]
        for i in mes:
            temp_mes = float(input("Anote a temperatura média do mês de {}: ".format(i)))
            temp.append(temp_mes)

        media_ano = sum(temp)/len(temp)
        dici_mes = dict(list(zip(mes,temp)))

        print("\n")
        print("Abaixo estão os meses com temperaturas a cima da média anual de {:.3}°".format(media_ano))
        for i in mes:
            if dici_mes[i] > media_ano:
                print("{:.3} ----> {:.3}°".format(i,dici_mes[i]))       
        continuar()
    except (ValueError,RuntimeError,TypeError,NameError):
        print("\n")
        print("cheque as entradas de temperatura")
        continuar()