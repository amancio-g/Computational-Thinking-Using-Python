massa = float(input("Qual seu peso? "))
altura = float(input("Qual sua altura?"))
imc = massa / altura ** 2
print("Este é é o seu IMC: " + str(imc))

if imc > 18.5 and imc < 24.9:
    print("Você está saudável")
elif imc > 25 and imc < 29.9:
    print("Sobrepeso")
elif imc > 30 and imc < 34.9:
    print("Obesidade I")
elif imc > 35:
    print("Obesidade II")
else:
    print("IMC abaixo do indicado.")
