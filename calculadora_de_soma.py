while True:
    try:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        resultado = numero1 + numero2
        print(f"O resultado é {resultado}.")
        break
    except:
        print("Erro: digite apenas números. ")

