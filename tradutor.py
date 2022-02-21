print('''

 ██▓   ▓██   ██▓ ▄████▄   ▄▄▄       ▒█████   ███▄    █ 
▓██▒    ▒██  ██▒▒██▀ ▀█  ▒████▄    ▒██▒  ██▒ ██ ▀█   █ 
▒██░     ▒██ ██░▒▓█    ▄ ▒██  ▀█▄  ▒██░  ██▒▓██  ▀█ ██▒
▒██░     ░ ▐██▓░▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██   ██░▓██▒  ▐▌██▒
░██████▒ ░ ██▒▓░▒ ▓███▀ ░ ▓█   ▓██▒░ ████▓▒░▒██░   ▓██░
░ ▒░▓  ░  ██▒▒▒ ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
░ ░ ▒  ░▓██ ░▒░   ░  ▒     ▒   ▒▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
  ░ ░   ▒ ▒ ░░  ░          ░   ▒   ░ ░ ░ ▒     ░   ░ ░ 
    ░  ░░ ░     ░ ░            ░  ░    ░ ░           ░ 
        ░ ░     ░                                      

''')
print('≃≃≃≃ Feito por Arthur Oliveira para uso da Equipe Wild Lions Nova Iguaçu ≃≃≃≃')
id = input('Qual o nome do arquivo com as instruções do código? (ex.: 7184397.txt)\n')
texto = open(id, 'r')

content = texto.read()
splitadoCru = content.split('|')

base = open('base.py', 'r')

final = open('final.py', 'w+')

baseStr = base.read()

final.write(f'{str(baseStr)}\n')

Splitado = []
Splitado.append(splitadoCru[0])
Splitado.append(splitadoCru[2])
Splitado.append(splitadoCru[1])

del splitadoCru[0]
del splitadoCru[0]
del splitadoCru[0]

for i in range(len(splitadoCru)):
    Splitado.append(splitadoCru[i])


for i in range(len(Splitado)):
    acao = Splitado[i]
    valor = acao.split(' ')[-1]

    if acao.startswith('R'):
        final.write(f'\nAcelera(600, {valor}) # Robô segue em frente por {valor} mm.')
    if acao.startswith('E'):
        final.write(f"\nCurva(600, {valor}, 'left') # Robô realiza curva de {valor}° para a esquerda.")
    if acao.startswith('D'):
        final.write(f"\nCurva(600, {valor}, 'right') # Robô realiza curva de {valor}° para a direita.")

final.write('\n\n# FIM DA PROGRAMAÇÃO | GERADO AUTMATICAMENTE POR LYCAON #')