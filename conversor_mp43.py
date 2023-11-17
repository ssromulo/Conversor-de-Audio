#Importação das bibliotecas necessárias
import os
from pydub import AudioSegment

#Especificação do caminho do diretório que contém os arquivos a serem convertidos
directory_path = './MP4'

#Array que irá guardar os nomes das músicas
music_name = []

#Posição das músicas dentro do array
pos_musicname = 0

#Checando se o caminho fornecido é um diretório
if os.path.isdir(directory_path):
    #Lista todos os arquivos do diretório
    files = [os.path.join(directory_path, file) for file in os.listdir(directory_path)]

#Filtra e exibe na tela todos os arquivos com extensão .mp4
print(f"Carregando arquivos mp4 do diretório {directory_path}\n")

for file in files:
    if file.endswith('.mp4') and os.path.isfile(file):
        music_name.append(os.path.basename(file))
        print(f'Arquivo de número {pos_musicname + 1}: ' + music_name[pos_musicname] + ' carregada no script.')
        pos_musicname = len(music_name)
    else:
        print(f"'{directory_path}' o caminho do diretório não é válido.")

print(f"\n>>> Total de arquivos mp4 carregados: {len(music_name)}")
#Convertendo os arquivos

def convert(musicname, directory):
    for x in range(len(musicname)):
        #Monta o caminho de origem do arquivo
        print(f'\n\n{musicname[x]}')
        save_from = directory + '/' + musicname[x]
        print('Abrindo diretório do arquivo')
        
        #Abre o arquivo MP4
        print("Abrindo o arquivo")
        audio = AudioSegment.from_file(save_from, format='mp4')

        #Removendo a extensão .mp4 do nome do arquivo
        musicname[x] = musicname[x][:-4] + '.mp3'

        #Montando o caminho de destino para o arquivo mp3
        save_as = './MP3/' + musicname[x]

        #Salvando o arquivo como mp3
        print("Convertendo e salvando em MP3...")

        try:
            #Converte o arquivo para mp3
            audio.export(save_as, format='mp3')

            #Informa que a conversão do arquivo teve sucesso
            print(f'[Sucesso]: O arquivo {musicname[x]} foi convertido para mp3 e já está disponível.')

        except Exception as erro:
            print(f"[ERRO] O seguinte erro foi encontrado durante a conversão: {erro}")

    #Finalização do script
    print("Fim da execução. Todas as músicas foram convertidas com sucesso.")

try:
    input(">>> Tecle enter para converter todas as músicas acima para mp3\n>>> Ou 'Ctrl + C' para cancelar...")
    convert(music_name, directory_path)
    input("Tecle Enter para fechar esta janela")
except Exception as erro:
    print(f"Um erro foi encontrado durante a conversão: \n{erro}")
    input("Tecle Enter para fechar esta janela")
