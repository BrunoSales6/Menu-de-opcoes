valor1=float(input("Digite um valor: "))
valor2=float(input("Digite um valor: "))
opcao=0
while opcao!=5:
    print('''[1]Somar
[2]Multiplicar
[3]Maior
[4]Outros valores
[5]Finalizar programa
    ''')
    opcao=int(input("O que você gostaria de fazer?"))
    if opcao==1:
        print(f"O valor da sua soma é {valor1+valor2}")
    elif opcao==2:
        print(f"O valor da sua multiplicação é {valor1*valor2}")
    elif opcao==3:
        if valor1>valor2:
            print(f"O maior valor é {valor1}")
        else:
            print(f"O maior valor é {valor2}")
    elif opcao==4:
        valor1=float(input("Digite um valor"))
        valor2=float(input("Digite um valor"))
    elif opcao==5:
        print("Finalizando o programa..")
    else:
        print("Opção inválida")
print("Fim do programa. Até!!")