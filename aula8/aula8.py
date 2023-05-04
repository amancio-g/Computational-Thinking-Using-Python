# criar um dicionario com função geral:
my_dict= dict(first_name="Leonardo", last_name="Bragatti")
empty_dict = {}

print(my_dict)

#mostra tudo que o number possui, dir mostra tudo que está declarado no seu objeto.
number = 5 
my_dict - {1}
for prop in dir(my_dict):
    print(prop)

#mostra uma lista com posições, ajuda com a identificação
names = ["Alysson", 'Marcel', 'Daniel', 'Anna']

for position, name in enumerate(names):
    print("Posição " + str(position))
    print("Nome " + name)

#mostra toda a documentação de um objeto ( se possuir)
names = ["Alysson", 'Marcel', 'Daniel', 'Anna']
name = "string"
print(help(names))

#uma função que vc espera uma entrada de dados do usuario de fora

name=input("Digite seu nome: ")
print(name)


#

numer=int("5")
print(number)

#
number = float("5.9321321321312")
print(number)

#contar a quantidade de coisas que tem no que vc dar para ele

name = "Leonardo"
itens = {"chave": "valor",
         "chave2": ["item 1", "item 2"]
}

print(len(name))

#retorna o maior valor da sequencia, pode ser utilizado em lista
numbers = ["4", "5", "6", "2", "13", "2442"]
highest = max(numbers)
print(highest)

#retorna o menor valor
numbers = ["4", "5", "6", "2", "13", "2442"]
minium = min(numbers)
print(minium)

#exibe mensagem
print("Exibir uma mensagem")


#arrendondar

pi = 10/3
print(pi)

#ordernar os elementos de uma sequencia.

names = ["Pedro", "Gabriel", "Leonardo"]
sorted_names = sorted(names)
print(sorted_names)

#soma numeros

numbers=range(10)
result = sum([1, 2, 3.43, 4, 5])
print(result)
