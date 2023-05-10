def calcular():
    number = input("Digite um numero: ")
    result = int(number) / 2
    print(f"O resultado é {number}")

while True:
    try:
        calcular()
        break
    except:
        print("Não foi possivel realizar a conta")
        print("Acredito que você não digitou um numero")

    print("Fim do programa.")
