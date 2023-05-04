lista_de_usuarios = []


print("Bem vindo ao nosso programa. Selecione uma opçao:")
print("1 = Cadastrar Nome. ")
print("2 = Sair do Programa.")

while True:
    boasvindas = input("Cadastrado. Deseja 1 ou 2?")
    if boasvindas == str(2):
        break

    nome = input("Digite seu nome: ")
    lista_de_usuarios.append(nome)

print(lista_de_usuarios)

