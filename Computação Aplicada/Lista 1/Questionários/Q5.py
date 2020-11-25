preço = 1.99
quantidade = 50
print("Lojas Quase Dois - Tabelas de preços")
for i in range(quantidade+1):
    print('{} ----> R$ {:.4}'.format(i,i*preço))