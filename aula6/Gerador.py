texto = "01"
num = 1 
qualquer_numero = 0.5
lista = ["meu nome no texto", 24,[1, 2, 3]]
print(lista)
variavel = True

if not variavel:
    print("Mostra algo aqui")
else:
    print("Exibe essa")

valor = 1


while variavel <= 10000:
    valor += 1 
    if valor % 2 == 0:
        continue
    print("esse numero é legal: " + str(valor))









for item in lista[2]:
    print("Item -> " + str(item))
