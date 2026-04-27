def validar_nota (nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("Digite novamente a nota:"))
    return nota

notaA = float(input("Digite a 1° nota:"))
notaA = validar_nota(notaA)

notaB = float(input("Digite a 2° nota:"))
while notaB <0 or notaB >10:
    print("A nota deve estar entre 0 e 10")
    notaA = float(input("Digite novamente a nota:"))

media = (notaA + notaB) / 2
print(media)