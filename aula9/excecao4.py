people = input("Digite o numero de pessoas: ")
value = input("Digite quanto deu o churras: ")

try:
    total = float(value) / float(people)
    print(f"O resultado é {total}")
except TypeError:
    print("Não foi digitado um numero")

print("Fim do programa.")