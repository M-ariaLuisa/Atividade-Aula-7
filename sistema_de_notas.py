while True:
    try:
        nota1 = float(input("Digite a 1ª nota: "))
        nota2 = float(input("Digite a 2ª nota: "))
        nota3 = float(input("Digite a 3ª nota: "))
        soma = nota1 + nota2 + nota3
        media = soma /3
        print(f"A média do aluno é {media:.2f}")
        if(media < 5):
            print(f"Reprovado")
        elif(media >= 5 and media <= 6.9):
            print(f"Recuperação")
        else:
            print("Aprovado")
        break
    except:
        print("Erro: digite apenas números.")

        
                            