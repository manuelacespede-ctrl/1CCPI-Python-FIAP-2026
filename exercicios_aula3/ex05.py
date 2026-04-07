a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a % b == 0 or b % a == 0:
    print("São Múltiplos")
else:
    print("Não são Múltiplos")