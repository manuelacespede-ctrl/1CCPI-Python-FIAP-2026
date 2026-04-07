import os

def tocar_audio(arquivo):
    os.system(f'start {arquivo}')

arquivo = input("Digite o nome do arquivo: ")

if arquivo.endswith(".mp3"):
    tocar_audio(arquivo)
else:
    print("Arquivo inválido")