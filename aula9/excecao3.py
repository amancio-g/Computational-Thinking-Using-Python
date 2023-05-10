try:
    number = input("Digite um numero: ")
    result = int(number) / 2
    print(f"O resultado é {number}")
except ValueError or TypeError():
    print("Não foi digitado um numero")

print("Fim do Programa.")