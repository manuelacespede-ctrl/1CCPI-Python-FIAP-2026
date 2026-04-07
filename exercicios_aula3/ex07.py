ano_nasc = int(input("Digite o ano de nascimento: "))

# Calcula a idade considerando o ano atual (2026)
idade = 2026 - ano_nasc

# Verifica a situação do voto
if idade < 16:
    print("Voto proibido")
elif 16 <= idade < 18 or idade > 70:
    print("Voto opcional")
else:
    print("Voto obrigatório")