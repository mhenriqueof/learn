# Módulos
import emoji
# Cores
we = '\033[1m'
gn = '\033[42m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':soccer: {gn} Brasileirão 2022 {cc} :soccer:',use_aliases=True))
# Lista dos 20 primeiros colocados
times = ('Corinthians', 'Palmeiras', 'São Paulo', 'Atlético Mineiro', 'Botafogo', 'Santos', 'Fluminense', 'Coritiba', 'América-MG', 'Avaí', 'Internacional', 'Athletico-PR', 'Bragantino', 'Flamengo', 'Goiás', 'Atlético-GO', 'Juventude', 'Ceará', 'Fortaleza')
print(f'{we}{times}{cc}')
# 5 primeiros
print(f'Os {we}cinco primeiros colocados{cc} são: {gn}{times[0:5]}{cc}\n')
# 4 últimos
print(f'No {we}sopé da tabela{cc} estão: {gn}{times[-4:]}{cc}\n')
# Ordem alfabética
print(f'A lista dos times em {we}ordem alfabética{cc}: {gn}{sorted(times)}{cc}\n')
# Posição Santos
santos = times.index('Santos')
print(f'O {gn}Santos{cc} se encontra na {we}posição {santos + 1}ª{cc} da tabela.\n')
# Encerramento
print(emoji.emojize(f':soccer: {gn} Brasileirão 2022 {cc} :soccer:',use_aliases=True))
