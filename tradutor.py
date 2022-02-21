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

Retas = []
Curvas = []

for i in range(len(splitadoCru)):
    movimento = splitadoCru[i].split(' ')
    if movimento[0].startswith('R'):
        Retas.append(movimento[-1])
    else:
        Curvas.append(splitadoCru[i])

Curvas.append('E 0')

for i in range(len(Retas)):
    reta = Retas[i]
    curva = Curvas[i]
    final.write(f'\nAcelera(600, {reta}) # Robô segue em frente por {reta} mm.')

    if curva.startswith('E'):
        valor = curva.split(' ')[-1]
        final.write(f"\nCurva(600, {valor}, 'left') # Robô realiza curva de {valor}° para a esquerda.")

    if curva.startswith('D'):
        valor = curva.split(' ')[-1]
        final.write(f"\nCurva(600, {valor}, 'right') # Robô realiza curva de {valor}° para a direita.")

final.write('\n\n# FIM DA PROGRAMAÇÃO | GERADO AUTMATICAMENTE POR LYCAON #')