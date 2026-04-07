a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

lados = [a, b, c]
lados.sort(reverse=True)  # ordena decrescente
a, b, c = lados

# forma triângulo
if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    # Calcula os quadrados para facilitar
    a2 = a ** 2
    b2 = b ** 2
    c2 = c ** 2

    # tipo de triângulo
    if a2 == b2 + c2:
        print("TRIANGULO RETANGULO")
    elif a2 > b2 + c2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    # equilátero e isósceles
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or a == c:
        print("TRIANGULO ISOSCELES")