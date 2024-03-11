#Definição de variáveis.
anos_fumando= float(input("\nInforme o tempo em anos que voçê fuma: "))
preco_maco = float(input("\nInforme o valor em reais atual do maço: "))
qtd_macos_dia = float(input("\nInforme a media de maços que voçê fuma por dia: "))


#Convertendo anos em dias fumando.
dias_fumando = int(anos_fumando * 365)

#Calculando o Montante.
Montante = dias_fumando * preco_maco * qtd_macos_dia
print("\nCalculando o montante...")
print("O seu montante é: R$" + str(Montante))

if Montante < 20000:
    print(f"Com o valor de R$ {Montante:.2f}, voçê poderia ter dado entrada em um carro.")
elif 20000 <= Montante <= 50000:
    print(f"Com o valor de R$ {Montante:.2f}, Voçê poderia ter comprado um carro popular usado.")
else:
    print(f"Com o valor de R$ {Montante:.2f}, voçê poderia ter comprado um carro zero.")